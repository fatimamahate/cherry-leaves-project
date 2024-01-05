import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random
# Visualization page with average image and standard deviation from outputs
def leaf_visualizer_page_body():
    st.title("Leaves Visualizer")

    st.write(
        "Business Requirement 1: The client is interested in having a study to"
        " visually differentiate between healthy and diseased leaves."
    )

    img_path="outputs/v1"

    st.header("Dimensions")

    if st.button("Dimensions Plot"):
        dimensions = plt.imread(f"{img_path}/dimensions.png")
    
    st.header("Mean Image and Variability")
    if st.button("Healthy Leaf"):
        avg_healthy = plt.imread(f"{img_path}/avg_var_healthy.png")
        st.success("The green part for the average image shows the leaf."
        " The lighter purple on the variability image shows the highest"
        " variance. The centre is the most similar.")
        
    if st.button("Powdery Leaf")
        avg_powdery = plt.imread(f"{img_path}/avg_var_powdery_mildew.png")
        st.warning("The average image shows the leaves. There is high variance"
        " most of the plot is the lighter purple. This means that there is"
        " more likely to be different pixels due to the powdery mildew." )
    
    if st.button("Differences"):
        diff = plt.imread(f"{img_path}/avg_diff.png")
        st.info("It is not entirely clear but there is some difference between"
        " each plot. The powdery mildew plot is a little lighter than healthy"
        " plot. This is due to the mildew.")
    
    st.header(Montage)
    st.info("Click on Montage to see images")

    data_dir = "inputs/cherry_leaves_dataset/cherry-leaves"
    labels=os.listdir(data_dir + "/val")
    curr_label = st.selectbox(label="Label", options=labels, index=0)

    if st.button("Montage"):
        img_montage(dir_path=data_dir + "/val",
        label = label,
        nrows=5,
        ncols=3)
    

def img_montage(dir_path, display_label,nrows,ncols,figsize(15,10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)
    if display_label in labels:
        img_list = os.listdir(dir_path + '/' + label)
        if nrows*ncols<len(img_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease dimensions to create your montage. \n"
                f"There are {len(images_list)} in your image set. "
                f"You want a montage with {nrows * ncols} images")
            return
    
    row_list=range(0,nrows)
    col_list=range(0,ncols)
    plot_idx = list(itertools.product(row_list,col_list))

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    for y in range(0, nrows * ncols):
        file = imread(dir_path + "/" + display_label + "/" + image_idx[y])
        img_shape = img.shape
        axes[ax_indices[y][0], ax_indices[y][1]].set_title(f"Height: {img_shape[0]}px Width: {img_shape[1]}px")
        axes[ax_indices[y][0], ax_indices[y][1]].imshow(file)
        # x axis
        axes[ax_indices[y][0], ax_indices[y][1]].set_xticks([])
        # y axis
        axes[ax_indices[y][0], ax_indices[y][1]].set_yticks([])
    plt.tight_layout()
    st.pyplot(fig=fig)

    else:
        print(f"The label you want doesn't exist. Choose from {labels}")



    
