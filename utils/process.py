import pandas as pd

def process(df):
    """
    Process the data before saving it
    """

    # Drop duplicates
    df.drop_duplicates(inplace=True, ignore_index=True)

    print(df.columns)
    # Convert columns into the appropriate type
    df['height'] = df['height'].apply(convert_into_cm)
    df['weight'] = df['weight'].apply(lambda x: int(x[:-3]) * 0.45359237)

    df['value'] = df['value'].apply(convert_into_value)
    df['wage'] = df['wage'].apply(convert_into_value)

    columns = ["VIT", "TIR", "PAS", "DRI", "DEF", "PHY"]
    df[columns] = df[columns].apply(pd.to_numeric)

    # Rename Columns
    df.columns = [column.replace('_', ' ').title() if not column.isupper() else column for column in df.columns]
    df.rename({"Country": "Nationality", "Overall Rating": "Overall"}, inplace=True)

    return df


def convert_into_cm(height):
    height = height.strip('"')
    foot, inches = height.split("'")
    return int(foot) * 30.48  + int(inches) * 2.54


def convert_into_value(value):
    value = value.strip('€')
    if value[-1] == 'M':
        return float(value[:-1]) * 1e6
    elif value[-1] == 'K':
        return float(value[:-1]) * 1e3
    else:
        return float(value)