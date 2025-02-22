import matplotlib.pyplot as plt
import seaborn as sns

def add_domestic_indicator(df_trans):
    df_trans['domestic'] = df_trans['country'].apply(lambda x: 'Yes' if x == 'Ireland' else 'No')
    return df_trans

def plot_transaction_distribution(df_trans):
    plt.figure(figsize=(8,6))
    sns.boxplot(x='domestic', y='amount', data=df_trans)
    plt.title('Transaction Amount Distribution (Domestic vs International)')
    plt.show()

def plot_transaction_by_country(df_trans):
    plt.figure(figsize=(12,6))
    sns.boxplot(x='country', y='amount', data=df_trans)
    plt.xticks(rotation=90)
    plt.title('Transaction Amount Distribution by Country')
    plt.show()
