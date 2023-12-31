# -*- coding: utf-8 -*-
"""Final_Exam Group 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13xyLEWneU_ifod8EvOnwP6W_R1S24lo8

Group 2 Final Exam <br>


Submitted By: <br>
Cantarona Zyrelle Jane, Canete John Carlo <br>
Capena Symon Renzo, Ching Kyle Jarick <br>
Conde Jethro Hans <br>

Submitted to: <br>
ENGR. Jonathan Taylar
"""

!pip install kaleido
!pip install cohere
!pip install tiktoken
!pip install spacy==3.6.0
!pip install tensorflow-probability<4.6.0
!pip install -r requirements.txt --use-deprecated=legacy-resolver

!pip install gradio

from google.colab import drive
drive.mount('/content/drive')

import gradio as gr

import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.models import load_model

data = '/content/drive/MyDrive/CPE 019 Final Exam/Fallimages'


img_size = (224, 224)
batch_size = 32

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_generator = datagen.flow_from_directory(data, target_size=img_size, batch_size=batch_size, subset='training')
val_generator = datagen.flow_from_directory(data, target_size=img_size, batch_size=batch_size, subset='validation')

lb = LabelBinarizer()
lb.fit(train_generator.classes)
num_classes = train_generator.num_classes

img_size = (224, 224)
batch_size = 32

datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    vertical_flip=True)
train_generator = datagen.flow_from_directory(
    data,
    target_size=img_size,
    batch_size=batch_size,
    subset='training')
val_generator = datagen.flow_from_directory(
    data,
    target_size=img_size,
    batch_size=batch_size,
    subset='validation')

num_epochs = 50

learning_rate = 0.01

model = Sequential()
model.add(Flatten(input_shape=train_generator.image_shape))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.8))
model.add(Dense(num_classes, activation='softmax'))

optimizer = Adam(lr=learning_rate)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

model_path = '/content/drive/MyDrive/CPE 019 Final Exam/Copy of best_model.h5'

checkpoint = ModelCheckpoint(model_path, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')

history = model.fit(train_generator, epochs=num_epochs, validation_data=val_generator, callbacks=[checkpoint])

model = load_model(model_path)

data = '/content/drive/MyDrive/CPE 019 Final Exam/fall_dataset'


img_size = (224, 224)
batch_size = 32

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_generator = datagen.flow_from_directory(data, target_size=img_size, batch_size=batch_size, subset='training')
val_generator = datagen.flow_from_directory(data, target_size=img_size, batch_size=batch_size, subset='validation')

lb = LabelBinarizer()
lb.fit(train_generator.classes)
num_classes = train_generator.num_classes

img = Image.open('/content/drive/MyDrive/CPE 019 Final Exam/Fallimages/normal/2018-07-04T12_04_18.513441.png').resize((224, 224))

x = np.array(img) / 255.0
x = np.expand_dims(x, axis=0)

predictions = model.predict(x)

class_names = ['Normal', 'Fall Warning', 'Fall']
predicted_class = class_names[np.argmax(predictions)]
probability = np.max(predictions)
print(f'Predicted class: {predicted_class}')
print(f'Probability: {probability}')

plt.imshow(img)
plt.show()

img = Image.open('/content/drive/MyDrive/CPE 019 Final Exam/Fallimages/normal/fall196.jpg').resize((224, 224))

x = np.array(img) / 255.0
x = np.expand_dims(x, axis=0)

predictions = model.predict(x)

class_names = ['Normal', 'Fall Warning', 'Fall']
predicted_class = class_names[np.argmax(predictions)]
probability = np.max(predictions)
print(f'Predicted class: {predicted_class}')
print(f'Probability: {probability}')

plt.imshow(img)
plt.show()

img = Image.open('/content/drive/MyDrive/CPE 019 Final Exam/Fallimages/normal/fall153.jpg').resize((224, 224))

x = np.array(img) / 255.0
x = np.expand_dims(x, axis=0)

predictions = model.predict(x)

class_names = ['Normal', 'Fall Warning', 'Fall']
predicted_class = class_names[np.argmax(predictions)]
probability = np.max(predictions)
print(f'Predicted class: {predicted_class}')
print(f'Probability: {probability}')

plt.imshow(img)
plt.show()

img = Image.open('/content/drive/MyDrive/CPE 019 Final Exam/Fallimages/normal/fall185.jpg').resize((224, 224))

x = np.array(img) / 255.0
x = np.expand_dims(x, axis=0)

predictions = model.predict(x)

class_names = ['Normal', 'Fall Warning', 'Fall']
predicted_class = class_names[np.argmax(predictions)]
probability = np.max(predictions)
print(f'Predicted class: {predicted_class}')
print(f'Probability: {probability}')

plt.imshow(img)
plt.show()

img = Image.open('/content/drive/MyDrive/CPE 019 Final Exam/Fallimages/normal/not fallen001.jpg').resize((224, 224))

x = np.array(img) / 255.0
x = np.expand_dims(x, axis=0)

predictions = model.predict(x)

class_names = ['Normal', 'Fall Warning', 'Fall']
predicted_class = class_names[np.argmax(predictions)]
probability = np.max(predictions)
print(f'Predicted class: {predicted_class}')
print(f'Probability: {probability}')

plt.imshow(img)
plt.show()

img = Image.open('/content/drive/MyDrive/CPE 019 Final Exam/Fallimages/normal/fall199.jpg').resize((224, 224))

x = np.array(img) / 255.0
x = np.expand_dims(x, axis=0)

predictions = model.predict(x)

class_names = ['Normal', 'Fall Warning', 'Fall']
predicted_class = class_names[np.argmax(predictions)]
probability = np.max(predictions)
print(f'Predicted class: {predicted_class}')
print(f'Probability: {probability}')

plt.imshow(img)
plt.show()