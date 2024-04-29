# PulseDB v2_0

- We have updated PulseDB to `v2_0` in the `main` branch. To check the historical data and repository published along the paper, see branch `v1_0`.
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
- Data in `v2_0` is stored in [OneDrive](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/EqalUqc2s_dEqbhgugkUW1MBeNQIUEntgsGM67atFfivbg?e=csitkl) and [GoogleDrive](https://drive.google.com/drive/folders/10mz4mfBo6NczPNbbjX0a9tAKQSMugBjV?usp=sharing). To view previous links that point to the previous PulseDB data, see branch `v1_0`.

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

Please refer to the **File_Preparation_Guide** in each folder, or find all **Segment** and **Info** files you need all at once in organized folders from this [OneDrive link](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/EqalUqc2s_dEqbhgugkUW1MBeNQIUEntgsGM67atFfivbg?e=csitkl) or [GoogleDrive link](https://drive.google.com/drive/folders/10mz4mfBo6NczPNbbjX0a9tAKQSMugBjV?usp=sharing)

The generated **Supplementary Subset** files with data derived from the **VitalDB** dataset are also available via [Kaggle](https://doi.org/10.34740/KAGGLE/DS/2447469).

# Download PulseDB v2_0

- `v2_0` is stored as uncompressed, individual MATLAB data files.
- At present, we recommend using the Google Drive app to download the shared files
  - Register a free Google Drive account
  - Open the [GoogleDrive link](https://drive.google.com/drive/folders/10mz4mfBo6NczPNbbjX0a9tAKQSMugBjV?usp=sharing) in your web browser
  - In Google Drive, go to "Shared with me"
  - Right click on the PulseDB folder, select "Organize > Add shortcut"
  - Pick a location in you Google Drive to create a link to the shared folder
  - Install the Google Drive app on your computer and sync with your Google Drive account. PulseDB will be synced to your computer just like all other files in your Google Drive.


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
