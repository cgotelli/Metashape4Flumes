# MetashapeForFlumes

**MetashapeForFlumes** is a set of codes made for automatize the serial . Currently, the files for running the Metashape projects are built with Matlab.  

This code is based on the [ucdavis/metashape](https://github.com/ucdavis/metashape) repository.

## File structure of the code 

The entire process works with 3 main folders: CODE, RAW, and PROCESSED. Below is the file tree with the required files:

```
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
│
├───PROCESSED*
│   ├───output*
│   └───project_files*
└───RAW
    ├───config_common
    │       baseConfig.yml
    │       outBoundary.shp
    │       referenceMarkers.txt
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


