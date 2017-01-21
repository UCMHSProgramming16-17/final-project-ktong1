# Import needed modules
import csv
import math
import requests

# Question: Compare the production of 3 different energy sources (renewable, nuclear, natrual gas) in kJs, by month, over the last 20 years

# Define global EIA API key variable
EIA_APIkey = "a0758428314605c2172e496804668b98"
 
# Collect renewable data
def collectdata_renewable():
    
    # Define api basics
    # Note: url, with various ids and series, found on eia site
    url_renewable = "http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.REPRBUS.M"
    
    # Insert EIA API key into url
    url_renewable = url_renewable.replace("YOUR_API_KEY_HERE", EIA_APIkey)
    
    # Send data requests and store in a variable
    json_renewable = requests.get(url_renewable)
    
    # Convert from json into python
    renewable_0 = json_renewable.json()
    
    # Convert data into kJ from trillions of butanes (1055055852620 kJ per trillion butane)
    renewable_data = renewable_0['series'][0]['data']
    for a in renewable_data:
        a[1] = a[1]*1055055852620
        
    # Return data
    return renewable_data

# Collect nuclear data
def collectdata_nuclear():
    
    # Define api basics
    # Note: url, with various ids and series, found on eia site.
    url_nuclear = "http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.NUETPUS.M"
   
    # Insert EIA API key into url
    url_nuclear = url_nuclear.replace("YOUR_API_KEY_HERE", EIA_APIkey)
    
    # Send data requests and store in a variable
    json_nuclear = requests.get(url_nuclear)
    
    # Convert from json into python
    nuclear_0 = json_nuclear.json()
    
    # Convert data from millions of kilowatt-hours into kJ (3600000000kJ per million of kilowatt-hours)
    nuclear_data = nuclear_0['series'][0]['data']
    for a in nuclear_data:
        a[1] = a[1]*3600000000
        
    # Return data
    return nuclear_data

# Collect natural gas data
def collectdata_naturalgas():
    
    # Define api basics
    # Note: url, with various ids and series, found on eia site
    url_naturalgas = "http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.NGELPUS.M"
    
    # Insert EIA API key into url
    url_naturalgas = url_naturalgas.replace("YOUR_API_KEY_HERE", EIA_APIkey)
    
    # Send data requests and store in a variable
    json_naturalgas = requests.get(url_naturalgas)
    
    # Convert from json into python
    naturalgas_0 = json_naturalgas.json()
    
    # Convert data from billions of cubic feet of natural gas to kJ (1055055852620kJ per billion ft^3 of natural gas)
    naturalgas_data = naturalgas_0['series'][0]['data']
    for a in naturalgas_data:
        a[1] = a[1]*1055055852620
   
    # Return data
    return naturalgas_data

# Store data in csv files  
def storedata(data1, data2, data3, type1, type2, type3, csvtitle):
    
    # Make csv files
    csvfile = open(csvtitle, "w")
    
    # Create csvwriter
    csvwriter = csv.writer(csvfile, delimiter = ",")
    
    # Put data into csv files
    csvwriter.writerow(['Year/Month', type1 + ' (kJ)', type2 + ' (kJ)', type3 + ' (kJ)'])
    for a in data1:
        csvwriter.writerow([str(a[0][0:4]) + "-" + str(a[0][4:6]), str(a[1]), str(data2[data1.index(a)][1]), str(data3[data1.index(a)][1])])

# Call all functions
storedata(collectdata_renewable(), collectdata_nuclear(), collectdata_naturalgas(), 'Renewable Energy', 'Nuclear Energy', 'Natural Gas Energy', 'energydata.csv')