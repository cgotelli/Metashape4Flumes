#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 16:04:16 2022

@author: cgotelli

 This function prepares the photos for the Metashape automatized process.
 It changes the names to fit the ones established in the script.
 As in the flume we have 104 photos (52 from each camera). These photos
 are taken always in the same positions, so on each survey the markers
 appear in the same correlative position. The idea is to have the markers
 always in pictures with the same name. This way we don't have to change
 the main code for each survey. It's easier to change the names of the
 pictures each time with this script.

 The code works as follows:
 * In one folder we have to create one subfolder per survey. At the end of
 a day where we scanned 5 times the bed, we should have 5 subfolders
 inside the main directory.
 * Then, we run this script and we choose the path of the main folder.
 * The code will enter each subfolder, changing the names of all the
 pictures inside. If the photo-capturing process is correct, we should
 have the same amount of pictures inside each subfolder. At the same time,
 each photo with the same name should be a photo taken from the same spot.
 Thus, photos with the same name should show the same markers.

"""
import os
from os.path import join, exists, basename, abspath
from os import listdir, mkdir, rename, makedirs
import s01_functions as s01
import shutil
import ntpath

# -------------------- Parameters for processing ------------------------------

originalPath = os.getcwd()

# We specify the main path where folders with photos are stored (RAW/photos)
filesPath = "F:\GOTELLI\Metashape4Flumes\EXPERIMENT001\RAW\photos"  #'path/to/RAW/photos'
filesPath = abspath(filesPath)


# We specify the path where configuration files are stored (RAW/config_common)
configPath = "F:\GOTELLI\Metashape4Flumes\EXPERIMENT001\RAW\config_common"
configPath = abspath(configPath)

RunFilesPath = join(filesPath, "..", "runfiles")
outputPath = join(filesPath, "..", "..", "PROCESSED", "output")
projectPath = join(filesPath, "..", "..", "PROCESSED", "project_files")
workflowPath = join(filesPath, "..", "..", "CODE", "step02")

# creates folder for run files.
if not exists(RunFilesPath):
    mkdir(RunFilesPath)

# From the content inside the main folder we keep only the path of subfolders
dfolders = [f.path for f in os.scandir(filesPath) if f.is_dir()]


# ------------------------- Renaming process ----------------------------------

# For each subfolder we enter and change the name of the files inside
for fid in range(0, len(dfolders)):

    filenames = []

    print("Working on folder: " + os.path.basename(dfolders[fid]))
    os.chdir(dfolders[fid])

    # List of photos inside the subfolder. Sorted by name to process left side first.
    imageList = sorted(listdir(os.getcwd()))

    # We loop through files looking only for JPG images.
    for file in imageList:
        # check only text files
        if file.endswith(".JPG") or file.endswith(".jpg"):
            filenames.append(file)

    # We change the name of the JPG files, according to the camera of origin.
    for id in range(0, len(filenames)):

        f = filenames[id]
        subfolder = dfolders[fid]
        subfolderName = basename(subfolder)
        print("Original name: " + f)

        if f[0:3] == "LFT":

            label = "LFT_" + "{:03.0f}".format(id) + ".JPG"

            if f != label:
                print("New name: " + "LFT_" + "{:03.0f}".format(id) + ".JPG")

                rename(join(subfolder, f), join(subfolder, label))

            else:
                print("Did not modify the name")

        elif f[0:3] == "RGT":

            label = "RGT_" + "{:03.0f}".format(id) + ".JPG"

            if f != label:
                print("New name: " + "RGT_" + "{:03.0f}".format(id) + ".JPG")
                rename(join(subfolder, f), join(subfolder, label))

            else:
                print("Did not modify the name")

        else:

            print("This file was not processed.")

    # ----------------------- Moving files process --------------------------------

    #   Move all photos to the output folder
    subfolderName = basename(subfolder)
    imageList = sorted(listdir(os.getcwd()))
    destinationFolder = join(RunFilesPath, subfolderName, "100MEDIA")

    if not exists(destinationFolder):
        makedirs(destinationFolder)

    for file in imageList:
        if file.endswith(".JPG") or file.endswith(".jpg"):
            shutil.move(
                join(dfolders[fid], file), join(RunFilesPath, subfolderName, "100MEDIA", file)
            )

    # ----------------------- Create configuration file --------------------------------
    # Write configuration file

    s01.writeConfig(
        join(configPath, "baseConfig.yml"),
        join(RunFilesPath, subfolderName, ("config_" + subfolderName + ".yml")),
        subfolderName,
        RunFilesPath,
        outputPath,
        projectPath,
    )

    # ----------------------- Create run file --------------------------------

    s01.writeRunFile(
        fid,
        workflowPath,
        join(RunFilesPath, subfolderName, ("config_" + subfolderName + ".yml")),
    )

    # ----------------------- Copy other Metashape necessary files --------------------------------

    src_dir = join(configPath)
    dest_dir = join(RunFilesPath, subfolderName)

    files = os.listdir(src_dir)
     # iterating over all the files in
    # the source directory
    for fname in files:         
        # copying the files to the
        # destination directory
        shutil.copy2(os.path.join(src_dir,fname), dest_dir)

# ---------------------------- Final steps ------------------------------------
# We go back to the original folder of the code
os.chdir(originalPath)

# The end
print("All files are ready to run")
