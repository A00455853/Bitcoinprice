#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 00:18:40 2022

@author: nitinkumar
"""

import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import requests

    
    
def fetchData(curr,days):
    url ='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
    payload = {'vs_currency': {curr}, 'days': {days}}
    response = requests.get(url , params=payload)
    data = response.json()
    return data

def main():
   
     num_days = st.slider("Day", 1,400,None)
     currency = st.radio("Currency",options=["CAD", "USD", "INR"]).lower()
     st.title('Bit coin price')
     data_price = fetchData(currency,num_days)
     df = pd.DataFrame(data=(dayprice[1] for dayprice in data_price['prices']))
     st.line_chart(df,use_container_width=True)
     
     
    
      
  
   


if __name__ == "__main__":
    main()