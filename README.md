----
# wesplit-demo
----
- Author: Jaelin Lee
- Date: Mar 18, 2023
- Description: WeSplit Receipt OCR Demo

----
# How To
----
1. Set up
### Run automated script to install packages
- chmod +x install_packages.sh
- sh install_packages.sh

2. Input
### Add a scanned receipt (i.e. .JPG, .PNG) to `raw/` folder

3. Preprocess Input Image and Run OCR
- python3 run.py

4. Output
- Enhanced receipt (.JPG) saved in `preprocessed/`folder
- OCR text ourput (.txt) saved in `output/` folder
