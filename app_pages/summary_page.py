import streamlit as st
import matplotlib.pyplot as plt

def summary_page_body():
    st.title("Project Summary")
    st.header("Introduction")
    st.info("Farmy & Foods have been struggling with the trying to keep their"
    " cherry trees healthy by preventing the spread of mildew. Therefore, they"
    " have decided on training a model using over 4000 images of healthy and"
    " diseased (containing mildew) leaves. They will be used to differentiate"
    " between the leaves. Currently, a sample must be taken and manually"
    " checked to see if the plant is diseased. This model would mean they could"
    " take a random sample and simply upload an image to detect whether it is"
    " healthy or powdery.")
    st.header("Business Requirements")
    st.success("1.The client is interested in having a study to visually"
    " differentiate between healthy and diseased leaves. \n 2.The client is"
    " interested in telling whether a specific leaf has mildew or not.")
    st.header("Extra Information")
    st.info("For extra information click below"
    " [README](https://github.com/fatimamahate/cherry-leaves-project)")
