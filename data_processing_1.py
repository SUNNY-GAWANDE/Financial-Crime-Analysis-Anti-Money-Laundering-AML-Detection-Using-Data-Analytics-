import pandas as pd
import re

def load_data(transactions_file, accounts_file):
    df_trans = pd.read_csv(transactions_file)
    df_accs = pd.read_csv(accounts_file)
    return df_trans, df_accs

def transaction_summary(df_trans):
    summary = df_trans.groupby(['acc_id', 'dr_cr']).agg(
        count=('tran_id', 'count'),
        avg_amount=('amount', 'mean'),
        max_amount=('amount', 'max')
    ).reset_index()
    return summary

def account_largest_credit(df_trans, df_accs):
    max_credit = df_trans[df_trans['dr_cr'] == 'Credit'].nlargest(1, 'amount')
    acc_id = max_credit['acc_id'].values[0]
    acc_name = df_accs[df_accs['acc_id'] == acc_id]['acc_holder'].values[0]
    return acc_name

def avg_days_between_transactions(df_trans):
    df_trans['tran_date'] = pd.to_datetime(df_trans['tran_date'])
    df_trans.sort_values(['acc_id', 'tran_date'], inplace=True)
    df_trans['prev_date'] = df_trans.groupby('acc_id')['tran_date'].shift()
    df_trans['days_between'] = (df_trans['tran_date'] - df_trans['prev_date']).dt.days
    avg_days = df_trans.groupby('acc_id').agg(
        avg_days=('days_between', 'mean'),
        transaction_count=('tran_id', 'count')
    ).reset_index()
    return avg_days

def coinbase_transactions(df_trans):
    return df_trans[df_trans['narrative'].str.contains('COINBASE', flags=re.IGNORECASE, na=False)]

def transactions_per_country(df_trans):
    return df_trans['country'].value_counts().reset_index().rename(columns={'index': 'country', 'country': 'transaction_count'})
