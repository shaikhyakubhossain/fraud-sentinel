from fraud_sentinel.analysis.analysis import (
    analyze_fraud_distribution,
    inspect_dataset,
)
from fraud_sentinel.data.loader import load_dataset
from fraud_sentinel.visualization.plots import (
    plot_amount_distribution,
    plot_fraud_distribution,
)


def main():
    df = load_dataset()

    inspect_dataset(df)
    analyze_fraud_distribution(df)

    plot_fraud_distribution(df)
    plot_amount_distribution(df)


if __name__ == "__main__":
    main()