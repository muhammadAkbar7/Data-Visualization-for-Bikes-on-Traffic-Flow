from numpy.lib.function_base import insert
# import streamlit and pandas into python

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk



def read_gd_data(data_url, nrows):
  # reads url from 
  data_url = 'https://drive.google.com/uc?id=' + data_url.split('/')[-2]
  data = pd.read_csv(data_url, nrows=nrows)
  lowercase = lambda x: str(x).lower()
  data.rename(lowercase, axis = 'columns', inplace=True)
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

  return data

def load_data(data_url, nrows):
  # notifies reader when the data is loading and successfully read
  
  data_load_state = st.text('Loading data... Please wait')
  data = read_gd_data(data_url, nrows)
  data_load_state.text('Loading data... Successful!')
  
  return data_load_state

 # CREATING HISTOGRAM FOR DATA

def CreateHistogram(title, data_url, col_name, nrows):
  # Creates a histogram from reading a file through GoogleDrive, where the
  # "col_name" attribute is a column name in the GD file.
  st.write('Histogram to demonstrate how the trip population changed over time.')
  data = load_data(data_url, nrows)
  st.write(data)
  st.subheader(title)
  x = st.slider('x')

  hist_vals = np.histogram(data[col_name].dt.day, bins=x, range=(0,24))[0]
  st.bar_chart(hist_vals)
  
  return

#DATE_TIME = 'date/time'
# histogram for CitiBike
#htitle_cb = 'Trip Count for CitiBikes in June 2012'
#hurl_cb = INSERT1 # help
#CreateHistogram(htitle_cb,hurl_cb, 1000)

# Read Traffic Volume Code

def ReadCSV(filename):
  df = pd.read_csv(filename)
  df['Sum']=df.iloc[:,7:31].sum(axis=1)
  df = df.drop(columns=['ID','Segment ID', 'Roadway Name','From','To','Direction','12:00-1:00 AM', '1:00-2:00AM', '2:00-3:00AM', '3:00-4:00AM', '4:00-5:00AM', '5:00-6:00AM', '6:00-7:00AM', '7:00-8:00AM', '8:00-9:00AM', '9:00-10:00AM', '10:00-11:00AM', '11:00-12:00PM', '12:00-1:00PM', '1:00-2:00PM', '2:00-3:00PM', '3:00-4:00PM', '4:00-5:00PM', '5:00-6:00PM', '6:00-7:00PM', '7:00-8:00PM', '8:00-9:00PM', '9:00-10:00PM', '10:00-11:00PM', '11:00-12:00AM'])
  return df

df12 = ReadCSV("Traffic_Volume_Counts__2012-2013_.csv")
htitle_t12 = 'Traffic Count for June 2012'
hurl_t12 = 'https://drive.google.com/file/d/1OfTA1BPHDNH4C_yTEv6qUjlZUdgtK8b5/view?usp=sharing'
CreateHistogram(htitle_t12, hurl_t12,'Sum', 1000)

dr14 = ReadCSV("Traffic_Volume_Counts__2014-2020_.csv")
htitle_t14 = 'Traffic Count for June 2014'
hurl_t14 = 'https://drive.google.com/file/d/1DfbuaniDt6omkrAB-uBn5FDZJaH843nk/view?usp=sharing'
CreateHistogram(htitle_t14, hurl_t14, 'Sum', 1000)