import os
import random
import shutil

def train_test_split(src, train_size=0.8):
    # create train and test folder
    if not os.path.exists(os.path.join(src, 'train')):
        os.makedirs(os.path.join(src, 'train'))
    if not os.path.exists(os.path.join(src, 'test')):
        os.makedirs(os.path.join(src, 'test'))

    # split train and test
    for root, dirs, files in os.walk(src):
        for file in files:
            if random.random() < train_size:
                shutil.move(os.path.join(root, file), os.path.join(src, 'train'))
            else:
                shutil.move(os.path.join(root, file), os.path.join(src, 'test'))

if __name__ == '__main__':
    train_test_split('/workspaces/Transformer_GANs_music_generation/Dataset/midis_emopia')