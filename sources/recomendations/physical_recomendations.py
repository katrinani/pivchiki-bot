import os

import librosa
import tensorflow_hub as hub
import numpy as np
from sklearn.decomposition import TruncatedSVD

model_vggish = hub.load('https://tfhub.dev/google/vggish/1')

def extract_features(audio_path):
    audio, sr = librosa.load(audio_path, sr=16000)
    features = model_vggish(audio)
    features = np.mean(features, axis=0)
    return features



def extract_svd_features(track_name):
    audio_path = os.path.join(os.getcwd(), track_name)
    features = extract_features(audio_path)
    #svd = TruncatedSVD(n_components=3)
    #svd_features = svd.fit_transform([features.tolist()])[0].tolist()

    return features#, svd_features

