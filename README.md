# Stock-Price-Pridiction
During this project, I conducted an analysis of various time series forecasting and predictive algorithms to accurately predict stock prices. A stock represents ownership certificates of a company, and its price undergoes changes over time, forming a time series. Time series refers to an ordered sequence of data points distributed across a specific period. 

In this project, I focused on the stock exchange data of Bajaj Finserv Ltd, an Indian financial services company, spanning from 2008 to the end of 2021. The dataset included daily stock prices (mean, low, and high values), total volume, and turnover of traded stocks.

There are many different techniques designed specifically for dealing with time series. Such techniques range from simple visualization tools that show trends evolving or repeating over time to advanced machine learning models that utilize the specific structure of time series. To tackle the time series analysis, I explored four prominent approaches:

# Overview of Models

1. Prophet : Prophet FB was developed by Facebook as an algorithm for the in-house prediction of time series values for different business applications. Therefore, it is specifically designed for the prediction of business time series. It utilizes Fourier series and has been widely adopted.

2. Neural Prophet :  Building upon Prophet, Neural Prophet incorporates neural networks into time series modeling, bridging the gap between traditional methods and deep learning techniques.

3. LSTM RNNs : Long Short-Term Memory (LSTM) RNNs are recurrent neural networks that excel in learning from sequential data of varying lengths. Unlike other models such as ARIMA and Prophet, LSTM RNNs are not confined to time series data and can handle a wide range of sequential data.

4. ARIMA : It is a class of time series prediction models, and the name is an abbreviation for AutoRegressive Integrated Moving Average. The backbone of ARIMA is a mathematical model that represents the time series values using its past values.

# Results 

1 Prophet :  The test data exhibited a mean absolute error (MAE) of approximately 1400, with a relative MAE about mean of 19.29%. The training error was around 380. Considering the stock price range of 4000 to 12000 in the testing dataset, the model showcased overall satisfactory performance.

2. Neural Prophet : This model performed similarly to Prophet, with a test error of around 1500 and a relative MAE about mean of 20.9%. The training error was approximately 150.

3. LSTM-RNN : Out of all the models, LSTM RNNs demonstrated the best performance. The test dataset achieved a low mean squared error (MSE) of around 60 and a relative MAE about mean of just 0.78%. This remarkable performance was observed despite the substantial price range of 4000 to 6000. The training error was around 50.

4. ARIMA : The performance of ARIMA was reasonable for the test data, with an error of around 1500 and a relative MAE about mean of 21.7%. The training error was approximately 1700.






