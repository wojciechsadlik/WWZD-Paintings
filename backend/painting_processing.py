import os
import numpy as np
import pickle

from keras.preprocessing.image import load_img

from keras.applications.resnet import preprocess_input, ResNet50
from keras.models import Model

from sklearn.decomposition import PCA

PCA_PICKLE_PATH = 'pca.pkl'

model = ResNet50()

model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

global pca
pca = PCA(n_components=2)

def fit_pca():
    global pca

    if os.path.isfile(PCA_PICKLE_PATH):
        with open(PCA_PICKLE_PATH, 'rb') as pca_file:
            pca = pickle.load(pca_file)
            print('\npca loaded\n')
        return

    data_files = {
        'abstract': [],
        'animal-painting': [],
        'cityscape': [],
        'figurative': [],
        'flower-painting': [],
        'genre-painting': [],
        'landscape': [],
        'marina': [],
        'mythological-painting': [],
        'nude-painting-nu': [],
        'portrait': [],
        'religious-painting': [],
        'still-life': [],
        'symbolic-painting': []
    }

    for dirpath, dirnames, files in os.walk('dataset'):
        for file_name in files:
            data_files[os.path.basename(dirpath)].append(
                load_img(os.path.join(dirpath, file_name), target_size=(224,224))
            )

    for key in data_files:
        data_files[key][:] = [
            preprocess_input(np.array(img).reshape(1,224,224,3)) for img in data_files[key]
        ]

    predictions = dict.fromkeys(data_files)

    print('\nfitting pca\n')
    for key in data_files:
        print(key)
        predictions[key] = []
        for img in data_files[key]:
            predictions[key].append(model.predict(img, use_multiprocessing=True))


    all_imgs = []

    for key in predictions:
        for img in predictions[key]:
            all_imgs.append(img.reshape(img.shape[1]))

    all_imgs = np.array(all_imgs)
    
    pca.fit(all_imgs)

    print('\npca fitted\n')

    with open(PCA_PICKLE_PATH, 'wb') as pca_file:
        pickle.dump(pca, pca_file)


def get_point(image):
    loaded_image = load_img(image, target_size=(224,224))
    model_input = preprocess_input(np.array(loaded_image).reshape(1,224,224,3))
    features = model.predict(model_input)

    coords = pca.transform(features)
    return coords[0][1], coords[0][1]


def get_style(image):
    return 'abstract'