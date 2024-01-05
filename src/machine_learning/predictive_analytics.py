import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file

#Plot the prediction probability values
def plot_pred_prob(pred_prob,pred_class):
    prob_per_class = pd.DataFrame(
        data=[0,0],
        index={'healthy':0, 'powdery_mildew':1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class]=pred_prob
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_prob
        prob_per_class=prob_per_class.round(3)
        prob_per_class['Healthy/Powdery_mildew']=prob_per_class.index

        fig = px.bar(
            prob_per_class,
            x='Label',
            y=prob_per_class['Probability'],
            range_y=[0,1],
            width=600, height=400, template='seaborn'
        )
        st.plotly_chart(fig)

def resize_in_img(img,ver):
    img_shape = load_pkl_file(file_path=f"outputs/{ver}/img_shape.pkl")
    img_resize=img.resize((img_shape[1], img_shape[0]), Image.ANTIALIAS)
    my_img = np.expand_dims(img_resized, axis=0)/255
    return my_img

#load the model and make prediction of the image
def pred_img(my_img,ver):
    model=load_model(f"outputs/{ver}/mildew_detector_model.h5")
    pred_prob=model.predict(my_img)[0,0]
    target_map={v: k for k, v in {'healthy':0,'powdery_mildew':1}.items()}
    pred_class=target_map[pred_prob>0.5]
    if pred_class == target_map[0]:
        pred_prob = 1 - pred_prob
    
    st.write(
        f"The predictive analysis shows the leag is "
        f"**{pred_class.lower()}**"
    )

    return pred_prob, pred_class
