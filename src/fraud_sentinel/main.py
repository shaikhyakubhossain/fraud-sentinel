import pandas as pd

from fraud_sentinel.config import DATASET_PATH


def main():
    df = pd.read_csv(DATASET_PATH)
    
    print(df.head())


if __name__ == "__main__":
    main()