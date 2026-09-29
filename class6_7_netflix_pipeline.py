import argparse
import logging
import sys
from pathlib import Path

import logging
import pandas as pd

from class6_7_netflix_utils import (
    drop_missing_rows,
    remove_duplicates,
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
    df = remove_duplicates(df)

    # Call drop_missing_rows().
    before = len(df)
    df = drop_missing_rows(df)
    logger.info(f"Dropped {before - len(df)} rows with missing values")

    # Log an INFO message after each step that
    # includes the number of rows removed.

if __name__ == "__main__":
    main()
