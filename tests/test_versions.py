def test_pandas_version():
    import pandas as pd
    assert pd.__version__.startswith("2.")

def test_polars_version():
    import polars as pl
    assert pl.__version__.split(".")[0].isdigit()
