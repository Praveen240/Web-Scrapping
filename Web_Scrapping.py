#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
gdp_html=requests.get(url)
html_text=gdp_html.text


# In[2]:


soup=BeautifulSoup(html_text,"html5lib")


# In[3]:


list_html=soup.find_all(name="tr")
states_list=[]
dict_gdp=[]
k=0
for table_data in list_html[6:219]:
    td_data=table_data.find_all("td")
    for i in td_data:
        states=i.a
        states_list.append(states.string)
        break
    n=[]
    dict_temp={"Country":None,"Region":None,"Imf":None}
    for i in td_data[1:3]:
        n.append(i.string)
    dict_temp['Country']=states_list[k]
    k+=1
    dict_temp['Region']=n[0]
    dict_temp['Imf']=n[1]
    dict_gdp.append(dict_temp)


# In[4]:


import json
json_data = json.dumps(dict_gdp, indent=2)
with open('output.json', 'w') as json_file:
    json_file.write(json_data)


# In[5]:


dataframe_gdp=pd.read_json('output.json')


# In[6]:


display(dataframe_gdp)


# In[7]:


dataframe_gdp.loc[dataframe_gdp['Imf'] == '—', 'Imf'] = '0'


# In[8]:


display(dataframe_gdp)


# In[9]:


dataframe_gdp.to_csv("Countrygdp.csv")


# In[10]:


dataframe_gdp.rename(columns={'Imf': 'billions'}, inplace=True)


# In[11]:


display(dataframe_gdp)


# In[12]:


csv_file=pd.read_csv('Countrygdp.csv')
display(csv_file)


# In[13]:


csv_file.rename(columns={'Imf':'Billions'}, inplace=True)


# In[14]:


csv_file['Billions']=csv_file['Billions'].str.replace(",","")
display(csv_file)


# In[15]:


csv_file['Billions']=csv_file['Billions'].astype(int)
csv_file['Billions']=round(csv_file['Billions']/1000,2)


# In[16]:


display(csv_file)
csv_file.to_csv('Countrygdp.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




