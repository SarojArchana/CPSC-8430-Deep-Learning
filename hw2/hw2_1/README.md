README
Introduction
This is a video caption generation system, which generates a textual description of a given video. The code is written by Archana Saroj and is designed to train a model on a dataset and generate captions for a given video using the trained model.

Files
The code consists of the following files:

models.py: contains the code for the video caption generation model
train.py: used for training the model on the dataset
test.py: used to generate captions from the trained model
hw2_seq2seq.sh: shell script to run the test program
Testing
To test the program, please follow the steps below:

Add the testing video features to the "testing_data/feat" folder in the same format as the training features.
Add the testing captions in JSON format to the "testing_data/" folder with the name "testing_label.json".
Edit the hw2_seq2seq.sh shell script and replace the "$1" with "testing_data" and "$2" with the output .txt file location.
Run the hw2_seq2seq.sh script.
Pretrained Model and Data
The Model folder contains the pretrained model, and the MLDS_hw2_1_data folder contains the necessary data to run the program.

Conclusion
Thank you for using this video caption generation system. If you have any questions or issues, please contact the author, Archana Saroj.
