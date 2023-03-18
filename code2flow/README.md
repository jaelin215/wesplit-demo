----
Author: Jaelin Lee
Date: Mar 18, 2023
Description: How to install and run code2flow to create a flowchart of your Python file
----

1. How to install (MacOS)
   brew install graphviz
   pip3 install code2flow

2. How to run (1 python file)
   code2flow run.py

3. How to run (2 python files)
   code2flow run.py functions.py

4. How to use code2flow as library
   import code2flow
   code2flow.code2flow(['path/to/filea', 'path/to/fileb'], 'path/to/outputfile')

code2flow --help
