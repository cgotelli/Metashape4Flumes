# Metashape for Flumes

**MetashapeForFlumes** is a code made for processing several sets of images of laboratory flumes and making a reconstruction of their topography using [Metashape Professional Python 3 Module](https://www.agisoft.com/features/professional-edition/). The code helps automatize the serial process of different scans of the same experimental setup. The idea is to set all the parameters for the experiments once (markers and local coordinate system) and apply that same configuration for different scans of the flume bed, storing the outputs in different folders.

This code is an adaptation of the [ucdavis/metashape](https://github.com/ucdavis/metashape) repository.

## File structure of the code 

The entire process works with 3 main folders: **CODE** (where the code is stored), **RAW** (where the photos and other necessary files are stored), and **PROCESSED** (where the project files and chosen outputs are saved). Below is the file tree showing the general file structure:

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
│	    	run.py*
│
├───PROCESSED**
│   ├───output**
│   └───project_files**
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

## Setup

**Python:** You need Python (3.5, 3.6, 3.7 or 3.8[^1]). [Anaconda distribution](https://www.anaconda.com/distribution/) is recommended because it includes all the required libraries. When installing, if asked whether the installer should initialize Anaconda3, say "yes". Anaconda must be initialized upon install such that `python` can be called from the command line. A way to check is to simply enter `python` at your command prompt (CMD) and see if the resulting header info includes Anaconda and Python 3. If it doesn't, you may still need to initialize your Conda install.

**Metashape:** You must install the Metashape Python 3 module (Metashape version 1.8.1). Download the [current \*.whl file](https://www.agisoft.com/downloads/installer/) and install it following [these instructions](https://agisoft.freshdesk.com/support/solutions/articles/31000148930-how-to-install-metashape-stand-alone-python-module) (using the name of the .whl file that you downloaded).

**MATLAB[^2]:** Any basic version of Matlab is useful. No extra toolboxes are required.

## Usage

### Step 1. Build

This step uses Matlab[^2] to get the required files and copy them into their correspondent folders. It also creates the `run.py` script, which will allow to process all the scans in different folders/projects.


#### GCPs and coordinate system

#### Outer boundary

### Step 2. Run

This step uses Python through the Anaconda Powershell Prompt in Windows. For MAC and Linux you can use your terminal directly.

#### License 

Before running the code, it is necessary to have a copy of your Metashape License file in the same path where you will run the code. For that, copy the file **license.lic** from *C:\Program Files\Agisoft\Metashape Pro* to the folder **CODE/step02**. You can do it directly by running the code `python metashape_license_setup.py` at the command prompt.

### Step 3. Analyze output


[^1]: Up to now it doesn't work with Python 3.9. 
[^2]: Future versions will work using only Python at command prompt.
