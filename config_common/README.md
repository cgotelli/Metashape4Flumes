# Configuration files example

Depending on the alternative steps we want to include, we need to put up to three files inside the RAW folder:

1. **baseConfig.yml**: This file contains the part of the configuration file that is common for all the projects to process. The most important parameters to set are:

	-	*run_name*: The identifier for the run. Will be used in naming output files. Recommended to include a photoset name and processing parameter set name.

	- *project_crs*: Coordinate system projection code. In the case of flumes, should be a local coordinated system. The code for that option is: 

	*'LOCAL_CS["Local Coordinates (m)",LOCAL_DATUM["Local Datum",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]]]'*

	- Definition of the steps to include in the process. You can deactivate some of them if you want to include only some steps in the general process. Inside each step, there is a keyword which you have to set on True or False, depending on if you want to include it or not.

2. 