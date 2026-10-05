# from pathlib import Path

# import pandas as pd

# data_path = Path("data") / "messy_netflix_titles.csv"
# df = pd.read_csv(data_path)

import logging
logger = logging.getLogger(__name__)
import re
import pandas as pd



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

def clean_text(value):
    """Normalize one text value."""
    # TODO 1:
    # Strip surrounding whitespace.
    value = value.strip()
    # Convert text to lowercase.
    value = value.lower()
    # Collapse repeated whitespace.
    value = re.sub(r"\s+", " ", value)
    return value


def remove_iqr_outliers(df, column, threshold):
    """Remove IQR outliers from one column."""
    # TODO 2:
    # If column does not exist:
    if column not in df.columns:
        logger.error(f"Column '{column}' does not exist in the DataFrame.")
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    # Log an ERROR message and raise ValueError.
    # Calculate Q1, Q3, and IQR.
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    # Use threshold to calculate lower and upper bounds.
    lower = q1 - threshold * iqr
    upper = q3 + threshold * iqr
    
    before = len(df)
    df = df[(df[column] >= lower) & (df[column] <= upper)]
    
    # Log a DEBUG message containing the bounds and the number of rows removed.
    logger.debug(f"Lower bound: {lower}, Upper bound: {upper}, Removed {before - len(df)} row(s)")
    
    # Return the resulting DataFrame.
    return df