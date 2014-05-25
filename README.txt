0) The input files 'fitness_Label_DATA_nlp.txt' and 'fitness_pre-processed_TEXT(2820).txt' need to be 
in the same folder as README.txt and my codes (runthis.sh, nlp-pg.py and model.Rmd).

1) chmod +x runthis.sh
./runthis.sh

# runthis.sh has the python (nlp-pg.py) and R (model.Rmd) code that does the text processing and modeling respectively

2) nlp-pg.py generates 4 output files: trainid.csv, testid.csv, dict.csv and allwords.csv; model.Rmd 
takes the trainid.csv, testid.csv and allwords.csv as input, and generates a html file (model.html) 
that gives the explanation, code, results and plots.

3) You have to have nltk for the python code nlp-pg.py to run, and you have to have RStudio with 
'knitr' package installed. All other R packages are automatically installed by the code.

4) Open 'words-NB-lasso.html' to read about the steps I have done.

5) Each code has its own description, if interested please open respective file and read more about the steps.
Thank you. 

Amrita Ray
