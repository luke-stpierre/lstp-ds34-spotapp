import tensorflow as tf
from backapp.list_var import SONG_LIST, SONG_URI_KEY
import pandas as pd
import numpy as np

# Loading the pre-built model 
MODEL = tf.keras.models.load_model('/app/backapp/music_autoencoder')


def transform(data_dict):
    # Create empty dictionary
    query_df = pd.DataFrame(data=np.zeros((1,10000), dtype='int'), columns=SONG_LIST)
    temp_list = []
    for key, value in data_dict.items():
        temp_list.append(value)
        query_df[value]= query_df[value].replace([0],1)
    
    pred_array = MODEL.predict(query_df)
    test_pred_df = pd.DataFrame(data={'song':query_df.columns,'pred':pred_array[0]}).sort_values('pred', ascending=False).head(12)['song']
    # Convert the dictionary values to tensors
    input_dict = {}
    for i,item in enumerate(test_pred_df):
        if item not in temp_list:
            input_dict[f'song{i}'] = SONG_URI_KEY[item].split(':')[-1]

    return input_dict