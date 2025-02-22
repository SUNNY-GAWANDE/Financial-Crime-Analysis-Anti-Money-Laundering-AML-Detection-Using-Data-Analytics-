def detect_suspicious_transactions(df_trans):
    high_value_transactions = df_trans[df_trans['amount'] > df_trans['amount'].quantile(0.99)]
    unusual_cash_ratio = df_trans[(df_trans['cash'] / df_trans['amount']) > 0.9]
    return high_value_transactions, unusual_cash_ratio
