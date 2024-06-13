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

Please refer to the **File_Preparation_Guide** in each folder, or find all **Segment** and **Info** files you need all at once in organized folders from [Box link](https://rutgers.box.com/s/1ko8x0emqjyyxc4l5ekboe3qq6qihdzk), [GoogleDrive link](https://drive.google.com/drive/folders/1behw-Dljs8-p2axHQ6KJZ5HTRKQHQgnS?usp=sharing) or [OneDrive link](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/ElnVrq7MWdVGvvZztLCuNe0BDJ1YKh9FNBM0tK2BJVC0ew?e=fQYySg) 

The generated **Supplementary Subset** files with data derived from the **VitalDB** dataset are also available via [Kaggle](https://doi.org/10.34740/KAGGLE/DS/2447469).

# Download PulseDB

## From Box

- The [Box link](https://rutgers.box.com/s/1ko8x0emqjyyxc4l5ekboe3qq6qihdzk) stores files under the folder `Segment_Files` as sub-section compressed parts, other files as uncompressed, individual MATLAB data files. 
- Use the following curl script to download all parts under the `Segment_Files` folder
  - If some file are not downloaded completely, try running the entire script again. The `curl -C` option will skip completed files and try resuming breakpoints of incomplete files and continue the download

```bash
curl -L -o "PulseDB_MIMIC.zip.001" -C - "https://rutgers.box.com/shared/static/53kfmkx15l62yu3rs1sxzvze2tzewutk.001"
curl -L -o "PulseDB_MIMIC.zip.002" -C - "https://rutgers.box.com/shared/static/785nurn76omwdwjnu003a8ska26obwe7.002"
curl -L -o "PulseDB_MIMIC.zip.003" -C - "https://rutgers.box.com/shared/static/5fvkx289q9khyetk36ow1jb10ek03n3j.003"
curl -L -o "PulseDB_MIMIC.zip.004" -C - "https://rutgers.box.com/shared/static/ulw32hprx591773fookhiwxjhgmy6wpx.004"
curl -L -o "PulseDB_MIMIC.zip.005" -C - "https://rutgers.box.com/shared/static/r1oaquc9802u9mgn5sysf179g8ww5jiu.005"
curl -L -o "PulseDB_MIMIC.zip.006" -C - "https://rutgers.box.com/shared/static/65zvh30kwwxlth3zq6rd9rkuil2w9rbt.006"
curl -L -o "PulseDB_MIMIC.zip.007" -C - "https://rutgers.box.com/shared/static/wtf7bpi0zdepraryylsc53673j4dq2eq.007"
curl -L -o "PulseDB_MIMIC.zip.008" -C - "https://rutgers.box.com/shared/static/tzp1b1cdobyp65vv0shaquw6kd0pd07g.008"
curl -L -o "PulseDB_MIMIC.zip.009" -C - "https://rutgers.box.com/shared/static/3iezt1ddlx7cbwgp4ithb5tr6p39jezx.009"
curl -L -o "PulseDB_MIMIC.zip.010" -C - "https://rutgers.box.com/shared/static/ib5cqx3m36mhel4gnz7vpvj1nw1wak5b.010"
curl -L -o "PulseDB_Vital.zip.001" -C - "https://rutgers.box.com/shared/static/6wr84abvfig13vsx4bvh6xh3urrozdpf.001"
curl -L -o "PulseDB_Vital.zip.002" -C - "https://rutgers.box.com/shared/static/u3arkvy1nauuppk62nxlksri6mdsmjk1.002"
curl -L -o "PulseDB_Vital.zip.003" -C - "https://rutgers.box.com/shared/static/lkinin92f1je8ktd9odfvtlwe02sdu33.003"
curl -L -o "PulseDB_Vital.zip.004" -C - "https://rutgers.box.com/shared/static/sd2u917eeliaougx7ljiwivjhp8c18vs.004"
curl -L -o "PulseDB_Vital.zip.005" -C - "https://rutgers.box.com/shared/static/bq7zf0yv7bt9vqjn80xdfnhdcmjau0ja.005"
curl -L -o "PulseDB_Vital.zip.006" -C - "https://rutgers.box.com/shared/static/q5uihdc7swwygzq0mou4xwodwqybzudg.006"
```

- Use the following sha1 file checksum to check the integrity of downloaded parts

```yaml
PulseDB_MIMIC.zip.001: 237c686b97580311a9a825c222427345f9463ede
PulseDB_MIMIC.zip.002: 012b01b8a05fed43faf6bcdb546b5d046d8ab6e0
PulseDB_MIMIC.zip.003: ae8d44914b55fdf9c2a3e4d72e8d0d28f603fa33
PulseDB_MIMIC.zip.004: 9db2ed484d061ae85f5219446cb2b11c5af7a816
PulseDB_MIMIC.zip.005: df20fa9e31eae4bb65debe69ac7861ddc2917c6a
PulseDB_MIMIC.zip.006: c0fa0cd2a085d1705a927147c3cc26bfc5a57803
PulseDB_MIMIC.zip.007: fcafb78e7aa2b4cffa67be8dd2ed5f6cf1bb23fc
PulseDB_MIMIC.zip.008: 4ae881e1c21cf81ef624904762042d90c199fe23
PulseDB_MIMIC.zip.009: 5141ba351ca43254a65a5c002c0364299885aab5
PulseDB_MIMIC.zip.010: 0ba3404842611e367d9bfda2519187ea02fd622c
PulseDB_Vital.zip.001: 58024e3a7ea817bd22a667a6acd680054af29f0e
PulseDB_Vital.zip.002: 0ba2752b3260569b7852f3ffb304dae232771a89
PulseDB_Vital.zip.003: 372edb13319a8ded48fce164e1653344341fb399
PulseDB_Vital.zip.004: 0ae48a57106dcf2f7e21eb193a4c843ef07c7596
PulseDB_Vital.zip.005: f0e31bc208c6cc80ad816bce1b5088e1f90fa2f7
PulseDB_Vital.zip.006: 04c385b55c9355f0cc7e2a984d3fa8c25559785b
```

- Unzip `PulseDB_MIMIC.zip.001` and `PulseDB_Vital.zip.001` with [7zip](https://www.7-zip.org/) to retrieve the `PulseDB_MIMIC` and `PulseDB_Vital` folders in the `Segment_Files` folder

## From GoogleDrive or OneDrive

- The [OneDrive link](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/ElnVrq7MWdVGvvZztLCuNe0BDJ1YKh9FNBM0tK2BJVC0ew?e=fQYySg) and [GoogleDrive link](https://drive.google.com/drive/folders/1behw-Dljs8-p2axHQ6KJZ5HTRKQHQgnS?usp=sharing) stores files under the folder `Segment_Files` as sub-section compressed parts as well as individual zip files. Other files are stored as uncompressed, individual MATLAB data files

- Tips for downloading data files:

  - Avoid selecting multiple files in the online drive and download together, or creating multiple downloads at the same time. Downloading each of the file one at a time is the fastest and easiest way to have all files properly downloaded.

  - If you can successfully download **PulseDB/Segment_Files/PulseDB_MIMIC.zip** and **PulseDB/Segment_Files/PulseDB_Vital.zip**, then there is no need to download any file in the folder **PulseDB/Segment_Files/Segment_Files_Subsection_Compressed**

  - Both OneDrive and GoogleDrive do not support resume downloading from break-point. Therefore, if the download pause or fail, you need to start all over again. This may create difficulties when downloading the largest data files, **PulseDB_MIMIC.zip** (136GB) and **PulseDB_Vital.zip** (77.4GB), in wirelessly connected circumstances that are prone to be interrupted. To resolve this problem, we have created sub-section compressed version of these two files, with each section being 10GB (except for the last section). If you have encountered problems or failures when downloading the .zip files, try the sub-section compressed version: **PulseDB_MIMIC_Parts** (14 Parts) ([OneDrive](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/Evexk1L7supLvnNOejVYJa0BJxOJmJNeKKgaL-h5_vrndw?e=bnkwWT)  [GoogleDrive](https://drive.google.com/drive/folders/1PEACOKTyrfBT9NUOypwwyITGgub7uWT0?usp=sharing)) and **PulseDB_Vital_Parts** (8 Parts) ([OneDrive](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/EuHxwv0ogdhGhKiABDvfEIcB_lolC0ufIZ2wWFY9MvvSEg?e=HCkRMH) [GoogleDrive](https://drive.google.com/drive/folders/1TUjAIORpytNc5LBShUOnTcGkHUlbSzeX?usp=sharing)) in the folder **PulseDB/Segment_Files/Segment_Files_Subsection_Compressed**, and download the data files section-by-section. After downloading all sections, unzip any one of the sections to get the desired data folder. 

  - No matter which version (the .zip or the sub-section compressed version) you have donwloaded, remember to unzip the files and put the data folders, **PulseDB_MIMIC** and **PulseDB_Vital**, into the **Segment_Files** folder, before you start generating the **Subset** files using the provided script.

  - If your unarchive software does not support subsection-compressed files or encounter other problems, we suggest using the open-source software [7Zip](https://www.7-zip.org/) for Windows, and the free software [The Unarchiver](https://theunarchiver.com/) for Mac.

  - If there is an error when unarchiving the subsection-compressed files, then some of your sections may not have been downloaded completely. Check for downloaded sections that are smaller than 10GB, and re-download them.

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


# Updates

- **Update_2023_03_02** 

  - We uploaded all **5,361** uncompressed segment files in **PulseDB_MIMIC.zip** and **PulseDB_Vital.zip** to [OneDrive](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/EhJfGb93KONPg0oXN7ISKLkBXqKvOJ-8VdEvux3Bny22TA?e=pG3ynR) and [GoogleDrive](https://drive.google.com/drive/folders/1uC5eaUbuOUqZooeJE0vLwLYZ9kEXjhCO?usp=sharing), so you can also search and download each file individually.
  - If you encountered difficulties when downloading files with web browser, use the above GoogleDrive links to create a shortcut or make a copy of PulseDB to you own GoogleDrive repository, then, sync your local hard drive with your GoogleDrive repository using the desktop GoogleDrive APP.



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
