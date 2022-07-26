# Licenses

PulseDB_MIMIC.zip, PulseDB_MIMIC.zip.001, PulseDB_MIMIC.zip.002, PulseDB_MIMIC.zip.003, PulseDB_MIMIC.zip.004 , PulseDB_MIMIC.zip.005, PulseDB_MIMIC.zip.006, PulseDB_MIMIC.zip.007, PulseDB_MIMIC.zip.008, PulseDB_MIMIC.zip.009, PulseDB_MIMIC.zip.010, PulseDB_MIMIC.zip.011, PulseDB_MIMIC.zip.012, PulseDB_MIMIC.zip.013, and PulseDB_MIMIC.zip.014, are data derived from the **MIMIC-III Waveform Database Matched Subset**: https://physionet.org/content/mimic3wdb-matched/1.0/

These files are made available under the Open Database License (ODbL): [http://opendatacommons.org/licenses/odbl/1.0/](https://opendatacommons.org/licenses/odbl/1.0/). Any rights in individual contents of the database are licensed under the Database Contents License: [http://opendatacommons.org/licenses/dbcl/1.0/](https://opendatacommons.org/licenses/dbcl/1.0/)

Refer to  [LICENSE_PulseDB_MIMIC](LICENSE_PulseDB_MIMIC) for details.



PulseDB_Vital.zip, PulseDB_Vital.zip.001, PulseDB_Vital.zip.002, PulseDB_Vital.zip.003, PulseDB_Vital.zip.004, PulseDB_Vital.zip.005, PulseDB_Vital.zip.006, PulseDB_Vital.zip.007, and PulseDB_Vital.zip.008, are data derived from the **VitalDB** dataset: https://vitaldb.net/dataset/

These files are made available under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License: https://creativecommons.org/licenses/by-nc-sa/4.0/ 

Refer to  [LICENSE_PulseDB_Vital](LICENSE_PulseDB_Vital) for details.



PulseDB_Info.mat, Train_Info.mat, CalBased_Test_Info.mat, CalFree_Test_Info.mat, AAMI_Test_Info.mat, AAMI_Cal_Info.mat, VitalDB_Train_Info.mat, VitalDB_CalBased_Test_Info.mat, VitalDB_CalFree_Test_Info.mat, VitalDB_AAMI_Test_Info.mat, VitalDB_AAMI_Cal_Info.mat, and Generate_Subsets.m, are information regarding to generation of the **Training, Calibration, and Testing Subsets of PulseDB**

These files are made available under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License: https://creativecommons.org/licenses/by-nc-sa/4.0/ 

Refer to  [LICENSE_PulseDB_Info](LICENSE_PulseDB_Info) for details.

# The PulseDB Dataset

The script, **Generate_Subsets.m**, is provided to generate **Subset** files, which are the training, calibration, and testing subsets of the PulseDB Dataset. 

**Subset** files are generated from the **Segment** and **Info** files stored in the folder **Segment_Files**, **Info_Files**, and **Supplementary_Info_Files**, whose contents have to be downloaded separately from online drive services.

The generated **Subset** files are stored in the folder **Subset_Files** and **Supplementary_Subset_Files**. Data were organized as large matrices for the compactness of file size that is more suitable to fit into memory for training and testing machine learning models.

Please refer to the **File_Preparation_Guide** in each folder, or find all **Segment** and **Info** files you need all at once in organized folders from this [OneDrive link](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/ElnVrq7MWdVGvvZztLCuNe0BDJ1YKh9FNBM0tK2BJVC0ew?e=fQYySg) or [GoogleDrive link](https://drive.google.com/drive/folders/1behw-Dljs8-p2axHQ6KJZ5HTRKQHQgnS?usp=sharing)

The generated **Supplementary Subset** files are also available via [Kaggle](https://doi.org/10.34740/KAGGLE/DS/2447469).

Tips for downloading data files:
- In our tests, the OneDrive links have shown better stability when downloading large files.
- Avoid selecting multiple files in the online drive and download together, or creating multiple downloads at the same time. Downloading each of the file one at a time is the fastest and easiest way to have all files properly downloaded.
- If you can successfully download **PulseDB/Segment_Files/PulseDB_MIMIC.zip** and **PulseDB/Segment_Files/PulseDB_Vital.zip**, then there is no need to download any file in the folder **PulseDB/Segment_Files/Segment_Files_Subsection_Compressed**
- Both OneDrive and GoogleDrive do not support resume downloading from break-point. Therefore, if the download pause or fail, you need to start all over again. This may create difficulties when downloading the largest data files, **PulseDB_MIMIC.zip** (136GB) and **PulseDB_Vital.zip** (77.4GB), in wirelessly connected circumstances that are prone to be interrupted. To resolve this problem, we have created sub-section compressed version of these two files, with each section being 10GB (except for the last section). If you have encountered problems or failures when downloading the .zip files, try the sub-section compressed version: **PulseDB_MIMIC_Parts** (14 Parts) ([OneDrive](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/Evexk1L7supLvnNOejVYJa0BJxOJmJNeKKgaL-h5_vrndw?e=bnkwWT)  [GoogleDrive](https://drive.google.com/drive/folders/1PEACOKTyrfBT9NUOypwwyITGgub7uWT0?usp=sharing)) and **PulseDB_Vital_Parts** (8 Parts) ([OneDrive](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/EuHxwv0ogdhGhKiABDvfEIcB_lolC0ufIZ2wWFY9MvvSEg?e=HCkRMH) [GoogleDrive](https://drive.google.com/drive/folders/1TUjAIORpytNc5LBShUOnTcGkHUlbSzeX?usp=sharing)) in the folder **PulseDB/Segment_Files/Segment_Files_Subsection_Compressed**, and download the data files section-by-section. After downloading all sections, unzip any one of the sections to get the desired data folder. 
- No matter which version (the .zip or the sub-section compressed version) you have donwloaded, remember to unzip the files and put the data folders, **PulseDB_MIMIC** and **PulseDB_Vital**, into the **Segment_Files** folder, before you start generating the **Subset** files using the provided script.
- If your unarchive software does not support subsection-compressed files or encounter other problems, we suggest using the open-source software [7Zip](https://www.7-zip.org/) for Windows, and the free software [The Unarchiver](https://theunarchiver.com/) for Mac.
- If there is an error when unarchiving the subsection-compressed files, then some of your sections may not have been downloaded completely. Check for downloaded sections that are smaller than 10GB, and re-download them.
