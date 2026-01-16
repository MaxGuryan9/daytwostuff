# %%
# What is your terminal display "path"?
# type `pwd` in your terminal to see your current path
# The file path is /workspaces/daytwostuff

# %%
# Creating a virtual environment

# In your terminal, type the following command to create a virtual environment called ".venv":
# python3 -m venv .venv

# Activate the virtual environment by typing the following command in your terminal:
# source .venv/bin/activate

# You do not need to put the virtual environment into the repo but you should have a requirements.txt file that has all
# of the requirements for the virtual environment. This is because you want the dependencies within the virtual environment to be
# the same, but actually creating a virtual environment within the repo would make the repo too large. Also, it would cause dependency issues
# when other people try tp use the repo.

# type pwd again in your terminal.
# The path is the same: /workspaces/daytwostuff

# %%
# Before installing the requirements.txt file, make sure your virtual environment is activated and that pip is up to date by typing the following command in your terminal:
# pip install --upgrade pip

# The correct terminal command to load a requirements.txt file into your virtual environment is:
# pip install -r requirements.txt

# %% 
# Data Wrangler was used as the extension. 
# A NHL game dataset from Kaggle was used.

import kagglehub
from kagglehub import KaggleDatasetAdapter


file_path = "game.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "martinellis/nhl-game-data",
  file_path
)

df.head()

# %%
# The extension menu gives you different extensions to download and install that 
# can help you accomplish different tasks. It also tells you the rating and how many installs it has.

# It allows you to adjust dataframes without writing code. You click a button and it can drop NAs, for example.
# A very easy way to do data cleaning and manipulation.
# Quick summary statistics from the dataframe are shown without having to write extra code.
# Seamless and eficient ways to filter and sort data throgh the column headers.

# %%
# To install plotly in the virtual environment, type the following command in your terminal:
# pip install plotly

# To check which version of plotly is installed, type the following command in your terminal:
# pip show plotly

# The version of plotly installed is 6.5.1

# Update the requirements.txt file by typing the following code into the .txt file:
# plotly==6.5.1

# We use a requirements.txt file to keep track of the packages and the versions of each package being
# downloaded into the virtual environment. This is the easiest way to ensure that everyone has the same
# dependencies when working on a project together without having the virtual environment inside the repo.
# Also, if you are moving between different projects that require different packages and versions
# having a requirements.txt file for each project makes it easy to keep track of what you need for each projects venv.

# %%
# The correct terminal command to update the requirements.txt file with the plotly (6.5.1) package is:
# pip freeze > requirements.txt