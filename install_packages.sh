#! /bin/bash 

# For preprocessing
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

brew update --auto-update
brew upgrade
pip3 install wheel

pip3 install autopep8
pip3 install numpy
pip3 install opencv-python
pip3 install imutils
brew install pillow
pip3 install matplotlib
pip3 install pytesseract

brew install graphviz
pip3 install code2flow

# For Flask
pip3 install Flask
pip3 install healthcheck
pip3 install plotly-express
pip3 install requests


