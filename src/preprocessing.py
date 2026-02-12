import pandas as pd

def regularize_time_series(
    df,
    date_col="date",
    cols_to_convert=None,
    freq="30min"
):
    """
    Convert date column to datetime, enforce numeric columns,
    regularize time index at fixed frequency and interpolate missing values.
    """

    df = df.copy()

    # Convert date column
    df[date_col] = pd.to_datetime(df[date_col])

    # Convert selected columns to numeric
    if cols_to_convert is not None:
        df[cols_to_convert] = df[cols_to_convert].apply(
            pd.to_numeric,
            errors="coerce"
        )

    # Set datetime index
    df = df.set_index(date_col)

    # Create regular time index
    new_index = pd.date_range(
        start=df.index.min(),
        end=df.index.max(),
        freq=freq
    )

    # Reindex and interpolate
    df = df.reindex(new_index)
    df = df.interpolate(method="linear")

    # Reset index
    df = df.reset_index().rename(columns={"index": date_col})

    return df
