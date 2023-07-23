import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizer import Adam

def Training_bot(x,y):
    model = Sequential()
    model.add(Dense(128,input_shape = (len(x[0]))))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation = "relu")
    model.add(Dropout(0.5))
    model.add(Dense(32, activation = "relu")
    model.add(Dropout(0.5))
    model.add(Dense(16, activation = "relu")
    model.add(Dropout(0.5))
    model.compile(optimizer = "adam", loss = "catagorical_crossentrpy", matrix = "accuracy")
    history = model.fit(x,y,epoches = 20, verbose = True)
    model.save("bot.h5",history)