# ECE143 Project Group 2: San Diego Fire and EMS Incidents
Download the data first (https://drive.google.com/file/d/11oMf0BE1kqd8apaxumLzH4Budo28zPlX/view?usp=sharing)  
Put the 'data' folder in the same directory of python files
## Data
'data' folder includes the raw data of incidents from 2007 to 2020, and the processed data of the overall years. Additionally, it also contains zip codes and positions of fire stations, and the populations according to zip code. All of the data are specific for San Diego.
## Preprocessing
Command: python dataloader.py
## dataloader.py
load(years) is used to get a dataframe of all the records in given years.  
clean_concat_data() is used to concatenate years of data and unify type of address_zip, and finally exports csv file.  
Data: 
https://drive.google.com/file/d/115-hVaf360Bo_oK6UHh0UnyDO2U3caEv/view?usp=sharing
## plot_time.py
plot_incident_time(data, unit_time) is used to plot counts of incidents over months or years.
## fire_station.ipynb
Plot the fire stations on the San Diego map
