from class8_src import load_netflix, require_columns
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

def main():
    input_path = Path("data/messy_netflix_titles.csv")

    # TODO 3:
    # Inside a try/except block:
     # Load the data and require columns: ["title", "type", "release_year"].
    try:
        df = load_netflix(input_path)
        df = require_columns(df, ["title", "type", "release_year"])

    # Catch ValueError and exit with status code 1.
    except ValueError as e:
        logger.error("Error occurred: %s", e)
        exit(1)

    # Log an INFO
    logger.info("Pipeline Completed.")


if __name__ == "__main__":
    main()