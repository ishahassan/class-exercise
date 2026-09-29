# from pathlib import Path

# import pandas as pd

# data_path = Path("data") / "messy_netflix_titles.csv"
# df = pd.read_csv(data_path)

import logging
logger = logging.getLogger(__name__)



def show_overview(df):
    """Display basic information about a DataFrame."""
    # TODO 1:
    # Log a DEBUG message containing the shape.
    logger.debug(f"DataFrame shape: {df.shape}")
    # Print the shape, first five rows, column names, and data types.
    print(f"Shape: {df.shape}")
    print(f"First five rows: {df.head()}")
    print(f"Column names: {df.columns}")
    print(f"Data types: {df.dtypes}")
    

def remove_duplicates(df):
    """Remove exact duplicate rows."""
    # TODO 2:
    # Remove exact duplicate rows.
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicate row(s)")

    # Log a DEBUG message containing the before and after row counts.
    logger.debug(f"Before: {before}, After: {len(df)}")
    # Return the resulting DataFrame.
    return df


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    # Drop rows containing one or more missing values.
    before = len(df)
    df = df.dropna() 

    # Log a DEBUG message containing the before and after row counts.
    logger.debug(f"Before: {before}, After: {len(df)}")

    # Return the resulting DataFrame.
    return df