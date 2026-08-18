def inspect_dataset(df):
    print("Shape:")
    print(df.shape)

    print("\nInfo:")
    print(df.info())

    print("\nStatistics:")
    print(df.describe())

    print("\nMissing values:")
    print(df.isnull().sum())


def analyze_fraud_distribution(df):
    print("\nFraud distribution:")
    print(df["is_fraud"].value_counts())

    print("\nFraud distribution (%):")
    print(df["is_fraud"].value_counts(normalize=True))