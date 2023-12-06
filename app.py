import numpy as np
import pandas as pd
# import plotly as px 
import streamlit as st
from PIL import Image
import requests

st.title('ICC MENS ODI CRICKET WORLD CUP 2023')
st.sidebar.title('world-cup')

def main():
    # st.title("KNOW YOUR CITIES WEATHER")
    page_bg_img ='''
    <style>
  [data-testid="stAppViewContainer"] {
    # background-image: url(https://www.cric-life.com/wp-content/uploads/2020/06/blind-cricket.jpeg);
    # background-image:url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTm-SlXk2jg3kIO_Ke8YVhIIp-ZNTjNOGWVOQ&usqp=CAU);
    background-size: cover;
}
    </style>
'''
    st.markdown(page_bg_img, unsafe_allow_html=True)
if __name__ == "__main__":
    main()

# img=Image.open('static/Cup.jpg')
# st.sidebar.image(img)
st.sidebar.title('ICC WORLD CUP 2023')

Wicket ={'Bowlers':['M Shami','A Zampa','S Madushanka','J Bumrah','G Coetzee','S Afridi','M Jensen','R Jadeja','J Hazlewood','M Santner'],
         'Wickets':[24,23,21,20,20,18,17,16,16,16]}
df3 = pd.DataFrame(Wicket)
show_chart = st.sidebar.checkbox('Show Line Chart')
if show_chart:
    st.line_chart(df3.set_index('Bowlers'))

Score ={'Batsmen':['V Kohli','R Sharma','De Kock','R Ravindra','D Mitchell','D Warner','S Iyer','Kl Rahul','Van der Dussen','M Marsh'],
    'Runs':[765,597,594,578,552,535,530,452,448,441]}
df2 = pd.DataFrame(Score)
show_chart = st.sidebar.checkbox('Show bar Chart')
if show_chart:
    st.bar_chart(df2.set_index('Batsmen'))

Squad = {'Batsmen':['R sharma','S Gill','Vkohli','S iyyer','KL Rahul','S yadav'],
         'All Rounder':['R Jadeja'],
         'Bowler':['M shami','J Bumrah','M Siraj']}
df= pd.Series(Squad)
if st.sidebar.button('squad'):
    st.write(df)

Table ={'TEAMS':['IND','AUS','RSA','NZ','PAK','AFG','ENG','BAN','SN','NED'],
        'POINTS':[18,14,14,10,8,8,6,4,4,4]}
df1= pd.DataFrame(Table)
points =bar(df1, x='TEAMS',y='POINTS')
if st.sidebar.button('points'):
    st.subheader('teams point table')
    st.bar_chart(df1.set_index('TEAMS'))

Wins ={'Teams':['IND','AUS','RSA','NZ','PAK','AFG','ENG','BAN','SN','NED'],
       'Percentage':[90,81,70,50,44,44,33,22,22,22]}
var=pd.DataFrame(Wins)

Per = px.bar(var, x='Teams',y='Percentage')
if st.sidebar.button('Per'):
    st.subheader('best win percentage in ICC WORLD-CUP 2023')
    st.write(Per)

Score ={'Batsmen':['V Kohli','R Sharma','De Kock','R Ravindra','D Mitchell','D Warner','S Iyer','Kl Rahul','Van der Dussen','M Marsh'],
    'Runs':[765,597,594,578,552,535,530,452,448,441]}
df2 = pd.DataFrame(Score)
show_chart = st.sidebar.checkbox('Show bar Chart')
if show_chart:
    st.bar_chart(df2.set_index('Batsmen'))


Wicket ={'Bowlers':['M Shami','A Zampa','S Madushanka','J Bumrah','G Coetzee','S Afridi','M Jensen','R Jadeja','J Hazlewood','M Santner'],
         'Wickets':[24,23,21,20,20,18,17,16,16,16]}
df3 = pd.DataFrame(Wicket)
show_chart = st.sidebar.checkbox('Show Line Chart')
if show_chart:
    st.line_chart(df3.set_index('Bowlers'))








    # Runs = px.bar(df2, x='Players', y='Runs')
# if st.sidebar.button('Runs'):
#     st.write(Runs)


