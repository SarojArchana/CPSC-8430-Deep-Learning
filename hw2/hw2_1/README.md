# Video Caption Generation using Sequence-to-Sequence Model

This is a code repository for the Video Caption Generation using Sequence-to-Sequence Model. The repository contains three Python files:

- `models.py`: This file contains the implementation of the Sequence-to-Sequence Model for video caption generation.
- `train.py`: This file is used to train the model using video features and corresponding captions.
- `test.py`: This file is used to generate captions for new videos using the trained model.
- `run.sh`: shell script to run the model.

## Testing the Program


To test the program, please follow these steps:

1. Add the test video features adhering to the following folder structure: `testing_data/feat`
2. Add the testing labels in JSON format at `testing_data/` with the name `testing_label.json`.
3. Edit the shell script `hw2_seq2seq.sh` and replace the `$1` with `testing_data` and `$2` with the output `.txt` file location.
4. Run the shell script using the following command: `./hw2_seq2seq.sh`

## Folder Structure

- `Model`: This folder contains the pre-trained model.
- `MLDS_hw2_1_data`: This folder contains necessary data.

## Author

The code is written by Archana Saroj.
