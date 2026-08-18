import matplotlib.pyplot as plt


def plot_fraud_distribution(df):
    fraud_counts = df["is_fraud"].value_counts()

    fraud_counts.plot(kind="bar")

    plt.title("Fraud Distribution")
    plt.xlabel("Fraud")
    plt.ylabel("Number of Transactions")
    plt.xticks(
        ticks=[0, 1],
        labels=["Legitimate", "Fraud"],
        rotation=0,
    )

    plt.show()


def plot_amount_distribution(df):
    plt.figure()

    plt.hist(df["amount"], bins=50)

    plt.title("Transaction Amount Distribution")
    plt.xlabel("Transaction Amount")
    plt.ylabel("Number of Transactions")

    plt.show()