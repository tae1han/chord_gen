# keras module for building LSTM
import tensorflow
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.preprocessing.text import Tokenizer
from keras.callbacks import EarlyStopping
from keras.models import Sequential
import keras.utils as ku


# set seeds for reproducability
#from tensorflow import set_random_seed
#from numpy.random import seed
#set_random_seed(2)
#seed(1)

import pandas as pd
import numpy as np
import string, os

import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)

from chordLSTM.py import model


def generate_text(seed_text, next_words, model, max_sequence_len):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict_classes(token_list, verbose=0)

        output_word = ""
        for word,index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " "+output_word
    return seed_text.title()

#test

print (generate_text('Bb^7', 4, model, max_sequence_len))
print (generate_text('D-9', 8, model, max_sequence_len))
print (generate_text('Eh7', 8, model, max_sequence_len))
print (generate_text('Eb^7', 16, model, max_sequence_len))
