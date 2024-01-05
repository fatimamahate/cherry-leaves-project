import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_as_csv
from src.machine_learning.predictive_analytics import (
                                                    pred_img,
                                                    resize_in_img,
                                                    plot_pred_prob
                                                    )
def mildew_detector_page_body():
    st.title("Mildew Detector")
    st.write("Business Requirement 2: The client is interested in telling"
    " whether a specific leaf has mildew or not.")
    st.info("The data set is from"
    " [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)."
    " It has over 4000 images to train, test and validate the model.")
    st.markdown("---")

    img_upload = st.file_uploader(
        "Upload cherry leaf images. You can select multiple.",
        type=["jpg", "jpeg", "png", "webp"],
        accept_multiple_files=True
    )

    if img_upload is not None:
        report = pd.DataFrame([])
        for img in img_upload:
            img_pil(Image.open(img))
            st.info(f"Leaf Image: {img.name}")
            img_arr = np.array(img_pil)
            st.image(
            img_pil, 
            caption=f"Image Size: {img_arr.shape[1]}px x {img_arr.shape[0]}px"
            )
            ver='v1'
            resized_img=resize_in_img(img=img_pil, version=ver)
            pred_prob, pred_class = pred_img(resized_img, version=ver)
            plot_pred_prob(pred_prob, pred_class)

            report= report.append({"Name":img.name,
            "Result": pred_class}, ignore_index=True)
        
        if not report.empty:
            st.success("Report")
            st.table(report)
            st.markdown(download_as_csv(df_report), unsafe_allow_html=True)