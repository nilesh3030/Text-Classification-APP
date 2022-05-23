from termcolor import colored
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import tensorflow.keras.models
import numpy as np


def classifier(news_text):

    model = tensorflow.keras.models.load_model('lstm_model.hdf5')

    # loading
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    maxlen = 177

    #News Labels
    labels = ['World News', 'Sports News', 'Business News', 'Science-Technology News']

    test_seq = pad_sequences(tokenizer.texts_to_sequences(news_text), maxlen=maxlen)

    test_preds = [labels[np.argmax(i)] for i in model.predict(test_seq)]

    for news, label in zip(news_text, test_preds):
        # print('{} - {}'.format(news, label))
        output = '{} - {}'.format(colored(news, 'yellow'), colored(label, 'blue'))

    return(label)

