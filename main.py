import pandas as pd


def main() -> pd.DataFrame:
    df = pd.DataFrame(data={"A": [1, 2, 3, 4, 5], "B": [1, 2, 3, 4, 5]})
    return df


if __name__ == "__main__":
    print(main())
