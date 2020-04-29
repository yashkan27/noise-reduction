#!/usr/bin/env python
# coding: utf-8

from flask import render_template
from flask import request, redirect, url_for,flash
from werkzeug.utils import secure_filename
import os
from flask import Flask
from flask import send_from_directory


import librosa
import matplotlib.pyplot as plt
import librosa.display
from scipy.io import wavfile
import numpy as np
import noisereduce as nr

app = Flask(__name__)

folder_path = 'static/upload/'
if not os.path.exists('static/upload'):
	os.mkdir(folder_path)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/process',methods=['GET','POST'])
def process():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        process.filename = filename
        file_path = folder_path+ filename
        f.save(file_path)
    audio_path = file_path
    x , sr = librosa.load(audio_path)

    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(x, sr=sr)    
    fig1 = folder_path+'original.png'
    plt.savefig(fig1)

    rate, data = wavfile.read(audio_path)
    data = np.asarray(data, dtype=np.float16)
    reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=data)
    wavfile.write(folder_path+f'clean_{f.filename}', rate, reduced_noise)

    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(reduced_noise, sr=rate)
    fig2 = folder_path+'processed.png'
    plt.savefig(fig2)

    return render_template('view.html',fig1 = fig1, fig2 = fig2,filename = filename)


@app.route('/uploads', methods=['GET', 'POST'])
def download():    
    return send_from_directory(directory=folder_path, filename='clean_'+process.filename)

app.run()
# if __name__ == "__main__":
#     app.run(debug = True,use_reloader=False)
