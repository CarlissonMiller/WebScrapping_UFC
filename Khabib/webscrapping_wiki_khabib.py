from urllib.request import urlopen
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


name = input('Please write Khabib_Nurmagomedov? ')

def get_rows(name):
    # Catch the HTML content from URL
    wiki_url = "https://pt.wikipedia.org/wiki/"+name
    response = requests.get(wiki_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', attrs={'class':'wikitable sortable'})

    rows = table.find_all('tr')
    return rows

#print(get_rows(name))

def dataframe(name):
    # Builds a dataframe form the HTML content
    rows = get_rows(name)
    columns = [v.text.replace('\n','') for v in rows[0].find_all('th')]

    df = pd.DataFrame(columns=columns)

    for i in range(2, len(rows)):
        tds = rows[i].find_all('td')

        values = [td.text.replace('\n','') for td in tds]
        #print(values)
        #break
        df = df.append(pd.Series(values, index=columns), ignore_index=True)
    return df
        #print(pd.Series(values, index=columns))

#print(dataframe(name))

def save_dataframe(name):
    # Save the dataframe
    df = dataframe(name)
    df.to_csv(r'C:\Users\Carlisson\Google Drive\WebScrapping_UFC\Khabib\khabib.csv',index=False)
    return df

print(save_dataframe(name))

'''
# Catch the HTML content from URL
wiki_url = "https://pt.wikipedia.org/wiki/Khabib_Nurmagomedov"

response = requests.get(wiki_url)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', attrs={'class':'wikitable sortable'})

rows = table.find_all('tr')
print(len(rows))

columns = [v.text.replace('n','') for v in rows[0].find_all('th')]

df = pd.DataFrame(columns=columns)

for i in range(2, len(rows)):#len(rows)):
    tds = rows[i].find_all('td')

    values = [td.text.replace('n','') for td in tds]
    #print(values)
    #break
    df = df.append(pd.Series(values, index=columns), ignore_index=True)
    df.to_csv(r'C:\WUsers\Carlisson\Google Drive\WebScrapping_UFC\Khabib\Cartel_khabib.csv',index=False)
    #print(df)


#print(df)
'''