'''
ResNet-18 modified to 1D physiological signal inputs.
Organized and simplified from: https://pytorch.org/vision/main/_modules/torchvision/models/resnet.html#resnet18
'''
import torch
import torch.nn as nn
from torch import Tensor

def conv3x1(in_channels: int, out_channels: int, stride: int = 1) -> nn.Conv1d:
    """3x1 convolution with padding, output_len=input_len"""
    return nn.Conv1d(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=3,
        stride=stride,
        padding=1, #If dilation =n, then kernel size is equivalent to 3+2n. To keep same output size, use padding=dilation.
        groups=1,
        bias=False,
        dilation=1,
    )


def conv1x1(in_channels: int, out_channels: int, stride: int = 1) -> nn.Conv1d:
    """1x1 convolution with no padding, output_len=input_len """
    return nn.Conv1d(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=1,
        stride=stride,
        bias=False,
    )
  
class BasicBlock(nn.Module): #BasicBlock always have dilation=1 and groups=1
    expansion: int = 1 #Basic block expect input and output to have same number of channels
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        stride: int = 1,
        downsample = None,
        norm_layer = nn.BatchNorm1d,
    ) -> None:
        super(BasicBlock,self).__init__()
        # Both self.conv1 and self.downsample layers downsample the input when stride != 1
        self.conv1 = conv3x1(in_channels, out_channels, stride=stride)
        self.bn1 = norm_layer(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = conv3x1(out_channels, out_channels, stride=1)
        self.bn2 = norm_layer(out_channels)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x: Tensor) -> Tensor:
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.downsample is not None:
            identity = self.downsample(x)

        out += identity
        out = self.relu(out)

        return out
      
      
class ResNet(nn.Module):

    def __init__(self, block=BasicBlock, layers=[2,2,2,2], num_BP=1, zero_init_residual=False, norm_layer=nn.BatchNorm1d):
        super(ResNet, self).__init__()
        self._norm_layer = norm_layer

        self.input_channels = 64

        
        self.conv1 = nn.Conv1d(2, self.input_channels, kernel_size=7, stride=2, padding=3,
                               bias=False) # 2CH -> 64CH, NowLen->Len/2
        self.bn1 = norm_layer(self.input_channels)
        self.relu = nn.ReLU(inplace=True) 
        
        self.maxpool = nn.MaxPool1d(kernel_size=3, stride=2, padding=1) #NowLen->Len/4
        
        self.layer1 = self._make_layer(block, out_channels=64, num_blocks=layers[0]) # 64CH->64CH, NowLen=Len/4
        
        self.layer2 = self._make_layer(block, out_channels=128, num_blocks=layers[1], stride=2) # 64CH->128CH, NowLen=Len/8
        
        self.layer3 = self._make_layer(block, out_channels=256, num_blocks=layers[2], stride=2) # 128CH->256CH, NowLen=Len/16
        
        self.layer4 = self._make_layer(block, out_channels=512, num_blocks=layers[3], stride=2) # 256CH->512CH, NowLen=Len/32
        
        self.avgpool = nn.AdaptiveAvgPool1d(1) # Final feature map =512*1
        self.fc = nn.Linear(512 * block.expansion, num_BP)

        for m in self.modules():
            if isinstance(m, nn.Conv1d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

        # Zero-initialize the last BN in each residual branch,
        # so that the residual branch starts with zeros, and each residual block behaves like an identity.
        # This improves the model by 0.2~0.3% according to https://arxiv.org/abs/1706.02677
        if zero_init_residual:
            for m in self.modules():
                if isinstance(m, BasicBlock):
                    nn.init.constant_(m.bn2.weight, 0)

    def _make_layer(self, block, out_channels, num_blocks, stride=1):
        norm_layer = self._norm_layer
        downsample = None
            
         # Adjust the identity mapping method to match desired number of channels and length   
        if stride != 1 or self.input_channels != out_channels * block.expansion:
            downsample = nn.Sequential(
                conv1x1(self.input_channels, out_channels * block.expansion, stride),
                norm_layer(out_channels * block.expansion),
            )

        layers = []
        # The first block adapt input channel to output channel, and downsample the length 
        layers.append(block(self.input_channels, out_channels, stride, downsample, norm_layer))
        
        # Next time when _make_layer is called, the input channel is the previous output channel
        self.input_channels = out_channels * block.expansion 
        
        # The rest of blocks do not change length or channels
        for _ in range(1, num_blocks):
            layers.append(block(self.input_channels, out_channels, norm_layer=norm_layer))

        return nn.Sequential(*layers)

    def _forward_impl(self, x):
        # See note [TorchScript super()]
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x

    def forward(self, x):
        return self._forward_impl(x)

def Resnet18_1D(**kwargs):
    return ResNet(**kwargs)
  
  
      
      