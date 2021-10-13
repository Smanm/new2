#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import pandas as pd
import requests
import json
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import seaborn as sns


# In[2]:


import warnings;
warnings.simplefilter('ignore')


# In[3]:


path=r'C:\Users\hp\Downloads\chromedriver_win32 (1)\chromedriver.exe'
browser=webdriver.Chrome(executable_path=path)


# In[4]:


browser.get('https://data.covid19india.org/')


# In[5]:


data=browser.find_element_by_xpath('/html/body/div/table[1]/tbody/tr[1]/td[2]/a')


# In[6]:


data.click()


# In[7]:


time.sleep(10)


# In[8]:


r=requests.get('https://data.covid19india.org/v4/min/timeseries.min.json')


# In[9]:


column_name=['dates','total_confirmed','total deceased']
Df=pd.DataFrame(columns=column_name)
Df
column_name=['dates','total_confirmed','total deceased']
D_frame=pd.DataFrame(columns=column_name)
D_frame


# In[10]:


state={"Abbreviation":['AN','AP','AR','AS','BR','CH','CT','DN','DD','DL','GA','GJ','HR','HP','JK','JH','KA','KL','LD','MP','MH','MN','ML','MZ','NL','OR','PY','PB','RJ','SK','TN','TG','TR','UP','UT','WB'],"State":["Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chattisgarh","Dadea and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telengana","Tripura","Uttar Pradesh","Uttrakhand","West Bengal"]}
state_name=pd.DataFrame(state)
state_name


# In[11]:


state_ab=input("ENTER THE STATE ABBREVIATION FROM ABOVE AN/GA/MH ")


# In[12]:


x=pd.datetime.now().year


# In[13]:


x=x%10


# In[14]:


Dat0={}
data0=json.loads(r.text)[state_ab]['dates']['2020-1{}-3{}'.format(2,1)]['total']['confirmed']
Data0=json.loads(r.text)[state_ab]['dates']['2020-1{}-3{}'.format(2,1)]['total']['deceased']
#data1=json.loads(r.text)['KL']['dates']
#print((data))
Dat0[Df.columns[0]]=str(['20201{}3{}'.format(2,1)])
Dat0[Df.columns[1]]=data0
Dat0[Df.columns[2]]=Data0
Df=Df.append(Dat0,ignore_index=True)
for y in range(x):
    for k in range(9):
        for i in range(9):
            try:
                Dat={}
           
            
                data1=json.loads(r.text)[state_ab]['dates']['202{}-0{}-0{}'.format(y+1,k+1,i+1)]['total']['confirmed']
                Data1=json.loads(r.text)[state_ab]['dates']['202{}-0{}-0{}'.format(y+1,k+1,i+1)]['total']['deceased']
        
                Dat[Df.columns[0]]=str('202{}/{}/{}'.format(y+1,k+1,i+1))
           
                Dat[Df.columns[1]]=data1
                Dat[Df.columns[2]]=Data1
                Df=Df.append(Dat,ignore_index=True)
                D_frame=D_frame.append(Dat,ignore_index=True)
        
            except:
                continue
        for j in range(22):
            try:
                Dat2={}
                data2=json.loads(r.text)[state_ab]['dates']['202{}-0{}-{}'.format(y+1,k+1,j+10)]['total']['confirmed']
                Data2=json.loads(r.text)[state_ab]['dates']['202{}-0{}-{}'.format(y+1,k+1,j+10)]['total']['deceased']
        
                Dat2[Df.columns[0]]=str('202{}/{}/{}'.format(y+1,k+1,j+10))
           
                Dat2[Df.columns[1]]=data2
                Dat2[Df.columns[2]]=Data2
            
                Df=Df.append(Dat2,ignore_index=True)
                D_frame=D_frame.append(Dat2,ignore_index=True)
        
            except:
                continue         
    for k in range(3):
        for i in range(9):
            try:
                Dat={}
           
            
                data1=json.loads(r.text)[state_ab]['dates']['202{}-{}-0{}'.format(y+1,k+10,i+1)]['total']['confirmed']
                Data1=json.loads(r.text)[state_ab]['dates']['202{}-{}-0{}'.format(y+1,k+10,i+1)]['total']['deceased']
       
                Dat[Df.columns[0]]=str('202{}/{}/{}'.format(y+1,k+10,i+1))
           
                Dat[Df.columns[1]]=data1
                Dat[Df.columns[2]]=Data1
                Df=Df.append(Dat,ignore_index=True)
                D_frame=D_frame.append(Dat,ignore_index=True)
        
            except:
                continue
        for j in range(22):
            try:
                Dat2={}
                data2=json.loads(r.text)[state_ab]['dates']['202{}-{}-1{}'.format(y+1,k+10,j+10)]['total']['confirmed']
                Data2=json.loads(r.text)[state_ab]['dates']['202{}-{}-1{}'.format(y+1,k+10,j+10)]['total']['deceased']
        
                Dat2[Df.columns[0]]=str('202{}/{}/{}'.format(y+1,k+10,j+10))
           
                Dat2[Df.columns[1]]=data2
                Dat2[Df.columns[2]]=Data2
            
                Df=Df.append(Dat2,ignore_index=True)
                D_frame=D_frame.append(Dat2,ignore_index=True)
        
            except:
                continue  
          


