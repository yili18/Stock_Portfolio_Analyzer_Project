# Stock_Portfolio_Analyzer_Project

## Import Libraries
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



## Process of Stock Selection

Stocks were selected based on the top ten large market cap companies

Then a random 3 was selected from the 10 to run analysis
