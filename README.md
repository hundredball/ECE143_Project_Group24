# ECE143 Project Team 24: San Diego Fire and EMS Incidents
This project analyzes fire and ems incident calls in San Diego.    
Plots and visualiztion shown on slides are contained on python notebook. Python notebook contains:  


1. Distribution of incident call categories  
2. Visualization of yearly, monthly and daily trends of fire incidents  
3. Mapping incident rate and population data across San Diego zip codes    
4. Comparison of incident rate to population data  
5. Correlation graph between month and zipcode

## Requirements
Python 3.75    
Matplotlib  
Pandas  
Geopandas
## Installation
Download the data first (https://drive.google.com/file/d/11oMf0BE1kqd8apaxumLzH4Budo28zPlX/view?usp=sharing)   
Put the 'data' folder in the same directory as python files  


GeoPandas is required. Follow the instruction of https://geopandas.org/install.html.  
Version: Python 3.7.5

### Environment Setup
`conda env create -f environment.yml`  
This command sets the environment named 'ECE143_Group24', which has all the required packages to run the code. 
## Data
'data' folder includes the raw data of incidents from 2007 to 2020, and the processed data of the overall years. Additionally, it also contains zip codes, positions of fire stations, geographic information of San Diego, and the populations according to zip code and years. All of the data are specific for San Diego.
## Data cleaning
`python dataloader.py`  
This command concatenates the raw data of every years, removes the data with incorrect zip codes, unifies the types of each column, and finally outputs 'all_fd_incidents.csv', which is already exists in 'data' folder.   
This process may takes over an hour. 
## Result
Open 'Final_plots.ipynb' and run the codes.  
