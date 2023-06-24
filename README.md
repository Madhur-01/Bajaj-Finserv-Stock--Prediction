# Stock-Price-Predction
In this project I analysed various time series forecasting and predictive algorithms to predict stock prices. A stock is a general term used to describe the ownership certificates of any company and it's price changes with time forming time series. Time series can be defined as an ordered sequence of data points spread across a period. Time, in this case, is usually an independent variable, whereas the other variables involved keep on changing the values.

The dataset which I used is stock exchange data for Bajaj Finserv Ltd, an Indian financial services company in order to compare the three models. The dataset spans the period from 2008 until the end of 2021. It contains the daily stock price (mean, low, and high values) as well as the total volume and the turnover of traded stocks.

There are many different techniques designed specifically for dealing with time series. Such techniques range from simple visualization tools that show trends evolving or repeating over time to advanced machine learning models that utilize the specific structure of time series. In this project, I analysed four popular approaches to learning from time-series data:

# Overview of Models

1. Prophet : Prophet FB was developed by Facebook as an algorithm for the in-house prediction of time series values for different business applications. Therefore, it is specifically designed for the prediction of business time series. It is based on Fourier Serie.

2. Neural Prophet : It is advanced version of FB Prophet based on neural networks.It bridges the gap between traditional time-series models and deep learning methods by combinig neural networks and fourier series.

3. LSTM recurrent neural networks : LSTM stands for Long short-term memory. LSTM cells are used in recurrent neural networks that learn to predict the future from sequences of variable lengths. They work with any kind of sequential data and, unlike ARIMA and Prophet, are not restricted to time series. 

4. ARIMA : It is a class of time series prediction models, and the name is an abbreviation for AutoRegressive Integrated Moving Average. The backbone of ARIMA is a mathematical model that represents the time series values using its past values.

# Results 

1 Prophet : 
