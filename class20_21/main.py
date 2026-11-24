import logging
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, Query

from check_analysis import summarize_genres
from check_analysis import summarize_years
from check_analysis import filter_movies

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Movie Analysis API")
df = pd.read_csv(Path("data") / "class20_movies.csv")


@app.get("/analysis/genres", response_model=list[dict])
def get_genres(min_movies: int = Query(default=1, ge=1)):
    # TODO: Pass min_movies to summarize_genres().
    result = summarize_genres(df, min_movies=min_movies)
    # Log the number of groups at INFO and return records.
    logger.info(f"Returned genre summary: groups={len(result)}")
    return result.to_dict(orient="records")

@app.get("/analysis/years", response_model=list[dict])
def get_years(window: int = Query(default=3, ge=1)):
    # TODO: Call summarize_years() with window.
    # Log the year count and window at INFO and return records.
    result = summarize_years(df, window=window)
    logger.info(f"Returned year summary: years={len(result)}, window={window}")
    return result.to_dict(orient="records")

@app.get("/movies/filter", response_model=list[dict])
def get_filtered_movies(min_rating: float = Query(default=8.0, ge=0, le=10)):
    # TODO: Call filter_movies() with df and min_rating.
    # Log the returned row count at INFO and return records.
    result = filter_movies(df, min_rating)
    logger.info(f"Returned filtered movies: rows={len(result)}")
    return result.to_dict(orient="records")