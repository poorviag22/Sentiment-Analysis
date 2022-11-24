import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.title("Sentiment Analysis of Tweets about US Airlines")
st.sidebar.title("Sentiment Analysis of Tweets about US Airlines")

st.markdown(" This application is a Streamlit dashboard to analyze the sentiment of Tweets 🐦 ")
st.sidebar.markdown(" This application is a Streamlit dashboard to analyze the sentiment of Tweets 🐦 ")
DATA_URL=("/home/rhyme/Desktop/Project/Tweets.csv")
@st.cache(persist=True)
def load_data():
    data=pd.read_csv(DATA_URL)
    data['tweet_created']=pd.to_datetime(data['tweet_created'])
    return data

data = load_data()

st.sidebar.subheader("Show Random Tweet")
random_tweet=st.sidebar.radio('Sentiment',('positive','neutral','negative'))
st.sidebar.markdown(data.query('airline_sentiment==@random_tweet')[["text"]].sample(n=1).iat[0,0])

st.sidebar.markdown("### Number Of Tweets By Sentiment")

select=st.sidebar.selectbox('Visualization type', ['Histogram','Pie Chart'],key='1')

sentiment_count=data['airline_sentiment'].value_counts()
st.write(sentiment_count)
sentiment_count=pd.DataFrame({'Sentiment':sentiment_count.index,'Tweets':sentiment_count.values})

if not st.sidebar.checkbox("Hide", True):
    st.markdown("### Number Of Tweets By Sentiment")
    if select =="Histogram":
        fig=px.bar(sentiment_count,x='Sentiment',y='Tweets',color='Tweets',height=500)
        st.plotly_chart(fig)
    else:
        fig=px.pie(sentiment_count,values='Tweets',names='Sentiment')
        st.plotly_chart(fig)    
