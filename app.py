#import libraries 
import streamlit as st 
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

#Load dataset
data = pd.read_csv('vehicles_us.csv')

#Cleaning data 
#Correcting datatypes for model_year: 
data['model_year']=data['model_year'].astype('Int64')

#Correcting datatypes for odometer: 
data['odometer']=data['odometer'].astype('Int64')

#Correcting datatypes for date_posted: 
data['date_posted'] = pd.to_datetime(data['date_posted'],format ='%Y-%m-%d')

#Filling missing values for is_4wd
data['is_4wd']=data['is_4wd'].fillna(0)

#Filling missing values for odometer
data['odometer']=data['odometer'].fillna(0)

#Filling missing values for paint_color
data['paint_color']=data['paint_color'].fillna('unkown')

#Filling missing values for cylinders
data['cylinders']=data['cylinders'].fillna('unkown')

#Dropping missing values for model_year 
data = data.dropna(subset=['model_year'])

st.header('Visualizations of the Data for Price & Type of Car')

#Creating a Plotly Express Histogram 
fig1 = px.histogram(data[data['price']<=100000], x= 'price',
title='Price Distribution')
st.plotly_chart(fig1)



#Creating a Plotly Express Scatter Plot 
fig2 = px.scatter(data, x='type', 
y= 'price', title= 'Price Compared to Type')
st.plotly_chart(fig2)

#Creating a Checkbox  
show_plot=st.checkbox("Show Scatter Plot") 

if show_plot: 
    fig3,ax = plt.subplots() 
    ax.scatter(data['odometer'],data['price']) 
    ax.set_xlabel('Odometer')
    ax.set_ylabel('Price') 
    ax.set_title('Odometer Compared to Price') 
    st.pyplot(fig3) 
else:
    st.write("Check the box to display scatter plot.") 
