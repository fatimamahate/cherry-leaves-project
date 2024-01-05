import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def leaf_visualizer_page_body():
    st.write("### Leaf Visualizer")
    st.info(
        f"* The client is interested in having a study that visually "
        f"differentiates a healthy and powdery leaf")
    
    version = 'v1'
    if st.checkbox("Difference between average and variability image"):
      
      avg_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
      avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

      st.warning(
        f"* There is some difference in that variance for healthy leaf is" 
        " higher since the cells are mostly similar.")

      st.image(avg_mildew, caption='Mildew Leaf - Average and Variability')
      st.image(avg_healthy, caption='Healthy Lead - Average and Variability')
      st.write("---")

    if st.checkbox("Differences between average healthy and mildew leaves"):
          diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

          st.warning(
            f"* The average for mildewleaf is also lighter showing that there is some mildew on the leaf"
            f"patterns where we could intuitively differentiate one from another.")
          st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"): 
      st.write("* To refresh the montage, click on the 'Create Montage' button")
      data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
      labels = os.listdir(data_dir+ '/val')
      display_label = st.selectbox(label="Select label", options=labels, index=0)
      if st.button("Create Montage"):      
        image_montage(dir_path= data_dir + '/val',
                      display_label=display_label,
                      nrows=8, ncols=3, figsize=(10,25))
      st.write("---")



def image_montage(dir_path, display_label, nrows, ncols, figsize=(15,10)):
  sns.set_style("white")
  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if display_label in labels:

    # checks if your montage space is greater than subset size
    # how many images in that folder
    images_list = os.listdir(dir_path+'/'+ display_label)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
      print(
          f"Decrease size to create your montage. \n"
          f"There are {len(images_list)} in your set. "
          f"You requested a montage with {nrows * ncols} spaces")
      return
    

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + display_label + '/' + img_idx[x])
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)



  else:
    print(f"Please choose from: {labels}")



    
