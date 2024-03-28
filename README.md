# Feature extraction using nPMI

This python script is designed to extract exclusive dialect features of a given dialect area.

Preparation of the data:
You are required to have a categorical dialect data (can be dialect features or multi-aligned segmental data) and a dialect classification based on the same dataset (using Relative Distance Value) before using this script, see more information about the format below.

Format required of input file:
Categorical data in the 'Gabmap' format, i.e. in a location x features tableau. Location is the first column, the rest are the list of aligned segments. The format of the file is recommended to be .csv or .txt, but you can change the settings in the script as well. An illustration of the input file can be found under 'example.csv' (based on the GTRP data from Gabmap.nl).

Before running the script:
Make sure you have added the directory of your input file (line 5) and your output file (line 80).

How to run the script:
Since this is a .py script, you have to run the script in your terminal (e.g. Anaconda prompt). First, you save this python script on your computer. Then you open your terminal and use 'cd' to change the directory into the same folder as the location where you saved this python script. Next, you type 'python nPMI_feature_extraction.py' and click enter, and the script should run automatically, given that there is no error. When you see 'file exported' on the terminal, it means the output file has been saved to the directory you gave in line 80.

Citation:
Please cite this script along with our article: Sung, H. W. M., & Prokić, J. (2024). Detecting Dialect Features Using Normalised Pointwise Information. Computational Linguistics in the Netherlands Journal, 13, 121–145. Retrieved from https://www.clinjournal.org/clinj/article/view/177

Contact:
If you have any questions, please don't hesitate to get in touch with me through h.w.m.sung[at]hum.leidenuniv[dot]nl.
