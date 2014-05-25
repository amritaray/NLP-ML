#!/bin/bash

# Author: Amrita Ray
## python script (nlp-pg.py) that does the training and test split, and the natural language processing to get the feature vector
## followed by modeling in R (model.rmd)

# The argument is the threshold, please read more in nlp-pg.html, words-NB-lasso.html and model.Rmd
python nlp-pg.py 10

Rscript -e 'knitr::knit2html("model.rmd")'

exit
