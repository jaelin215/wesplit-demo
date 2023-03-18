- Author: Jaelin Lee
- Date: Mar 18, 2023
- Description: How to install and run code2flow to create a flowchart of your Python file

---

## How to create a flowchart

1. Install(MacOS)

   - brew install graphviz
   - pip3 install code2flow

2. Run

   - code2flow run.py (--> To run 1 python file)
   - code2flow run.py functions.py (--> To run 2 python files)

3. Import as library

   - import code2flow
   - code2flow.code2flow(['path/to/filea', 'path/to/fileb'], 'path/to/outputfile')

4. Help
   - code2flow --help
