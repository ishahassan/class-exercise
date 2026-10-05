import argparse
import logging
import sys
from pathlib import Path

import pandas as pd

from class6_7_netflix_utils import (
    clean_text,
    drop_missing_rows,
    remove_duplicates,
    remove_iqr_outliers,
    show_overview,
)


logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(
        description="Explore Netflix titles"
    )
    parser.add_argument(
        "--input",
        default="data/messy_netflix_titles.csv",
        help="Path to the Netflix CSV file"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show debug messages"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S"
    )

    # TODO 4:
    # Create a Path object from args.input.
    data_path = Path(args.input)

    # Inside a try block, load that path using pd.read_csv().
    try:
        df = pd.read_csv(data_path)
            # Save original before any cleaning
        df_original = df.copy()

        logger.info(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    # Catch FileNotFoundError, log an ERROR message,
    except FileNotFoundError:
        logger.error(f"Input file not found: {data_path}")
        # and exit with sys.exit(1).
        sys.exit(1)

    # TODO 5:
    # Call show_overview().
    show_overview(df)
    # Log an INFO message.
    logger.info("Displayed overview of the DataFrame")

    # TODO 6:
    # Call remove_duplicates().
    before = len(df)
    df = remove_duplicates(df)
    logger.info(f"Removed {before - len(df)} duplicate row(s)")

    # Call drop_missing_rows().
    before = len(df)
    df = drop_missing_rows(df)
    logger.info(f"Dropped {before - len(df)} rows with missing values")

    # Log an INFO message after each step that
    # includes the number of rows removed.

    # TODO 3:
    # Inside a try block, remove runtime_minutes outliers
    try:
        before = len(df)
         # using remove_iqr_outliers() with a threshold of 1.5.
        df = remove_iqr_outliers(df, "runtime_minutes", 1.5)
        logger.info(f"Removed {before - len(df)} runtime_minutes outliers")
        # Catch ValueError and exit with sys.exit(1).# Log an INFO message.
    except ValueError as e:
        logger.error(str(e))
        sys.exit(1)

    # TODO 4:
    # Apply clean_text() to title, type, and country.
    df["title"] = df["title"].apply(clean_text)
    df["type"] = df["type"].apply(clean_text)
    df["country"] = df["country"].apply(clean_text)
    logger.info("Cleaned text fields: title, type, and country")
    # Log an INFO message.

    # TODO 5:
    # Create a report (dictionary) containing rows_before, rows_after, rows_removed, and columns.
    report = {
        "rows_before": len(df_original),
        "rows_after": len(df),
        "rows_removed": len(df_original) - len(df),
        "columns": list(df.columns)
    }
    # Log an INFO message reporting: rows_before, rows_after, rows_removed, and columns.
    logger.info(f"Report: {report}")
    

if __name__ == "__main__":
    main()
