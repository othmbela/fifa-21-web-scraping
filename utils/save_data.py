from itertools import chain
import pandas as pd

def save_data(data):
    """
    Save the data scrapped by generating a .csv file
    """
    flatten = lambda x: list(chain.from_iterable(x))

    df = pd.DataFrame(flatten(data))
    df.to_csv('./data/fifa21.csv', index=False)