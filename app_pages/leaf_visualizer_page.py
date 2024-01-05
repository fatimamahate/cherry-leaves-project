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
        dimensions = plt.imread(f"{img_path}/image_shape.pkl")
    
