----
## Faded Receipt OCR Flask App
As part of KaggleX BIPOC Mentorship Program-Cohort2 (Dec 2022 - Mar 2023), I created a Receipt OCR Web App called **WeSplit**. 
This app utilizes [Tesseract OCR engine](https://github.com/tesseract-ocr/tesseract), an open source library, and custom preprocessing steps 
that I designed to improve the quality of the input image. 
The subset of the code is shared here to demonstrate the preprocessing steps and its positive impact to the Faded Receipt OCR output.
This code also includes flask app deployment.

- Author: Jaelin Lee
- Date: Mar 19, 2023
- [LinkedIn](https://www.linkedin.com/in/jaelin-lee-23678458/)
----

## Installation
1. Download this repository to your local machine
2. Open the project directory
3. In Terminal, run automated script to install packages
- chmod +x install_packages.sh
- sh install_packages.sh

## Input
- Upload a scanned receipt (i.e. .JPG, .PNG) 

<img width="587" alt="Screenshot 2023-03-19 at 10 01 11 PM" src="https://user-images.githubusercontent.com/12604611/226229664-8c74d8b0-b794-40e0-8289-c53e9232e1c9.png">

## Run
- python3 app.py

## Output
<img width="840" alt="Screenshot 2023-03-19 at 10 02 44 PM" src="https://user-images.githubusercontent.com/12604611/226229820-f995eb82-14f5-4771-bad8-f159f2612a3c.png">


Enjoy! 


## Flask App Components
<img width="744" alt="Screenshot 2023-03-19 at 10 02 10 PM" src="https://user-images.githubusercontent.com/12604611/226229744-75099443-05af-47a5-9d86-c2e0ba0e5632.png">

## Reference:
- For a detailed explanation of the preprocessing steps used in this project (https://medium.com/@jaelin_75015/faded-torn-rotated-receipt-ocr-with-image-preprocessing-1fb03c036504)
- For a quick sample run of this project in Kaggle notebook (https://www.kaggle.com/jaelin215/faded-receipt-ocr-tesseract-preprocessing)

## License:
- MIT License
- I would appreciate if you quote my name and the link to this GitHub repo if you reference this code. Thanks!
----
