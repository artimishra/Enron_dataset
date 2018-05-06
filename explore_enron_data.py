#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
#length of enron dataset
len(enron_data)
length=len(enron_data.keys())
print("Length of Enron data")
print(length)

#for each person features length of features
list1=list(enron_data.values())
len(list1[0])
list2=list(enron_data.keys())
enron_data[list2[0]]
length1=len(enron_data['SKILLING JEFFREY K'])
print("For each person features lenth is")
print(length1)

#calculating person of interest
count=0
for i in range (len(enron_data)):
	a=list(enron_data.values())
	if a[i]['poi']==1:
		count=count+1
print("Count of POI IN enron dataset")
print(count)

#how many poi exist?
poi_names = open("../final_project/poi_names.txt", 'rb')

fr=poi_names.readlines()
length=len(fr[2:])
print("How many POI exist")
print(length)
poi_names.close()




# print poi_names.read()

num_lines = sum(1 for line in open("../final_project/poi_names.txt", 'rb'))

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

file_len('../final_project/poi_names.txt')

# Check if values exist in any string in the list
matching = [s for s in enron_data.keys() if "PRENTICE" in s]
matching

# What is the total value of the stock belonging to James Prentice?
stock=enron_data['PRENTICE JAMES']['total_stock_value']
print("What is the total value of the stock belonging to James Prentice?")
print(stock)

# What is the total value of the stock belonging to Wesley Colwell?
[s for s in enron_data.keys() if "COLWELL" in s]
#enron_data['COLWELL WESLEY']
Wesley=enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print("What is the total value of the stock belonging to Wesley Colwell")
print(Wesley)

#What is the total value of the stock belonging to Jeffrey K Skilling?
[s for s in enron_data.keys() if "Skilling" in s]
Jeffrey=enron_data['SKILLING JEFFREY K']['exercised_stock_options']
#enron_data[enron_data.keys()[1]]
print("What is the total value of the stock belonging to K Jeffrey")
print(Jeffrey)

#Sort values
sorted(enron_data.keys())

#Who earned the most Money
Skilling=enron_data['SKILLING JEFFREY K']['total_payments']
Fastow=enron_data['FASTOW ANDREW S']['total_payments']
Kenneth=enron_data['LAY KENNETH L']['total_payments']
print("Maximum money earned by")
print("Skilling",Skilling)
print("Fastow",Fastow)
print("Kenneth",Kenneth)

#How a unfilled feature is denoted
Unfilled=enron_data['FASTOW ANDREW S']['deferral_payments']
print("Unfilled payments is denoted by")
print(Unfilled)

# How many folks in this dataset have a quantified salary?
# What about a known email address?
count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary+=1
    if enron_data[key]['email_address'] != 'NaN':
        count_email+=1
print (count_salary)
print (count_email)

# How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments?
# What percentage of people in the dataset as a whole is this?
count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        count_NaN_tp+=1
print("People in enron dataset have NaN for total Payments")
print (count_NaN_tp)
print("Percentage os such people")
print (float(count_NaN_tp)/len(enron_data.keys()))

# How many POIs in the E+F dataset have “NaN” for their total payments? 
# What percentage of POI’s as a whole is this?   
count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True :
        print 
        count_NaN_tp+=1
print (count_NaN_tp)
print (float(count_NaN_tp)/len(enron_data.keys()))


