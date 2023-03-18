----
## Faded, Torn, Rotated Receipt OCR with Image Preprocessing
As part of KaggleX BIPOC Mentorship Program-Cohort2 (Dec 2022 - Mar 2023), I created an Receipt OCR web app called **WeSplit**. This app utilizes Tesseract OCR engine, an open source libarary, and custom preprocessing steps that I designed to improve the quality of the input image. The subset of the code is shared here to demonstrate the preprocessing steps and its positive impact to the OCR output.

- Author: Jaelin Lee
- Date: Mar 18, 2023
- Description: 
----

## Installation
1. Download this repository to your local machine
2. Oepen the project directory
3. In Terminal, run automated script to install packages
- chmod +x install_packages.sh
- sh install_packages.sh
4. Create folders under the project directory
- `raw` 
- `preprocessed`
- `output`

## Input
- Add a scanned receipt (i.e. .JPG, .PNG) to `raw` folder

## Run
- python3 run.py

## Output
- Enhanced receipt (.JPG) is saved in `preprocessed/`folder
- OCR text ourput (.txt) is saved in `output/` folder

Enjoy! 

<img width="1334" alt="Screenshot 2023-03-18 at 6 48 51 PM" src="https://user-images.githubusercontent.com/12604611/226144015-d6f04f30-f178-4e61-9d6c-b3cc02c303b8.png">

----
Reference:
- For a detailed explanation of the preprocessing steps used in this project (https://medium.com/@jaelin_75015/faded-torn-rotated-receipt-ocr-with-image-preprocessing-1fb03c036504)
