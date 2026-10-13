import pandas as pd
import pytest 
import pytest

with pytest.raises(ValueError):
    float("unknown")

def test_dataframe_shape():
    # This DataFrame has 5 rows and 4 columns.
    df = pd.DataFrame({
        "title": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie D"],
        "type": ["Movie", "Movie", "Movie", "Movie", "Movie"],
        "release_year": [2020, 2021, 2022, 2023, 2023],
        "rating": [7, 8, 6, 9, 9],
    })

    # assert checks a condition. If it is true, the test continues. If it is false, the test fails.
    assert df.shape == (5, 4)
    # assert df.shape == (1, 1) 
    # ^ will get an AssertionError4

def test_drop_duplicates():
    # Arrange
    df = pd.DataFrame({
        "title": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie D"],
        "type": ["Movie", "Movie", "Movie", "Movie", "Movie"],
        "release_year": [2020, 2021, 2022, 2023, 2023],
        "rating": [7, 8, 6, 9, 9],
    })
    # note: the final two rows are identical, so removing duplicates leaves four rows and four columns.

    # Act
    result = df.drop_duplicates()

    # Assert
    assert result.shape == (4, 4)
    assert result["title"].tolist() == ["Movie A", "Movie B", "Movie C", "Movie D"]

def test_invalid_numeric_value():
    df = pd.DataFrame({"rating": [7, "unknown", 9]})

    with pytest.raises(ValueError):
        pd.to_numeric(df["rating"])

def add(x,y): 
    return x + y

def create_add_k(k):
    def _add_func(x):
        return add(x,k)
    return _add_func


add_10 = create_add_k(10)
add_5 = create_add_k(5)
add_1 = create_add_k(1)

add_10(5)  # returns 15
add_5(5)   # returns 10

