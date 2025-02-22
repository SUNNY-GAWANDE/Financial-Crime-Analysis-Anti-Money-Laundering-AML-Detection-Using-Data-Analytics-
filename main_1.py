from data_processing import load_data, transaction_summary, account_largest_credit, avg_days_between_transactions, coinbase_transactions, transactions_per_country
from visualization import add_domestic_indicator, plot_transaction_distribution, plot_transaction_by_country
from eda import detect_suspicious_transactions

def main():
    transactions_file = 'df_trans.csv'
    accounts_file = 'df_accs.csv'
    
    df_trans, df_accs = load_data(transactions_file, accounts_file)
    
    summary = transaction_summary(df_trans)
    print("Transaction Summary:\n", summary)
    
    largest_credit_name = account_largest_credit(df_trans, df_accs)
    print("Account with largest credit:", largest_credit_name)
    
    avg_days = avg_days_between_transactions(df_trans)
    print("Average Days Between Transactions:\n", avg_days)
    
    coinbase_trans = coinbase_transactions(df_trans)
    print("Coinbase Transactions:\n", coinbase_trans)
    
    country_trans = transactions_per_country(df_trans)
    print("Transactions per Country:\n", country_trans)
    
    df_trans = add_domestic_indicator(df_trans)
    plot_transaction_distribution(df_trans)
    plot_transaction_by_country(df_trans)
    
    suspicious_transactions = detect_suspicious_transactions(df_trans)
    print("Suspicious Transactions Identified")
    
if __name__ == "__main__":
    main()
