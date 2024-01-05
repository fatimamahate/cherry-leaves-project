import numpy as np
import pandas as pd
import os
import base64
from datetime import datetime
import joblib

#download dataframa as csv
def download_as_csv(df):

    curr_date = datetime.now().strftime("%d%m%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Report {curr_date}.csv" '
        f'target="_blank">Download Report</a>'
    )
    return href
#load pkl files
def load_pkl_file(file_path):
    return joblib.load(filename=file_path)