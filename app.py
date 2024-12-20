# Load the Iris dataset into a table using pandas
from sklearn.datasets import load_iris
import pandas as pd

def main():
    iris = load_iris()

    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

    print(iris_df)
    print("foo")
    print('asdf')

if __name__ == "__main__":
    main()