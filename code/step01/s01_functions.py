#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 17:08:38 2022

@author: cgotelli
"""


def writeRunFile(fid, workflowPath, configPath):
    """
    WRITERUNFILE writes the file for running Metashape on all the scans inside 
    Parameters
    ----------
    fid : TYPE
        DESCRIPTION.
    workflow : TYPE
        DESCRIPTION.
    workflowPyPath : TYPE
        DESCRIPTION.
    configPath : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    from os.path import join

    fileout = join(workflowPath, "run.py")
    workflowPyPath = join(workflowPath, "workflow.py")
    if fid == 0:
        print("hola")
        outfid = open(fileout, "w")
        outfid.write("import os" + "\n")
        outfid.write(
            (
                "os.system('python"
                + " "
                + join(workflowPyPath)
                + " "
                + join(configPath)
                + "'"
                + ")"
                + "\n"
            )
        )
        outfid.close()
    else:
        outfid = open(fileout, "a")
        outfid.write(
            (
                "os.system('python"
                + " "
                + join(workflowPyPath)
                + " "
                + join(configPath)
                + "'"
                + ")"
                + "\n"
            )
        )


def writeConfig(filein, fileout, subfolder, photoPath, outputPath, projectPath):
    """
    WRITECONFIG writes configuration file for each scan.
    This function takes the path of the base configuration file and then adds the specific
    parameters of each subfolder (corresponding to single scans).

    Parameters
    ----------
    filein : STRING
        DESCRIPTION.
    fileout : STRING
        DESCRIPTION.
    subfolder : STRING
        DESCRIPTION.
    photoPath : STRING
        DESCRIPTION.
    outputPath : STRING
        DESCRIPTION.
    projectPath : STRING
        DESCRIPTION.

    Returns
    -------
    None.

    """

    from os.path import join

    outfid = open(fileout, "wt")

    outfid.write(
        ("main_path: " + '"' + join(photoPath) + '"' + "\n")
    )  # the text you are adding at the beginning
    outfid.write(
        ("subFolder: " + '"' + subfolder + '"' + "\n")
    )  # the text you are adding at the beginning\
    outfid.write(
        ("output_path: " + '"' + join(outputPath) + '"' + "\n")
    )  # the text you are adding at the beginning\
    outfid.write(
        ("project_path: " + '"' + join(projectPath) + '"' + "\n")
    )  # the text you are adding at the beginning\
    outfid.close()

    with open(filein) as f:
        lines = f.readlines()
        with open(fileout, "a") as f1:
            f1.writelines(lines)
