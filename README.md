# DogCatClassifier

Dog and cat image classifier with deep learning.

Using Predict Command:

python predict.py <path to image>

..path to image means enter the image path you want to predict.


Train for your own dataset:

python train.py

 CUSTOM DATASET FOR CLASSIFICATION:

If you want to add new dataset to datasets, you create a directory and rename what you want to add category (like 'cat' or 'phone').

If you want to add a new training image to previously category datasets, you add a image to about category directory and if you have npy files in Data folder delete npy_train_data folder.
Program automatically converts image to 64x64.


Important Notes:

Used Python Version: 3.6 or greater
numpy
scikit-learn
scikit-image
tensorflow < =1.19
keras
h5py
