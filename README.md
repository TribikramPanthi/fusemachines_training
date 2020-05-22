# Ballot Paper Classification
<p align="center">
<img src="./layout.png"  />
</p>

# Project Structure

```
.
├── api_predict.py                       >>>> Prediction api
├── app.py
├── Data                                 >>>>Data folder
│   ├── Test                             >>>> Put testing data here
│   └── Train                            >>>> Put training data here
├── encoder.pkl
├── layout.png
├── main.py
├── model                               >>>>Location for model
├── model.h5                            >>>> Saved model
├── notebook                            >>>> Data analysis jupyter notebooks
├── output.jpeg
├── _predict.py                         >>>> File for making prediction
├── __pycache__
│   ├── api_predict.cpython-36.pyc
│   ├── api_predict.cpython-37.pyc
│   └── app.cpython-36.pyc
├── README.md                          >>>> README file
├── requirements.txt                   >>>> Requirement files
├── static                             >>>> Web related static files
│   └── 4585.jpg
└── templates                          >>>> Web related html and js files
    ├── index.html
    ├── js.html
    └── master.html
    
```
# Getting Started

## Install all requirements
`pip install -r requirements.txt`

## Launch Flask app

To launch the flask app, type the following command
`python app.py`

The web app is launched at your local ip `127.0.0.1:8000`

