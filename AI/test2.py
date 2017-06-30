import os
import urllib.request
from PIL import Image

import numpy as np
from numpy import * 

import matplotlib
from matplotlib.pyplot import imshow

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

path1="C:/Users/cpereyda18/Desktop/data/Images"    #path of folder of images    
path2='C:/Users/cpereyda18/Desktop/data/Scaled'  #path of folder to save images   
imlist = os.listdir(path2)


#Get image data
tmp = []
for im2 in imlist:
	tmpIm = load_image('Scaled'+ '/' + im2)
	tmp.append(tmpIm)
	
imageData = np.array(tmp)
	
print(imageData.shape)
X = imageData

my_data = genfromtxt('turn2.csv', delimiter=',')
Y = my_data.astype(dtype=np.float64)


print(Y.shape)

print('X.shape: ', X.shape)
print('Y.shape: ', Y.shape)
imshow(X[0])


import numpy as np
#shuffle  both X and Y the same way
def unison_shuffled_copies(X, Y):
    assert len(X) == len(Y)
    p = np.random.permutation(len(X))
    return X[p], Y[p]

shuffled_X, shuffled_Y = unison_shuffled_copies(X,Y)

len(shuffled_X)

test_cutoff = int(len(X) * .8) # 80% of data used for training
val_cutoff = test_cutoff + int(len(X) * .1) # 10% of data used for validation and test data 

train_X, train_Y = shuffled_X[:test_cutoff], shuffled_Y[:test_cutoff]
val_X, val_Y = shuffled_X[test_cutoff:val_cutoff], shuffled_Y[test_cutoff:val_cutoff]
test_X, test_Y = shuffled_X[val_cutoff:], shuffled_Y[val_cutoff:]

len(train_X) + len(val_X) + len(test_X)


X_flipped = np.array([np.fliplr(i) for i in train_X])
Y_flipped = np.array([-i for i in train_Y])
train_X = np.concatenate([train_X, X_flipped])
train_Y = np.concatenate([train_Y, Y_flipped])
len(train_X)


from keras.models import Model, load_model
from keras.layers import Input, Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense


img_in = Input(shape=(200, 200, 3), name='img_in')
angle_in = Input(shape=(1,), name='angle_in')

x = Convolution2D(8, 3, 3)(img_in)
x = Activation('relu')(x)
x = MaxPooling2D(pool_size=(2, 2))(x)

x = Convolution2D(16, 3, 3)(x)
x = Activation('relu')(x)
x = MaxPooling2D(pool_size=(2, 2))(x)

x = Convolution2D(32, 3, 3)(x)
x = Activation('relu')(x)
x = MaxPooling2D(pool_size=(2, 2))(x)

merged = Flatten()(x)

x = Dense(8172)(x)
x = Activation('linear')(x)
x = Dropout(.2)(x)

x = Dense(4096)(x)
x = Activation('linear')(x)
x = Dropout(.2)(x)

x = Dense(2048)(x)
x = Activation('linear')(x)
x = Dropout(.2)(x)

x = Dense(1024)(x)
x = Activation('linear')(x)
x = Dropout(.2)(x)

x = Dense(512)(x)
x = Activation('linear')(x)
x = Dropout(.2)(x)

x = Dense(256)(merged)
x = Activation('linear')(x)
x = Dropout(.2)(x)
angle_out = Dense(1, name='angle_out')(x)

model = Model(input=[img_in], output=[angle_out])
model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

import os
from keras import callbacks

model_path = os.path.expanduser('~/best_autopilot.hdf5')

#Save the model after each epoch if the validation loss improved.
#save_best = callbacks.ModelCheckpoint(model_path, monitor='val_loss', verbose=1, 
#                                     save_best_only=True, mode='min')

#stop training if the validation loss doesn't improve for 5 consecutive epochs.
#early_stop = callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=5, 
#                                     verbose=0, mode='auto')

#callbacks_list = [save_best]

#model.fit(train_X, train_Y, batch_size=64, nb_epoch=20, validation_data=(val_X, val_Y), callbacks=callbacks_list)


results = model.predict(X)
for n in results:
	print(n)
