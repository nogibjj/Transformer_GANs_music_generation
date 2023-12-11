import os
import pandas as pd


# Specify the directory path where the MIDI files are located
train_directory = 'Dataset/midis_emopia/train'
test_directory = 'Dataset/midis_emopia/test'

# Get a list of all the MIDI files in the directory
train_midi_files = os.listdir(train_directory)
test_midi_files = os.listdir(test_directory)

# Create an empty list to store the y values
y_train = []
y_test = []

# Iterate over each MIDI filename
for filename in train_midi_files:
    # Get the emotion label from the filename for the first 2 characters
    label = filename[:2]
    # Append the label to the y_train list
    y_train.append(label)

    # save it into csv file and add it to the dataset
    df = pd.DataFrame(y_train)
    df.to_csv('y_train.csv', index=False, header=False)
   
for filename in test_midi_files:
    # Get the emotion label from the filename for the first 2 characters
    label = filename[:2]
    # Append the label to the y_train list
    y_test.append(label)

    # save it into csv file and add it to the dataset
    df = pd.DataFrame(y_test)
    df.to_csv('y_test.csv', index=False, header=False)

