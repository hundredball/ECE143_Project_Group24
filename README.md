# ECE143 Project Group 2: San Diego Fire and EMS Incidents
Download the data first (https://drive.google.com/file/d/11oMf0BE1kqd8apaxumLzH4Budo28zPlX/view?usp=sharing)  
Put the 'data' folder in the same directory of python files
## Data
'data' folder includes the raw data of incidents from 2007 to 2020, and the processed data of the overall years. Additionally, it also contains zip codes, positions of fire stations, and the populations according to zip code and years. All of the data are specific for San Diego.
## Preprocessing
Command: python dataloader.py  
This command concatenates the raw data of every years, removes the data with incorrect zip codes, unifies the types of each column, and finally outputs 'all_fd_incidents.csv', which is already exists in 'data' folder.   
This process may takes over an hour. 
## Result
Open 'Final_plots.ipynb' and run the codes.  
It includes all the plots presented in the slides. 