# Metashape for Flumes

**MetashapeForFlumes** is a code made for processing several sets of images of laboratory flumes and making a reconstruction of their topography using [Metashape Professional Python 3 Module](https://www.agisoft.com/features/professional-edition/). The code helps automatize the serial processing of different scans of the same experimental setup when you want to compare the variation in time of DEMs and/or Orthophotos.

To automatize the process it is necessary to first have one test scan running properly with Metashape and getting the results in the best possible way. Once you have the final values for the parameters, and the coordinates of your markers in the local coordinate system of the flume, you can start thinking about applying that configuration to all your future scans. By doing this, you assure that you will have comparable results, all made with the same parameters. Also, you will not have to be thinking about the computer all the time as now it runs independently.

This code is based on the work done by [this group](https://github.com/ucdavis/metashape). This code is adapted for being used in experimental flumes with fixed and known marker positions. For other uses please refer to the original repository.

## Folders structure 

The entire process works with 3 subfolders inside one main folder: **CODE** (where this code is stored), **RAW** (where the photos and other necessary files should be placed), and **PROCESSED** (where the project files and outputs are saved). Below is the file tree showing the general folders and files structure:

```
EXPERIMENT001
├───CODE
│   ├───step01
│   │       build.py
│   │       s01_functions.py
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
	|	photo001.jpg
	|	photo002.jpg
	|	...
        ├───scan02
	|	photo001.jpg
	|	photo002.jpg
	|	...
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

**Environment:** All the necessary packages can be installed with the file `metashape.yml`. For doing it we should execute in your terminal (UNIX OS) or Anaconda Command Prompt (Windows) the following command:

```
conda env create -f metashape.yml 
```

The only package that must be installed manually is Metashape API. 

**Metashape:** You must install the Metashape Professional Edition and Metashape Python 3 module (version 1.8.1). Download the [current \*.whl file](https://www.agisoft.com/downloads/installer/) and install it following [these instructions](https://agisoft.freshdesk.com/support/solutions/articles/31000148930-how-to-install-metashape-stand-alone-python-module) (using the name of the .whl file that you downloaded). **It can be used with the trial version of one month.**

## Usage  
The process consists of two main steps: preparing the data, and processing it. The postprocess is done with other codes, depending of what you want to analyze (see the [TTGA repository](https://github.com/cgotelli/DEM-ttga) for graph-theory analysis or [DEM-Iber](https://github.com/cgotelli/DEM-Iber/) to prepare the DEMs to simulate the flow with [Iber](https://iberaula.es/)). 

The first of the two steps gets the required files and copy them into their correspondent subfolders inside the **RAW** folder. It also creates the `run.py` script, which will run the Metashape Python package over each subfolder containing the photos of the different scans. Below there is an explanation of both steps.

### Step 1. Build  
In the main folder (EXPERIMENT001 in the file tree above) you will have two folders:  
1. You will copy the **CODE** folder from this repository in that path, and
2. You will make another folder named **RAW**. Inside it you will create:
	1. **photos**: Inside this folder you will put the pictures to process divided in subfolders: one for each scan.
	2. **config_common**: This folder contains the files to use for configuring the Markers and coordinate system, and the outer boundary to have a regular shape as output for DEMs and Orthophotos (this makes comparison between files easier).

#### What should be inside the **RAW** folder?

1. **Markers and coordinate system**  
Markers are a feature included in Metashape (Tools > Markers) that allows to include Ground Control Points that are recognizable for the software. We can assign coordinates to markers and use them to give dimensions to the model. The autodetection of these markers is included in the process and requires only an exported CSV file generated by you in Metashape. This file must be put in the folder **config_common** with the name **referenceMarkers.txt** and exported with comma (,) as separator.  
The markers should be enumerated in order, following the longitudinal axis. First, the right side of the flume from target 01 to target (N), and then the left side from targe (N+1) to target (end). This would allow using markers as polygon shape for exporting DEMs and Orthophotos.

2. **Outer boundary**  
The outerBoundary files is a set of 4 files that are used by Metashape to define the zone of the model to be included in the DEM and/or Ortophoto. The easiest way of getting this region is by doing it in Metashape. It is necessary to create the region `Ortho > Create Polygon` and then go to `File > Export > Shapes`. After exporting you will have the 4 files ready to put inside the **RAW** folder.

3. **baseConfig.yml file**  
This file is the base configuration for all the projects. It includes all the parameters set by the user that will be equal for processing every scan, and it is modified for each project including the specific path for the photo subfolders. The details of how it works and what does mean each parameter are included inside the file as comments. 


### Step 2. Run

This step uses Python through the Anaconda Powershell Prompt (Windows) or the terminal (UNIX). It is necessary to set the directory of the terminal/console in folder `EXPERIMENT001 > CODE > step02` and execute the following command: `python run.py`. 
> :warning: Remember to set as conda working environment the one where you have installed the Meashape API.

#### License 

Before running the code, it is necessary to have a copy of your Metashape License file in the same path where you will run the code. For that, copy the file **license.lic** from `C:\Program Files\Agisoft\Metashape Pro` to the folder **CODE/step02**. You can do it directly by running the code `python metashape_license_setup.py` at the command prompt. If you're using the trial license **license_trial.lic**, you have to either edit the function ```metashape_license_setup.py``` or copy the license file manually to folder **CODE/step02** and rename it as **license.lic**.



[^1]: Up to now (August, 2022) it doesn't work with Python 3.9. 
