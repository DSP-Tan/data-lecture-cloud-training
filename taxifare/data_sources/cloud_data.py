from google.cloud import bigquery
import pandas as pd
import os
from colorama import Fore, Style


def get_cloud_chunk(table, index, chunk_size, dtypes):

    table = f"{os.environ['PROJECT']}.{os.environ['DATASET']}.{table}"

    client = bigquery.Client()

    rows = client.list_rows(table, start_index=index, max_results=chunk_size)

    big_query_df = rows.to_dataframe()

    if big_query_df.shape[0] == 0:
        return None  # end of data

    #big_query_df = big_query_df.astype(dtypes)

    print(f"Data loaded from BQ 🔥")
    print(big_query_df.head())

    return big_query_df

def get_bq_chunk(table: str,
                 index: int,
                 chunk_size: int,
                 dtypes: dict = None,
                 verbose=True) -> pd.DataFrame:
    """
    return a chunk of a big query dataset table
    format the output dataframe according to the provided data types
    """

    #table_path = f"{PROJECT}.{DATASET}.{table}"
    table_path = f"{os.environ['PROJECT']}.{os.environ['DATASET']}.{table}"

    if verbose:
        print(Fore.MAGENTA + f"Source data from big query {table}: {chunk_size if chunk_size is not None else 'all'} rows (from row {index})" + Style.RESET_ALL)

    client = bigquery.Client()
    try:
        rows = client.list_rows(table_path, start_index=index, max_results=chunk_size)
        df = rows.to_dataframe(dtypes=dtypes)


        # read_csv(dtypes=...) will silently fail to convert data types, if column names do no match dictionnary key provided.
        if isinstance(dtypes, dict):
            assert dict(df.dtypes) == dtypes , "Dtypes did not match specified input dtypes."


    except pd.errors.EmptyDataError:
        return None  # end of data

    return df
