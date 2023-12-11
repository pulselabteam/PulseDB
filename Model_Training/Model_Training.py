import torch
import torch.utils.data as data
import random
import numpy as np
from mat73 import loadmat
from Model_Def.Trainer import Model_Trainer
from Model_Def import ResNet



def Seed(seed): 
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

class Dataset(data.Dataset):
    def __init__(self, Input, Label):
        self.Input = Input
        self.Label = Label

    def __len__(self):
        return len(self.Input)

    def __getitem__(self, idx):
        return self.Input[idx, :], self.Label[[idx]]


def Build_Dataset(Path, Label):
    Data = loadmat(Path)
    # Get the first two channels, which are the ECG and the PPG signals
    return Dataset(Data['Subset']['Signals'][:, 0:2, :], Data['Subset'][Label])


# Replace 'YOUR_PATH' with the folder of your generated Training, CalBased and CalFree testing subsets.
data_folder = 'YOUR_PATH'
Train_File = data_folder+'Train_Subset.mat'
Test_CalBased_File = data_folder+'CalBased_Test_Subset.mat'
Test_CalFree_File = data_folder+'CalFree_Test_Subset.mat'


# Training model for estimating SBP. Replace 'SBP' with 'DBP' to train model for DBP.
Train_Data = Build_Dataset(Train_File, 'SBP')
Test_CalBased_Data = Build_Dataset(Test_CalBased_File, 'SBP')
Test_CalFree_Data = Build_Dataset(Test_CalFree_File, 'SBP')
# %% Start model training

if __name__ == '__main__':
    # Initialize model 
    Seed(6)
    model = ResNet.Resnet18_1D()
    Seed(6)
    
    # Prepare settings to be recorded
    Settings = {'BP_optimizer': 'torch.optim.Adam(model.parameters(), lr=1e-6, betas=(0.9, 0.999), weight_decay=0)',
                'trainer': 'Model_Trainer(model,torch.nn.MSELoss(), BP_optimizer, device, Settings,batch_size=32, num_epochs=100, save_states=True, save_final=True)'
                }
    # Setup training device
    torch.cuda.empty_cache()
    device = torch.device("cuda:0" if (torch.cuda.is_available()) else "cpu")
    print(device)
    print(torch.cuda.get_device_name(0))
    model.to(device)
    # Instantiate optimizer and model trainer
    BP_optimizer = eval(Settings['BP_optimizer'])
    model_trainer = eval(Settings['trainer'])
    # Set the training set and the two setting set under comparison
    model_trainer.Set_Dataset(Train_Data, {
                              'Test_CalBased': Test_CalBased_Data, 'Test_CalFree': Test_CalFree_Data})
    model_trainer.Train_Model()
    # Find the curves of error metrics in the TensorBoard folder
