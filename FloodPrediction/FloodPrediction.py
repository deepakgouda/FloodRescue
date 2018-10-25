#!/usr/bin/env python
# coding: utf-8

# In[133]:


import numpy as np
import math
import matplotlib.pyplot as plt
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.callbacks import TensorBoard
from time import time


# In[134]:


# %matplotlib gtk


# In[135]:


def create_dataset(dataset, look_back = 1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), :]
        dataX.append(a)
        dataY.append(dataset[i + look_back, :])
    return np.array(dataX), np.array(dataY)


# In[136]:


dataframe = read_csv('flood_train.csv', skipinitialspace = True, squeeze = True)
print(dataframe.head())


# In[137]:


dataframe.shape


# In[138]:


data = np.array(dataframe)
data = data[:, 1]


# In[139]:


plt.plot(data)
plt.show()


# In[140]:


data = data.reshape((data.shape[0], 1))
data.shape


# In[141]:


data = data.astype('float64')

scaler = MinMaxScaler(feature_range=(0, 1))
data = scaler.fit_transform(data)
print(data[:5])


# In[142]:


split = 0.67
train_size = int(len(data)*split)
test_size = len(data)-train_size
train = data[0:train_size,:]
test = data[train_size:len(data),:]
print(train.shape)
print(test.shape)


# In[143]:


look_back = 3
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
print(trainX.shape)
# print(trainY[:5])


# In[144]:


# trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
# testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))


# In[145]:


units = 100
drop = 0.2
epoch = 10

model = Sequential()
model.add(LSTM(units, input_shape=(look_back, 1)))
# model.add(Dropout(drop))
model.add(Dense(1))
# model.compile(loss='mean_squared_error', optimizer='adam')
model.compile(loss='mean_squared_error', optimizer='nadam')
# model.summary()
tensorboard = TensorBoard(log_dir="logs/{}".format(time()))
model.fit(trainX, trainY, epochs=epoch, batch_size=1, verbose=1, callbacks=[tensorboard])


# In[151]:


trainPredict = model.predict(trainX)
testPredict = model.predict(testX)


# In[152]:


testPredict.shape


# In[153]:


trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform(trainY)
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform(testY)


# In[154]:


trainScore = math.sqrt(mean_squared_error(trainY, trainPredict))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY, testPredict))
print('Test Score: %.2f RMSE' % (testScore))


# In[155]:


trainPredictPlot = np.empty_like(data)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict

testPredictPlot = np.empty_like(data)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(data)-1, :] = testPredict


# In[122]:


# print(data.shape)
# print(train.shape)
# print(test.shape)
# print(trainPredict.shape)
# print(testPredict.shape)


# In[156]:


# col = 0
# plt.plot(scaler.inverse_transform(data)[:,col])
# plt.plot(trainPredictPlot[:,col])
# plt.plot(testPredictPlot[:,col])

plt.plot(scaler.inverse_transform(data))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.title('Units = %d Dropout = %.2f Epoch = %d Split = %d%% Train = %.2f Test = %.2f' % 
          (units, drop, epoch, split*100, trainScore, testScore))
plt.show()


# In[ ]:




