# Metashape for Flumes

**MetashapeForFlumes** is a code made for processing several sets of images of laboratory flumes and making a reconstruction of their topography using [Metashape Professional Python 3 Module](https://www.agisoft.com/features/professional-edition/). The code helps automatize the serial processing of different scans of the same experimental setup when you want to compare the variation in time of DEMs and/or Orthophotos.

To automatize the process it is necessary to first have one test scan running properly with Metashape and getting the results in the best possible way. Once you have the final values for the parameters, and the coordinates of your markers in the local coordinate system of the flume, you can start thinking about applying that configuration to all your future scans. By doing this, you assure that you will have comparable results, all made with the same parameters. Also, you will not have to be thinking about the computer all the time as it runs now independently.

This code is adapted for being used in experimental flumes with fixed and known marker positions. For other uses please refer to the repository on which this code is based: the work done on [this repository](https://github.com/ucdavis/metashape).

## Folders structure 

The entire process works with 3 subfolders inside one main folder: **CODE** (where this code is stored), **RAW** (where the photos and other necessary files should be placed), and **PROCESSED** (where the project files and outputs are saved). Below is the file tree showing the general folders and files structure:

```
EXPERIMENT001
├───CODE
│   ├───step01
│   │       build.m
│   │       writeConfig.m
│   │       writeRunFile.m
│   │
│   └───step02
│           metashape_license_setup.py
│           metashape_workflow.py
│           metashape_workflow_functions.py
│           read_yaml.py
│           run.py*
│
├───PROCESSED**
│   ├───output**
│   └───project_files**
│
└───RAW
    ├───config_common
    │       baseConfig.yml
    │       referenceMarkers.txt
    │       outBoundary.shp
    │	    outBoundary.prj
    │       outBoundary.shx
    │       outBoundary.dbf
    │
    └───photos
        ├───scan01
		photo001.jpg
		photo002.jpg
		...
        ├───scan02
		photo001.jpg
		photo002.jpg
		...
        └───scan03
		photo001.jpg
		photo002.jpg
		...
	...
        
```

**\***: file `run.py` is created automatically in Step 01.  
**\*\***: These folders are created when running the script `run.py`.

## Setup

Before start, you have to install all the necessary software and packages:   

**Python:** You need Python (any version between 3.5 and 3.8[^1]). [Anaconda distribution](https://www.anaconda.com/distribution/) is recommended because it includes all the required libraries. When installing, if asked whether the installer should initialize Anaconda3, say "yes". Anaconda must be initialized upon install such that `python` can be called from the command line. A way to check is to simply enter `python` at your command prompt (CMD) and see if the resulting header info includes Anaconda and Python 3. If it doesn't, you may still need to initialize your Conda install.

**Metashape:** You must install the Metashape Professional Edition and Metashape Python 3 module (version 1.8.1). Download the [current \*.whl file](https://www.agisoft.com/downloads/installer/) and install it following [these instructions](https://agisoft.freshdesk.com/support/solutions/articles/31000148930-how-to-install-metashape-stand-alone-python-module) (using the name of the .whl file that you downloaded). It can be used with the trial version of one month.

**MATLAB[^2]:** Any basic version of Matlab is useful. No extra toolboxes are required.

## Usage  
The process consists of two main steps: preparing the data, and processing it. The first step uses Matlab[^2] to get the required files and copy them into their correspondent subfolders inside the **RAW** folder. It also creates the `run.py` script, which will run the Metashape Python package over each subfolder containing the photos of different scans.

### Step 1. Build  
In the main folder (EXPERIMENT001 in the file tree above) you will have two folders:  
1. You will copy the **CODE** folder from this repository.
2. You will make a folder named **RAW**. Inside it you will put:
	1. **photos**: Inside this folder you will put the pictures to process divided in subfolders: one for each scan.
	2. **config_common**: This folder contains the files to use for configuring the Markers and coordinate system, and the outer boundary to have a regular shape as output for DEMs and Orthophotos (this makes comparison between files easier).

#### Markers and coordinate system  
Markers are a feature included in Metashape (Tools > Markers) that allows to include Ground Control Points that are recognizable for the software. We can assign coordinates to markers and use them for give dimensions to the model. The autodetection of these markers is included in the process and requires only an exported CSV file generated by you in Metashape. This file must be put in the folder **config_common** with the name **referenceMarkers.txt** and exported with comma (,) as separator.  
The markers should be enumerated in order following the longitudinal axis. First, the right side of the flume from target 01 to target (N), and then the left side from targe (N+1) to target (end). This would allow using markers as polygon shape for exporting DEMs and Orthophotos.

#### Outer boundary

#### baseConfig.yml file  
This file is the base configuration for all the projects. It includes all the parameters set by the user that will be equal for processing every scan, and it is modified for each project including the specific path for the photo subfolders. The details of how it works and what does mean each parameter are included inside the file as comments. 


### Step 2. Run

This step uses Python through the Anaconda Powershell Prompt in Windows. For MAC and Linux you can use your terminal directly.

#### License 

Before running the code, it is necessary to have a copy of your Metashape License file in the same path where you will run the code. For that, copy the file **license.lic** from *C:\Program Files\Agisoft\Metashape Pro* to the folder **CODE/step02**. You can do it directly by running the code `python metashape_license_setup.py` at the command prompt. If you're using the trial license **license_trial.lic**, you have to either change edit the python function *metashape_license_setup.py* or copy the license file manually to folder **CODE/step02**.

### Step 3. Analyze output


[^1]: Up to now it doesn't work with Python 3.9. 
[^2]: Future versions will work using only Python at command prompt.
