# Carbon Border Adjustment Mechanism Research for MIT Sloan

## Overview
- The **data** folder contains where you should have your data downloaded. See below for instructions.
- The **CBAM Tipping Point** Excel sheet analyzes the payoff to the US based on the implementation of carbon pricing in other countries. The trade flow data used in this Excel sheet is sourced from Atlas of Economic Complexity and processed in Python (in the Trade tab). The model allows you to tune parameters (e.g. CP value, trade loss rate, abatement rate) and calculates the resulting payoff to the U.S. in the scenarios with and without a domestic CP
- Data_dictionary.pdf tells you about the data you downloaded from the Atlas of Economic Complexity.
- Filter.py contains the Python script used to filter and manipulate the raw data from the .csv file into data that can be directly used inside the CBAM Tipping Point sheet in the Trade tab. This data gets saved in the trade_data.csv file.
- Hs_code_classification.pdf tells us how the EU categorizes the hs_codes and the sectors. Look at the end of the pdf to see the breakdowns of the categories. This is how you filter hs_code to sector/products.
- Trade_data.csv is the data that gets put inside the Trade tab and is the result of running filter.py. It is currently the trade data for the year 2021.

## Installation

Make sure you have Python installed on your device. Run the following in terminal (MAC)

1) pip install pandas

## Downloading the data

This repository assumes that you have already downloaded the data from the Atlas of Economic Complexity by the Growth Lab at Harvard University. To download the data, complete the following steps:

1) Go to the [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/T4CHWJ) and download the 6-digit data of the year you want to analyze. Currently, trade_data.csv is for the year 2021.
2) Insert the data into the data folder.
3) Run data_to_csv.py to transform a .dta file into a .csv file. Make sure to change the string names inside the Python file to match the string names of the files you downloaded.
4) Now you should have the data in a .csv file saved inside the data folder.

## Data filtering/transformation

All data manipulation is done in the filter.py folder. All countries in the [European Union](https://en.wikipedia.org/wiki/European_Union) are combined into a bigger "country" we call "EU," and all countries that aren't USA, CAN, MEX, BRA, IND, CHN, RUS, or EU get put into "ROW" or Rest of the World. In the .csv data file, all countries are in [ISO 3166-1 alpha-3 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3).

Currently, the added sectors are chemicals, fertilizer, aluminum, iron/steel, crude, gas, and refined. Use the map_to_sector() function to add more sectors if needed. Be sure you have declared your variables before adding a new sector.
