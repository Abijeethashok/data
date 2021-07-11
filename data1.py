import plotly.express as px
import pandas as ps 
import csv 

df = ps.read_csv("data.csv")
fig = px.bar(df,x = "Country",y = "InternetUsers" )
fig.show()
