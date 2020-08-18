from urllib.request import urlopen
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Catch the HTML content from URL
wiki_url = "https://en.wikipedia.org/wiki/Khabib_Nurmagomedov"

response = requests.get(wiki_url)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class':'infobox vcard'}).tbody

print(len(table))

'''
rows = table.find_all('tr')

columns = [v.text for v in rows[2].find_all('th')]
#print(columns)

list = []
for i in range(2, 17):#len(rows)):
    ths = rows[i].find_all('th')
    tds = rows[i].find_all('td')
    #print(tds)
    values_ths = [th.text for th in ths]
    #values_tds = [td.text for td in tds]
    values_tds = [td.text.replace('\xa0','').replace(' (1988-09-20) 20 September 1988 (age31)Sildi, '
                                                     'Dagestan, ','').replace('5ft 10in (178cm)', '1.78m') for td in tds]
    values = (values_ths[0], values_tds[0])
    list.append(values)

def transf_dict():
    # Transforming the table into a dictionary #
    list = []
    for i in range(2, 17):#len(rows)):
        ths = rows[i].find_all('th')
        tds = rows[i].find_all('td')
        #print(tds)
        values_ths = [th.text for th in ths]
        #values_tds = [td.text for td in tds]
        values_tds = [td.text.replace('\xa0','').replace(' (1988-09-20) 20 September 1988 (age31)Sildi, '
                                                     'Dagestan, ','').replace('5ft 10in (178cm)', '1.78m') for td in tds]
        values = (values_ths[0], values_tds[0])
        list.append(values)
        dict_Khabib = dict(list)

    return dict_Khabib

dictionary = transf_dict()

print(dictionary)


def elim_keys(key):
    # Eliminating some keys#
    if key in dictionary:
        del dictionary[key]
    return dictionary

list = ["Residence","Nationality","Reach","Fighting out of","Trainer","Stance","Style","Rank"]

def dic_final():
    for i in range(0,len(list)):
        elim_keys(list[i])
    return elim_keys(len(list))

dict_final = dic_final()

def replace(key,value,new_value):
    dict_final[key] = dict_final[key].replace(value, new_value)
    return dict_final[key]

dict_final["Weight"] = replace("Weight",'155lb (70kg; 11st 1lb)[1]','70kg')

dict_final["Division"] = replace("Division",'Lightweight (2008–'
                                            '2010, 2012–present)  Welterweight (2009–'
                                            '2011)','Lightweight')
dict_final["Team"] = replace('Team','[3]','')

print(100*'#')
print(dict_final)

print(100*'#') '''
