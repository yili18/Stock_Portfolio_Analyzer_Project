
# Portfolio Analyzer 



## Import Libraries/ Installation Guide
import os

import requests

import json

import pandas as pd

import numpy as np

from dotenv import load_dotenv

import alpaca_trade_api as tradeapi

## List of Stocks:

 Apple – AAPL

-Microsoft – MSFT

Google - GOOGL

Amazon - AMZN

Facebook - FB

Johnson and Johnson - JNJ

JP Morgan - JPM

Visa - V

Proctor and Gable - PG

Tesla - TSLA

 
## Perspective of Project
Role - Client

Goal - Access account

Benefit - to decide on what stocks to buy by utilizing tools like plots, simulations, etc


## Project Script

Client enters the portal

Client asked to enter client id number and 5 digit pin code

Portal confirms the client’s id and pin code
Once confirmed, the client is asked what he wants to do.

Check account balance

Select a stock
Client is asked to enter the crypto ticker of three stocks for comparison

Client is asked to choose between

ROI

Volatility

Sharpe Ratio

Monte Carlo Simulation

Client is asked if he wants to buy

Asked how much

If amount is greater than account balance reject

purchase otherwise sell to client

Codes and Formulas

Questionary

Monte Carlo simulation - brownian movement

Sharpe Ration - omigarish

ROI, Volatity, box plot



## Process of Stock Selection & Usage

Stocks were selected based on the top ten large market cap companies

Then a random 3 was selected from the 10 to run analysis
Sharpe Ratio Breakdown

## Calculate Sharpe Ratio for top ten large market cap companies
### Calculate Closing price for each of the top ten companies over ten years
### Calculate the daily returns data for each of the top ten large market cap companies over ten years
### Calculate the standard deviation by using the ***std.()*** function of daily returns
### Calculate the annualized standard deviation (252 trading days) for each of the top ten large market cap companies
### Calculate the annualized Sharpe Ratios for each of the top ten large market cap companies
### Visualize the Sharpe ratios as a bar chart
### Compare the Sharpe Ratios for each of the top ten large market cap companies to determine which company has the best risk-adjusted performance
## Monte Carlo Simulation & GBM Breakdown

MONTE CARLO SIMULATION
We randomly choose three stocks from the list
["AAPL", "MSFT", "AMZN", "GOOGL", "FB", "JNJ", "JPM", "V", "PG", "TSLA"]
For example
['AMZN', 'JNJ', 'AAPL']
Then we generate Monte Carlo Simulation
And a plot of the distribution of Final Cumulative returns
Summarize the Cumulative Returns
Print an analysis of the 95% Confidence Interval
GEOMETRIC BROWNIAN MOTION SIMULATIONS
First we generate an even weight GBM simulations for the cumulative portfolio from the randomly chosen stocks previously.
Next we generate an even weight GBM simulations for the cumulative portfolio for ALL ten stocks.
Last we generate an even weight GBM simulations for EACH of the ten individual
stocks.


## Contributors:

Yi Li

Liza Gino

Randy Miyazaki

Cesar Estrada

Kacie Motley