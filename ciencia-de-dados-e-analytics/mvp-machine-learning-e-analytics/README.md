# MVP — Machine Learning & Analytics: Room Image Classifier

Capstone project for the Machine Learning & Analytics module of the PUC-Rio "Ciência de Dados e Analytics" postgraduate program. A computer-vision deep learning model that classifies images of house interiors into 5 categories: bathroom, bedroom, dining room, kitchen, and living room.

## Approach

1. Import libraries (TensorFlow/Keras, scikit-learn, Pandas).
2. Load and preprocess the image dataset.
3. Build and configure a convolutional neural network for multiclass image classification.
4. Train and evaluate the model (confusion matrix, accuracy metrics).
5. Export the trained model.
6. Test the exported model against unseen images.

See [`datasets.md`](datasets.md) for dataset download instructions (also detailed inside the notebook).

## Contents

- [`house-data-multiclassify-dl.ipynb`](house-data-multiclassify-dl.ipynb) — full pipeline: data loading, CNN architecture, training, evaluation, model export and test.

## Tech stack

Python, TensorFlow/Keras, scikit-learn, Pandas.

## Running it

```
pip install tensorflow keras pandas scikit-learn
```

Then open the notebook and follow the dataset download instructions in section 2.
