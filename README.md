# Financial Crime Analysis & Anti-Money Laundering (AML) Detection

## Overview
This project focuses on analyzing financial transaction data to identify potential financial crimes, including money laundering and tax evasion. Using data analytics and statistical techniques, we detect suspicious activities such as high-value transactions, irregular transaction patterns, and dormant accounts that have been reactivated. The insights generated can be used to enhance Anti-Money Laundering (AML) frameworks for financial institutions.

## Features

Transaction Analysis: Evaluates financial transactions to detect anomalies based on amount, frequency, and account activity.

Dormant Account Detection: Identifies accounts that had no activity in the first quarter but were reactivated later.

High-Value & Suspicious Transactions: Flags transactions based on predefined thresholds and cross-border money transfers.

Trade-Based Money Laundering (TBML) Indicators: Recognizes patterns that may indicate TBML schemes.

## Data & Methodology

## Data Source: Simulated transaction dataset containing account IDs, transaction dates, amounts, payment methods (cash/cheque), country, and other attributes.

## Technologies Used:

Python: Pandas, NumPy, Matplotlib, Seaborn

SQL (MySQL): Data querying and aggregation

Jupyter Notebook: Exploratory Data Analysis (EDA) & visualization

## Analysis Steps:

Descriptive Statistics: Summarizing transactions by count, mean, standard deviation, and range.

Average Days Between Transactions: Calculates transaction frequency per account.

Detection of Dormant Accounts: Identifies accounts with no transactions in Q1 but activity in Q2.

Suspicious Transaction Detection: Flags large transactions and cross-border activities.

## Key Results

Detected a transaction of $25,000 in the Cayman Islands via Coinbase XCHNG, a potential red flag for cryptocurrency-based money laundering.

Identified multiple high-value transactions in Ireland without a narrative, raising concerns about trade-based money laundering (TBML) or tax evasion.

Found the longest average transaction gap of 11.6 days for Account 30013, suggesting unusual activity compared to other accounts.
