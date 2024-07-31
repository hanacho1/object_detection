## Object Detection(small object)
This project is an example of training and evaluating deep learning models for small object detection.

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Training](#training)
4. [Testing](#testing)

## Overview
This project involves the following key steps:
1. Prepareing custom dataset: Converting label files in JSON format to TXT format from images stored in Google Drive.
[Download the dataset from Google Drive]([https://drive.google.com/uc?id=FILE_ID&export=download](https://drive.google.com/drive/folders/1XANY18zT8qBWTSP8uH8tW5PPtoHU-CEH?usp=drive_link](https://drive.google.com/drive/folders/1XANY18zT8qBWTSP8uH8tW5PPtoHU-CEH?usp=drive_link))
2. Training a deep learning model using the converted data.
3. Detecting small objects in test images using the trained model.

## Installation
This section describes the steps to set up the necessary packages and environment.
1. Create a new conda environment.
```bash
conda create --name yolov9 python=3.8
```
2. Activate yolov9
```bash
conda activate yolov9
```
3. Install requirements
```bash
pip install -r requirements.txt
```

## Training
Before starting the training process, data preparation and conversion are necessary.

Convert the JSON files stored in Google Drive to TXT format using the "update_and_convert_labels.py" script.
```bash
python update_and_convert_labels.py --json-folder /path/to/json/folder --txt-folder /path/to/txt/folder --image-folder /path/to/image/folder

```bash
python train.py --batch 32 --epochs 100 --device=0 --img 320 --min-items 0 --close-mosaic 20 --data /workspace/yolov9/customYolo9.yaml --weights /workspace/yolov9/weights/gelan-e.pt --cfg models/detect/gelan-e.yaml --hyp /workspace/yolov9/data/hyps/hyp.scratch-high.yaml
```

## Testing
```bash
python detect.py --source '/workspace/testimg/1517699_597.jpg' --img 640 --device 0 --weights '/workspace/runs/train/exp22/weights/best_striped.pt' --name exp22_test --conf-thres 0.5
```
