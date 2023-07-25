import pandas as pd
import numpy as np
from .chatbot import chat
from flask import Flask, render_template, request
from .utils import MulMarker

def page_not_found(e):
    return render_template('404.html'), 404

def upload_file():
    if request.method == 'POST':
        # load files from POST request
        analysis_name = str(request.form['analysisName'])
        chosen_genes_DF = pd.read_csv(request.files['genes_file'], delimiter="\t", names=["gene"])
        clinical_filter_patient = pd.read_csv(request.files['clinical_info_file'], delimiter="\t")
        rna_filter_nor_info = pd.read_csv(request.files['rna_info_file'], delimiter="\t")
        seed = int(request.form.get('seed'))
        ratio = float(request.form.get('ratio'))
    
        uni_res_html, formula, mul_res_html, train_img, test_img, total_img = MulMarker(analysis_name, chosen_genes_DF, clinical_filter_patient, rna_filter_nor_info, seed, ratio)

        return render_template('results.html', uni_res = uni_res_html, risk_formula = formula, mul_res = mul_res_html, train_img=train_img, test_img=test_img, total_img=total_img)
 
    return render_template('upload.html')