# In[15]:


display(Df)


# In[14]:


#n_rows=Df.shape[0]
Df.dtypes


# In[16]:


#pd.set_option('display.max_rows',n_rows)
D_frame=D_frame.rename(columns={"total_confirmed":"active_cases"})
D_frame=D_frame.rename(columns={"total deceased":"daily_deaths"})


# In[17]:


D_frame


# In[17]:



#rows=D_frame.shape[0]
#pd.set_option('display.max_rows',rows)


# In[18]:



#D_frame


# In[18]:


D_frame.loc[:,"active_cases"]=D_frame.loc[:,"active_cases"]- Df.loc[:,"total_confirmed"]
D_frame.loc[:,"daily_deaths"]=D_frame.loc[:,"daily_deaths"]- Df.loc[:,"total deceased"]


# In[19]:


D_frame


# In[20]:


D_frame.dtypes


# In[21]:


Df["active_cases"]=D_frame[["active_cases"]].copy()


# In[22]:


Df


# In[23]:


Df.drop(labels=["dates","total_confirmed","total deceased"],axis=1,inplace=True)


# In[24]:


Df.dropna(inplace=True)


# In[25]:


Df


# In[26]:


Df["Target_cases"]=Df.active_cases.shift(-1)


# In[27]:


Df


# In[28]:


Df.dropna(inplace=True)


# In[29]:


Df


# In[30]:


def train_test_split(dat_frame,per):
    dat_frame=dat_frame.values
    l=int(len(dat_frame)*(1-per))
    return dat_frame[:l],dat_frame[l:]


# In[31]:


train,test=train_test_split(Df,0.2)


# In[32]:


print(len(D_frame))
print(len(train))
print(len(test))


# In[33]:


test


# In[34]:


X1=train[:,:-1]
y1=train[:,-1]


# In[35]:


y1


# In[36]:


X1_test=test[:,:-1]
y1_test=test[:,-1]


# In[37]:


reg=XGBRegressor(n_estimators=700,learning_rate=0.01)
reg.fit(X1,y1,eval_set=[(X1,y1),(X1_test,y1_test)],eval_metric='rmse')


# In[38]:


predictions=reg.predict(test[:,:-1])


# In[39]:


predictions


# In[40]:


y1_test


# In[44]:


from sklearn.metrics import mean_squared_error as mse
from math import sqrt
rmse=sqrt(mse(y1_test,predictions))


# In[45]:


rmse


# #deaths_prediction_model

# In[46]:


Df["daily_deaths"]=D_frame[["daily_deaths"]].copy()


# In[47]:


Df.drop(labels=["active_cases","Target_cases"],axis=1,inplace=True)


# In[48]:


Df["Target_deaths"]=Df.daily_deaths.shift(-1)


# In[49]:


Df.dropna(inplace=True)


# In[50]:


train2,test2=train_test_split(Df,0.2)


# In[77]:


X2=train2[:,:-1]
y2=train2[:,-1]
X2_test=test[:,:-1]
y2_test=test[:,-1]


# In[78]:


reg2=XGBRegressor(n_estimators=700,learning_rate=0.01)
reg2.fit(X2,y2,eval_set=[(X2,y2),(X2_test,y2_test)],eval_metric='rmse')
reg2=XGBRegressor(objective="reg:squarederror",n_estimators=700)
reg2.fit(X2,y2)


# In[79]:


predictions2=reg2.predict(test2[:,:-1])


# In[ ]:


rmse=sqrt(mse(y2_test,predictions2))

