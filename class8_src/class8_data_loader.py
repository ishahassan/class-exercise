import logging
import pandas as pd

logger = logging.getLogger(__name__)

def load_netflix(filepath):
    """Load the Netflix CSV file."""
    # TODO 1:
    # Load filepath using pd.read_csv().
    df = pd.read_csv(filepath)
    # Log an INFO.
    logger.info("Successfully loaded data from %s", filepath)
    # Return the DataFrame.
    return df