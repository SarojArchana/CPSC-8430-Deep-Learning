# Video Caption Generation using Sequence-to-Sequence Model

This is a code repository for the Video Caption Generation using Sequence-to-Sequence Model. The repository contains three Python files:

- `models.py`: This file contains the implementation of the Sequence-to-Sequence Model for video caption generation.
- `train.py`: This file is used to train the model using video features and corresponding captions.
- `test.py`: This file is used to generate captions for new videos using the trained model.
- `run.sh`: shell script to run the model.


# Program Testing Instructions

## Description

 Please follow the steps carefully.

## Installation

First clone the repository to your local machine.


## Testing

To test the program, please follow these instructions carefully:

1. Add the test video features to a folder "testing_data"

2. Edit the `run.sh` shell script and replace `$path1` with the path to the `testing_data` folder, and `$path2` with the location where you want the output `.txt` file to be saved.

3. Download the model from the Google Drive link that I shared in the `modeldownload.txt` file located in the "Model" folder. Please note that you must also put the `picket_data.pickle` file in the same "Model" folder.

4. Run the shell script using the following command: `./run.sh`.

Please note the following carefully:

You need to change the `data_path`, `model_path`, `pickel_file`, and `test_json` variables in the `Train.py`, `Test.py`, and `model.py` code in order to run the code correctly. I am taking absolute paths to avoid confusion.


## Folder Structure

- `Model`: This folder contains the pre-trained model.
## Author

The code is written by Archana Saroj.
