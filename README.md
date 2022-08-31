# The PulseDB Dataset

The script, **Generate_Subsets.m**, is provided to generate **Subset** files, which are the training and testing subsets of the PulseDB Dataset. **Subset** files are generated from the **Segment** and **Info** files stored in the folder **Segment_Files** and **Info_Files**, whose contents have to be downloaded separately from online drive services.

The generated **Subset** files are stored in the folder **Subset_Files**. Data were organized as large matrices for the compactness of file size that is more suitable to fit into memory for training and testing machine learning models.

Please refer to the **File_Preparation_Guide** in each folder, or find all (248GB) MATLAB data files you need all at once in organized folders from this [OneDrive link](https://rutgersconnect-my.sharepoint.com/:f:/g/personal/ww329_soe_rutgers_edu/ElnVrq7MWdVGvvZztLCuNe0BDJ1YKh9FNBM0tK2BJVC0ew?e=fQYySg) or [Google Drive link](https://drive.google.com/drive/folders/1behw-Dljs8-p2axHQ6KJZ5HTRKQHQgnS?usp=sharing), including the already-generated **Subset** files. Remember to unzip the **PulseDB_MIMIC.zip** and **PulseDB_Vital.zip** files before you start if you want to generate the **Subset** files by yourself.

Here are some guides for downloading these data files
- In our tests, the OneDrive links have shown better stability for downloading the data files, so we recommend using them.
- We recommend downloading each of the file one at a time, instead of zipping multiple files in the online drive and download together
- Both OneDrive and GoogleDrive do not support resume downloading from break-point. Therefore, if the download pause or fail, you have to start all over again. This has create difficulties when downloading the largest data files: PulseDB_MIMIC.zip (136GB) and PulseDB_Vital.zip (77.4GB). To resolve that problem, we have created sub-section compressed version of these two files: . Each sub-section is of 10GB. After downloading all sections, unzip any one of the sections, and you get the desired data folder. If your unarchive software does not support subsection-compressed files, the open-source software [7Zip](https://www.7-zip.org/) might help.
