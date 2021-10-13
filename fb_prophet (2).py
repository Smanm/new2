#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import pandas as pd
import requests
import json
from fbprophet import Prophet


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


# In[14]:


r=requests.get('https://data.covid19india.org/v4/min/timeseries.min.json')


# In[90]:


column_name=['dates','total_confirmed','total deceased']
Df=pd.DataFrame(columns=column_name)
Df
column_name=['dates','total_confirmed','total deceased']
D_frame=pd.DataFrame(columns=column_name)
D_frame


# In[28]:


state={"Abbreviation":['AN','AP','AR','AS','BR','CH','CT','DN','DD','DL','GA','GJ','HR','HP','JK','JH','KA','KL','LD','MP','MH','MN','ML','MZ','NL','OR','PY','PB','RJ','SK','TN','TG','TR','UP','UT','WB'],"State":["Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chattisgarh","Dadea and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telengana","Tripura","Uttar Pradesh","Uttrakhand","West Bengal"]}
state_name=pd.DataFrame(state)
state_name


# In[29]:


state_ab=input("ENTER THE STATE ABBREVIATION FROM ABOVE AN/GA/MH ")


# In[30]:


x=pd.datetime.now().year


# In[31]:


x=x%10


# In[32]:


x


# In[91]:


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
          


# In[92]:


display(Df)


# In[113]:


#n_rows=Df.shape[0]
#Df.dtypes
#n_rows


# In[114]:


#pd.set_option('display.max_rows',n_rows)
#D_frame=D_frame.rename(columns={"total_confirmed":"active_cases"})
#D_frame=D_frame.rename(columns={"total deceased":"daily deaths"})


# In[115]:


#D_frame


# In[35]:



#rows=D_frame.shape[0]
#pd.set_option('display.max_rows',rows)


# In[36]:



#D_frame


# In[94]:


D_frame.loc[:,"active_cases"]=D_frame.loc[:,"active_cases"]- Df.loc[:,"total_confirmed"]
D_frame.loc[:,"daily deaths"]=D_frame.loc[:,"daily deaths"]- Df.loc[:,"total deceased"]


# In[38]:


#D_frame


# In[39]:


#D_frame.dtypes


# In[95]:


active_columns=D_frame[["dates","active_cases"]]
active_df=active_columns.copy()


# In[96]:


death_columns=D_frame[["dates","daily deaths"]]
death_df=death_columns.copy()


# In[97]:


active_df.columns=['ds','y']
#active_df.dtypes


# In[98]:


death_df.columns=['ds','y']


# In[99]:


active_df['ds']=pd.to_datetime(active_df['ds'],format='%Y/%m/%d')


# In[100]:


death_df['ds']=pd.to_datetime(death_df['ds'],format='%Y/%m/%d')


# In[67]:


#active_df


# In[118]:


ml=Prophet(interval_width=0.95,yearly_seasonality=True,weekly_seasonality=True)
model=ml.fit(active_df)


# In[119]:


future=ml.make_future_dataframe(periods=30,freq='D')
forecast=ml.predict(future)


# In[120]:


forecast.tail(30)[['ds','yhat']] # yhat shows the 30 DAYS ACTIVE CASE FORECAST


# In[121]:


ml.plot(forecast)


# In[122]:


from fbprophet.diagnostics import cross_validation
data_val=cross_validation(ml,initial='223 days',period='1 days',horizon='1 days')


# In[128]:


from fbprophet.diagnostics import performance_metrics
data_metric=performance_metrics(df)
data_metric.head()


# In[125]:


df=data_val.drop(0,axis=0)


# In[126]:


df


# In[ ]:


dat_val


# In[ ]:


from sklearn.metrics import mean_squared_error as mse
from math import sqrt
rmse=sqrt(mse(y1_test,predictions))


# In[127]:


from fbprophet.plot import plot_cross_validation_metric
fig=plot_cross_validation_metric(data_val,metric='rmse')


# In[51]:


#death_df


# In[52]:


dl=Prophet(interval_width=0.95,yearly_seasonality=True)
model0=dl.fit(death_df)


# In[53]:


future2=dl.make_future_dataframe(periods=30,freq='D')
forecast2=dl.predict(future2)


# In[ ]:





# In[54]:


forecast2.tail(30)[['ds','yhat']] # yhat shows the 30 DAYS DEATH FORECAST


# In[55]:


dl.plot(forecast2)


# In[61]:


from fbprophet.diagnostics import cross_validation
df_cv2=cross_validation(dl,initial='213 days',period='1 days',horizon='30 days')
df_cv2.head()


# In[62]:


from fbprophet.plot import plot_cross_validation_metric
fig=plot_cross_validation_metric(df_cv2,metric='rmse')


# In[ ]:




