----
## Faded, Torn, Rotated Receipt OCR with Image Preprocessing
As part of KaggleX BIPOC Mentorship Program-Cohort2 (Dec 2022 - Mar 2023), I created a Receipt OCR Web App called **WeSplit**. This app utilizes [Tesseract OCR engine](https://github.com/tesseract-ocr/tesseract), an open source library, and custom preprocessing steps that I designed to improve the quality of the input image. The subset of the code is shared here to demonstrate the preprocessing steps and its positive impact to the OCR output.

- Author: Jaelin Lee
- Date: Mar 18, 2023
- [LinkedIn](https://www.linkedin.com/in/jaelin-lee-23678458/)
----

## Installation
1. Download this repository to your local machine
2. Open the project directory
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
- Enhanced receipt (`enhanced.jpg`) is saved in `preprocessed`folder
- OCR text ourput (`enhanced.txt`) is saved in `output` folder

Enjoy! 

Faded Receipt:

<img width="1334" alt="Screenshot 2023-03-18 at 6 48 51 PM" src="https://user-images.githubusercontent.com/12604611/226144208-a6bc4a13-9943-484c-87c2-e3cc6c49eb8e.png">

Rotated / Crumbled Receipt:

<img width="1199" alt="Screenshot 2023-03-18 at 6 56 52 PM" src="https://user-images.githubusercontent.com/12604611/226144334-4e8518e8-584a-4f2a-878c-a86bd2a24321.png">

Torn Receipt:

<img width="850" alt="Screenshot 2023-03-18 at 6 54 17 PM" src="https://user-images.githubusercontent.com/12604611/226144251-d15c7365-3f1b-446e-a62b-280346fc3872.png">

## Preprocessing Components
<img width="366" alt="Screenshot 2023-03-18 at 6 59 03 PM" src="https://user-images.githubusercontent.com/12604611/226144425-a8c9be8c-3c2f-4bbc-aac1-40cfa913e5ec.png">

## Reference:
- For a detailed explanation of the preprocessing steps used in this project (https://medium.com/@jaelin_75015/faded-torn-rotated-receipt-ocr-with-image-preprocessing-1fb03c036504)
- For a quick sample run of this project in Kaggle notebook (https://www.kaggle.com/jaelin215/faded-receipt-ocr-tesseract-preprocessing)

## License:
- MIT License
- I would appreciate if you quote my name and the link to this GitHub repo if you reference this code. Thanks!
----
