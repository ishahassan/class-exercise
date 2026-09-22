import json
import logging
from logging import config
from pathlib import Path

import pandas as pd
import yaml
import os
from dotenv import load_dotenv

file_path_csv = Path(__file__).parent / "data" / "sample.csv"
file_path_json = Path(__file__).parent / "data" / "sample.json"
file_path_yaml = Path(__file__).parent / "data" / "sample.yaml"
file_path_env = Path(__file__).parent / "data" / ".env"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def inspect_csv(filepath):
    """Read a CSV file and display basic information."""
    # 1. Read the file using pd.read_csv().
    df = pd.read_csv(filepath)
    # 2. Log the filepath at INFO.
    logger.info(f"Inspecting CSV: {filepath.name}") #or automate with logger.info(f"Inspecting {filepath.suffix} : {filepath.name}")
    # 3. Print the first three rows (e.g. DataFrame.head(3))
    print(df.head(3))


def inspect_json(filepath):
    """Read a JSON file and display basic information."""
    # 1. Open the file and read it using json.load().
    with open(filepath, "r") as f:
        data = json.load(f)
    # 2. Log the filepath at INFO.
    logger.info(f"Inspecting JSON: {filepath.name}")
    # 3. Print the contents.
    print(data)


def inspect_yaml(filepath):
    """Read a YAML file and display basic information."""
    # 1. Open the file and read it using yaml.safe_load().
    with open(filepath, "r") as f:
        data = yaml.safe_load(f)
    # 2. Log the filepath at INFO.
    logger.info(f"Inspecting YAML: {filepath.name}")
    # 3. Print the contents.
    print(data)


def inspect_env():
    """Read a .env file and display basic information."""
    load_dotenv()

    keys = [
        key for key in ["USERNAME", "PASSWORD"]
        if os.getenv(key) is not None
    ]

    # TODO:
    # 1. Log at INFO that .env was loaded.
    logger.info("Loaded environment variables from .env")
    # 2. Print keys.
    # Do not print passwords, API keys, or other secret values.
    print(keys)


def main():
    # TODO:
    # 1. Create a Path object for the data directory.
    data_dir = Path("data")

    # 2. Use the / operator to build the CSV, JSON, and YAML paths.
    csv_path = data_dir / "sample.csv"
    json_path = data_dir / "sample.json"
    yaml_path = data_dir / "sample.yaml"

    # 3. Call each inspection function using the matching path.
    inspect_csv(csv_path)
    inspect_json(json_path)
    inspect_yaml(yaml_path)

    # 4. Call inspect_env() without an argument.
    inspect_env()


if __name__ == "__main__":
    main()
