import streamlit as st
#this will have the contents of the hypothesis
def hypothesis_page_body():
    st.title('Hypothesis and Validation')
    st.markdown("1. Healthy leaves do not have any specks on them"
    " therefore they can be detected by the lack of specks.")
    st.success("The average and standard deviation plot shows this. The 
    " powdery_leaves will have specks on them whereas hhe healthy leaves do not. ")
    st.markdown("2. The model can be trained to a high degree of 95%")
    st.success("Train the model (Convolutional Neural Network(CNN))."
    " The loss and accuracy plots are plotted to show if there is any under"
    " or overfitting. The model is successful as it has a high degree of"
    " accuracy (<99%). The loss and accuracy plots show a normal fit.")
