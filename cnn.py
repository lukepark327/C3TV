#-*- coding:utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.advanced_activations import LeakyReLU


leakyrelu = LeakyReLU(alpha=0.3)

def create_model(result_class_size, input_n, input_m):
    model = Sequential()

    model.add(Conv2D(32, (5, 5), input_shape=(input_n, input_m, 1), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Flatten())

    model.add(Dense(130, activation=leakyrelu))
    model.add(Dense(50, activation=leakyrelu))
    model.add(Dropout(0.3))
    model.add(Dense(result_class_size, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model
