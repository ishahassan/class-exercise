import logging

logger = logging.getLogger(__name__)

def require_columns(df, required_columns):
    """Check that all required columns exist."""
    # Check if any of the configured columns (list) are missing from df.
    missing_columns = [col for col in required_columns if col not in df.columns]

    # If any are missing, log an ERROR and raise ValueError.
    if missing_columns:
        #logger.error("Missing required columns: %s", missing_columns) 
        # #"{len(missing_columns)} columns are missing"
        logger.error("Missing Columns: {%s}", ",".join(missing_columns))
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Log an INFO.
    logger.info("Pipeline completed.")

    # Return the DataFrame.
    return df
    