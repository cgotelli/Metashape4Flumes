# -*- coding: utf-8 -*-
# File for running a metashape workflow

# Derek Young and Alex Mandel
# University of California, Davis
# 2021

import sys
import telegram # Install using the following command: pip install python-telegram-bot

## Load custom modules and config file: slightly different depending whether running interactively or via command line
try:        # running interactively (in linux) or command line (windows)
    from python import workflow_functions as meta
    from python import read_yaml
except:     # running from command line (in linux) or interactively (windows)
    import workflow_functions as meta
    import read_yaml

api_key = 'API KEY'
user_id = 'YOUR USER ID'
bot = telegram.Bot(token=api_key)


config_file = sys.argv[1]

## Parse the config file
cfg = read_yaml.read_yaml(config_file)

### Run the Metashape workflow

doc, log, run_id = meta.project_setup(cfg)

meta.enable_and_log_gpu(log)

if cfg["load_project"] == "":  # only add photos if this is a brand new project, not based off an existing project
    meta.add_photos(doc, cfg)

if cfg["alignPhotos"]["enabled"]:
    meta.align_photos(doc, log, cfg)
    meta.reset_region(doc)

if cfg["optimizeCameras"]["enabled"]:
    meta.optimize_cameras(doc, cfg)
    meta.reset_region(doc)

if cfg["buildDenseCloud"]["enabled"]:
    meta.build_dense_cloud(doc, log, run_id, cfg)

if cfg["importMarkers"]["enabled"]:
    print('Entered')
    meta.importReference(doc, cfg)
    
if cfg["buildDem"]["clip_to_boundary"]:
    meta.SetBoundary(doc, cfg)

if cfg["buildDem"]["enabled"]:
    meta.build_dem(doc, log, run_id, cfg)

if cfg["buildOrthomosaic"]["enabled"]:
    meta.build_orthomosaics(doc, log, run_id, cfg)

meta.export_report(doc, run_id, cfg)

meta.finish_run(log, config_file)

bot.send_message(chat_id=user_id, text='We just finished the run: '+ run_id)