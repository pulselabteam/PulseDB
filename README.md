# PulseDB v2_0

- We have updated PulseDB to `v2_0` in the `main` branch. To check the historical data and repository published along the paper, see branch [v1_0](https://github.com/pulselabteam/PulseDB/tree/v1_0).
- In `v2_0`, we re-generated the `5,361` MATLAB data files in PulseDB, such that they have all fields present in `v1_0` (corresponding to the paper), plus the following new fields:
  - `T`: The absolute timestamp of each sample in the 10-s segment
    - Notes: PulseDB retrieves 1 consecutive clip from each MIMIC/VitalDB record, divides the clip into 10-s segments, and removes those 10-s segments of bad quality. `T` locates the temporal position of each sample in the 10-s segment within this consecutive clip, with the `0` timestamp corresponding to the first sample in the clip.
  - `ECG_Record`: The raw ECG signal in the MIMIC/VitalDB dataset with non-normalized absolute amplitudes
  - `PPG_Record`: The raw PPG signal in the MIMIC/VitalDB dataset with non-normalized absolute amplitudes
  - `ECG_Record_F`: The filtered ECG signal with non-normalized absolute amplitudes
  - `PPG_Record_F`:  The filtered PPG signal with non-normalized absolute amplitudes
- For fields that are present in both `v2_0` and `v1_0`, their equivalence were checked:
  - Data in the following fields in `v2_0` are equal to `v1_0` within a tolerance of 1e-6:
    - `ECG_F`, `PPG_F`, `ABP_F`, `PPG_ABP_Corr`
  - Data in all other fields in `v2_0` are identical to data in `v1_0`.
- All other scripts and files such as the **Info** files or the script **Generate_Subsets.m** are identical to `v1_0`. Therefore, running the script **Generate_Subsets.m** still retrieves the normalized signals from the previous fields, `ECG_F` and `PPG_F` (corresponding to the paper). If you want to retrieve the new non-normalized signals instead, modify the script to read from the newly added fields.

# The PulseDB Dataset

Please refer to the paper for detailed information about this dataset:

**PulseDB: A large, cleaned dataset based on MIMIC-III and VitalDB for benchmarking cuff-less blood pressure estimation methods**

**Frontiers in Digital Health, 08 February 2023**
**Volume 4 - 2022 | [https://doi.org/10.3389/fdgth.2022.1090854](https://doi.org/10.3389/fdgth.2022.1090854)**

For additional information about the fields in PulseDB files, refer to the [Supplementary Material](https://github.com/pulselabteam/PulseDB/blob/main/Supplementary%20Materials.pdf) of the paper. 
___

The script, **Generate_Subsets.m**, is provided to generate **Subset** files, which are the training, calibration, and testing subsets of the PulseDB Dataset. 

**Subset** files are generated from the **Segment** and **Info** files stored in the folder **Segment_Files**, **Info_Files**, and **Supplementary_Info_Files**, whose contents have to be downloaded separately from online drive services.

The generated **Subset** files are stored in the folder **Subset_Files** and **Supplementary_Subset_Files**. Data were organized as large matrices for the compactness of file size that is more suitable to fit into memory for training and testing machine learning models.

Please refer to the **File_Preparation_Guide** in each folder, or find all **Segment** and **Info** files you need all at once in organized folders from [Box link](https://rutgers.box.com/s/sw3c51fr5oybz6mhqsphh5zg8ibxw800), [GoogleDrive link](https://drive.google.com/drive/folders/10mz4mfBo6NczPNbbjX0a9tAKQSMugBjV?usp=sharing) or [OneDrive link](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/EqalUqc2s_dEqbhgugkUW1MBeNQIUEntgsGM67atFfivbg?e=csitkl)

The generated **Supplementary Subset** files with data derived from the **VitalDB** dataset are also available via [Kaggle](https://doi.org/10.34740/KAGGLE/DS/2447469).

# Download PulseDB v2_0

## From Box

- The [Box link](https://rutgers.box.com/s/sw3c51fr5oybz6mhqsphh5zg8ibxw800) stores files under the folder `Segment_Files` as sub-section compressed parts, other files as uncompressed, individual MATLAB data files
- Use the following curl script to download all parts under the  `Segment_Files` folder
  - If some file are not downloaded completely, try running the entire script again. The `curl -C` option will skip completed files and try resuming breakpoints of incomplete files and continue the download

```bash
curl -L -o "PulseDB_MIMIC.zip.001" -C - "https://rutgers.box.com/shared/static/7l8n3tn9tr0602tdss1x7e3uliahlibp.001"
curl -L -o "PulseDB_MIMIC.zip.002" -C - "https://rutgers.box.com/shared/static/zco48rvz5dog72970679foen6hct15c8.002"
curl -L -o "PulseDB_MIMIC.zip.003" -C - "https://rutgers.box.com/shared/static/x22qpmelx6sz3wgkm5qyc0eis429361f.003"
curl -L -o "PulseDB_MIMIC.zip.004" -C - "https://rutgers.box.com/shared/static/xj25sqnluiz6s4z8tzzm5phk00ohp6e8.004"
curl -L -o "PulseDB_MIMIC.zip.005" -C - "https://rutgers.box.com/shared/static/dxus2lsoop02chaspnwipwrf0g4wmenr.005"
curl -L -o "PulseDB_MIMIC.zip.006" -C - "https://rutgers.box.com/shared/static/rts6sj441laenm2sy1qcemg7ke4om3j6.006"
curl -L -o "PulseDB_MIMIC.zip.007" -C - "https://rutgers.box.com/shared/static/vor4hjllld7a0c3nzef8uptbb4ut3koo.007"
curl -L -o "PulseDB_MIMIC.zip.008" -C - "https://rutgers.box.com/shared/static/a2qg2p4ebyrooji3z88djlokji65tlf3.008"
curl -L -o "PulseDB_MIMIC.zip.009" -C - "https://rutgers.box.com/shared/static/uh6kbiuqgnib5wakiv6o35gkpusyamc7.009"
curl -L -o "PulseDB_MIMIC.zip.010" -C - "https://rutgers.box.com/shared/static/h6eyhkkx48pf3ce3th1clwj43hn98j5c.010"
curl -L -o "PulseDB_MIMIC.zip.011" -C - "https://rutgers.box.com/shared/static/e93dp94hxpkas45yc59n289s2wvkafgi.011"
curl -L -o "PulseDB_MIMIC.zip.012" -C - "https://rutgers.box.com/shared/static/iuvyuw7dmlxvbjvt53dj49wqn3gelqni.012"
curl -L -o "PulseDB_MIMIC.zip.013" -C - "https://rutgers.box.com/shared/static/qxx6tjz8c3778601ib3icu6o1rranmc7.013"
curl -L -o "PulseDB_MIMIC.zip.014" -C - "https://rutgers.box.com/shared/static/ip2ninwqj8437l9fyffjprnk90ptnx9k.014"
curl -L -o "PulseDB_MIMIC.zip.015" -C - "https://rutgers.box.com/shared/static/yrtbo0lg8mjhaw624iw9bbhk1obbocwd.015"
curl -L -o "PulseDB_MIMIC.zip.016" -C - "https://rutgers.box.com/shared/static/wmzndowgfa5xi3tvtqahxkld3ngdyjds.016"
curl -L -o "PulseDB_Vital.zip.001" -C - "https://rutgers.box.com/shared/static/vtxoksmn7emeaxypb2prywgwscuefoqa.001"
curl -L -o "PulseDB_Vital.zip.002" -C - "https://rutgers.box.com/shared/static/euzkek7c3xoy62jisheuxqar7z5y8xig.002"
curl -L -o "PulseDB_Vital.zip.003" -C - "https://rutgers.box.com/shared/static/49lngo0benxfjw193jnqz9tctlyb3qam.003"
curl -L -o "PulseDB_Vital.zip.004" -C - "https://rutgers.box.com/shared/static/jf4fwgkmhry20mf5tcg9t0wxvky64um0.004"
curl -L -o "PulseDB_Vital.zip.005" -C - "https://rutgers.box.com/shared/static/2lgxysbskfuapsaan4jypvmm8316fdkc.005"
curl -L -o "PulseDB_Vital.zip.006" -C - "https://rutgers.box.com/shared/static/x27ktb4qsx43razwo4tjmxq9v1ro0x3y.006"
curl -L -o "PulseDB_Vital.zip.007" -C - "https://rutgers.box.com/shared/static/q0t36fikgf3pimhvnerwwnovfr0umtp8.007"
curl -L -o "PulseDB_Vital.zip.008" -C - "https://rutgers.box.com/shared/static/ihckx2g0f981g5yz2x8v5rgwndl6yebw.008"
curl -L -o "PulseDB_Vital.zip.009" -C - "https://rutgers.box.com/shared/static/y8j14h8tvi5b3du8nap9dnura1omfrk6.009"
curl -L -o "PulseDB_Vital.zip.010" -C - "https://rutgers.box.com/shared/static/fu0m9tx33jkxywq32shh0g8dg3not15u.010"
```

- Use the following sha1 file checksum to check the integrity of downloaded parts

```yaml
PulseDB_MIMIC.zip.001: f3adc384962136eb93d5e12c73d1e2c742387df3
PulseDB_MIMIC.zip.002: b8db02f3e490c94e8b8b1e5c50bd127c0c340a65
PulseDB_MIMIC.zip.003: b32a27d7be4c8919b72a85b0bdafd716b0243f14
PulseDB_MIMIC.zip.004: 8e97e3811c42c6d5311d2a5151652be2b5b087d7
PulseDB_MIMIC.zip.005: 947ac26f686f3068cb726b3d158fb3469c203f68
PulseDB_MIMIC.zip.006: 8b6ab2773a3c7135d8cd71c9c33d7a480a1531e5
PulseDB_MIMIC.zip.007: 1648b9c50cf4b4949582955fa517c0a036982e03
PulseDB_MIMIC.zip.008: 4c9534c904d71cefafc6e8892d0eaeb6f6990113
PulseDB_MIMIC.zip.009: b7ad32b67abebec81861253ee1e1efac66a9527f
PulseDB_MIMIC.zip.010: 29fcc37cd04a9d099cb3a7566b07a3175b36e87f
PulseDB_MIMIC.zip.011: 70e585b97f2dc72130ea1c34ff0ba936a86e8e2c
PulseDB_MIMIC.zip.012: 5e4f38cc64cdb7938b144664f4863086bdf547f8
PulseDB_MIMIC.zip.013: 6acc91136ac53e232b4c83a6b3363b3077af2407
PulseDB_MIMIC.zip.014: 67b20543d8240ba6db7cf696638edf21c76ab26e
PulseDB_MIMIC.zip.015: 7e3edd06e61365b481233c60890309b43d57be29
PulseDB_MIMIC.zip.016: 837559cc18349e610d7950394e11be2d86d559c3
PulseDB_Vital.zip.001: 3e25f5f89e77b5619f911376f714facd1d14b95e
PulseDB_Vital.zip.002: 1ba93c9c4f1189f940be89db513b306ddbe93ffa
PulseDB_Vital.zip.003: 612ab2056288183bb2bba9724d6a66c18b15e71c
PulseDB_Vital.zip.004: f10ee6fe9f36b292ed5b313e6ea57357aa596c76
PulseDB_Vital.zip.005: 9a7c332ae6954a0e613b38b3ee522ab109e84736
PulseDB_Vital.zip.006: 8d7104a83e797d5c7026b0b1492d0f91fda6b426
PulseDB_Vital.zip.007: d60553c8cb46657f00f37c31494c5cde4b170a2b
PulseDB_Vital.zip.008: a64d6c051fe3f2bc0f6b438d6b9bcad7150e9c6f
PulseDB_Vital.zip.009: d98fb31b44364875c379fa82293ca14845b9f1c2
PulseDB_Vital.zip.010: 45c8a5bd810b1b5e70a63c3b9300490737fcabf4
```

- Unzip `PulseDB_MIMIC.zip.001` and `PulseDB_Vital.zip.001` with [7zip](https://www.7-zip.org/) to retrieve the `PulseDB_MIMIC` and `PulseDB_Vital` folders in the `Segment_Files` folder

## From GoogleDrive

- The [GoogleDrive link](https://drive.google.com/drive/folders/10mz4mfBo6NczPNbbjX0a9tAKQSMugBjV?usp=sharing) stores all files as uncompressed, individual MATLAB data files

- The Google Drive desktop app has option to sync all files in the link to a local machine
  - Register a free Google Drive account
  - Open the  in your web browser
  - In Google Drive, go to "Shared with me"
  - Right click on the PulseDB folder, select "Organize > Add shortcut"
  - Pick a location in you Google Drive to create a link to the shared folder
  - Install the Google Drive app on your computer and sync with your Google Drive account. PulseDB will be synced to your computer just like all other files in your Google Drive.

## From OneDrive

- The [OneDrive link](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/EqalUqc2s_dEqbhgugkUW1MBeNQIUEntgsGM67atFfivbg?e=csitkl) stores all files as uncompressed, individual MATLAB data files
- Use OneDrive as a backup to lookup individual file in case you encounter corrupted files


# Loading Subset Files in Python
Here is an example for loading the **Subset** files generated using the script **Generate_Subsets.m** in Python:
```python
#You need to install the package mat73 because PulseDB uses MAT file version 7.3 to store large volume data
from mat73 import loadmat 
import numpy as np

def Build_Dataset(Path,FieldName='Subset'):
        Data=loadmat(Path)
        # Access 10-s segments of ECG, PPG and ABP signals
        Signals=Data[FieldName]['Signals']
        # Access SBP labels of each 10-s segment
        SBPLabels=Data[FieldName]['SBP']
        # Access Age of the subject corresponding to each of the 10-s segment
        Age=Data[FieldName]['Age']
        # Access Gender of the subject corresponding to each of the 10-s segment
        Gender=np.array(Data[FieldName]['Gender']).squeeze()
        # Convert Gender to numerical 0-1 labels
        Gender=(Gender=='M').astype(float)
        # Access Height and Weight of the subject corresponding to each of the 10-s segment
        # If the subject is from the MIMIC-III matched subset, height and weight will be NaN 
        # since they were only recorded in VitalDB
        Height=Data[FieldName]['Height']
        Weight=Data[FieldName]['Weight']
        # Concatenate the demographic information as one matrix
        Demographics=np.stack((Age,Gender,Height,Weight),axis=1)
        return Signals,SBPLabels,Demographics
        
Build_Dataset('PulseDB\\Subset_Files\\Train_Subset.mat')
```

# Training the Models

To reproduce the gap between the calibration-free and calibration-based testing sets when training the model, use the code provided in **PulseDB/Model_Training**.

The code uses **TensorBoard** to record the results shown in the paper. In **PulseDB/Model_Training/TensorBoard**, results from previous runs described in the paper are included:

- **2022_0725_170136(SBP)** when training a SBP estimation model
- **2022_0726_221554(DBP)** when training a DBP estimation model

You can check these results with **TensorBoard**.

To run your own training, the following lines in **PulseDB/Model_Training/Model_Training.py** need to be modified per your setting:

```python
# Replace 'YOUR_PATH' with the folder of your generated Training, CalBased and CalFree testing subsets.
data_folder = 'YOUR_PATH'
Train_File = data_folder+'Train_Subset.mat'
Test_CalBased_File = data_folder+'CalBased_Test_Subset.mat'
Test_CalFree_File = data_folder+'CalFree_Test_Subset.mat'


# Training model for estimating SBP. Replace 'SBP' with 'DBP' to train model for DBP.
Train_Data = Build_Dataset(Train_File, 'SBP')
Test_CalBased_Data = Build_Dataset(Test_CalBased_File, 'SBP')
Test_CalFree_Data = Build_Dataset(Test_CalFree_File, 'SBP')
```

Once you are finished with these settings, run **Model_Training.py** to start model training. The results will be recorded in **PulseDB/Model_Training/TensorBoard**, just as the provided results. 

# Licenses

All files under the folder **PulseDB_MIMIC**, are data derived from the **MIMIC-III Waveform Database Matched Subset**: https://physionet.org/content/mimic3wdb-matched/1.0/

These files are made available under the Open Database License (ODbL): [http://opendatacommons.org/licenses/odbl/1.0/](https://opendatacommons.org/licenses/odbl/1.0/). Any rights in individual contents of the database are licensed under the Database Contents License: [http://opendatacommons.org/licenses/dbcl/1.0/](https://opendatacommons.org/licenses/dbcl/1.0/)

Refer to  [LICENSE_PulseDB_MIMIC](LICENSE_PulseDB_MIMIC) for details.

____

All files under the folder **PulseDB_Vital**, are data derived from the **VitalDB** dataset: https://vitaldb.net/dataset/

These files are made available under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License: https://creativecommons.org/licenses/by-nc-sa/4.0/ 

Refer to  [LICENSE_PulseDB_Vital](LICENSE_PulseDB_Vital) for details.

____

PulseDB_Info.mat, Train_Info.mat, CalBased_Test_Info.mat, CalFree_Test_Info.mat, AAMI_Test_Info.mat, AAMI_Cal_Info.mat, VitalDB_Train_Info.mat, VitalDB_CalBased_Test_Info.mat, VitalDB_CalFree_Test_Info.mat, VitalDB_AAMI_Test_Info.mat, VitalDB_AAMI_Cal_Info.mat, and Generate_Subsets.m, are information regarding to generation of the **Training, Calibration, and Testing Subsets of PulseDB**

These files are made available under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License: https://creativecommons.org/licenses/by-nc-sa/4.0/ 

Refer to  [LICENSE_PulseDB_Info](LICENSE_PulseDB_Info) for details.
