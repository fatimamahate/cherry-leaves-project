import streamlit as st
from app_pages.multipage import MultiPage

#Load the pages
from app_pages.summary_page import summary_page_body
from app_pages.leaf_visualizer_page import leaf_visualizer_page_body
from app_pages.mildew_detector_page import mildew_detector_page_body
from app_pages.hypothesis_page import hypothesis_page_body
from app_pages.ml_performance_page import ml_performace_page_metrics

#Create the instance
app = MultiPage(app_name="Mildew Detector")
#Add pages
app.add_page('Project Summary', summary_page_body)
app.add_page('Leaf Visualizer', leaf_visualizer_page_body)
app.add_page('Mildew Detector', mildew_detector_page_body)
app.add_page('Hypothesis and Validation', hypothesis_page_body)
app.add_page('ML Performance Metrics', ml_performace_page_metrics)
#Run the app
app.run()