def normalize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df
from  pands import pd 
def load_data(path):
   return pd.read_csv(path)


def handle_missing_values(data):
        return data.fillna(0)
 feature/protected/main
#test pull request



def normalize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^a-z0-9_]+", "", regex=True)
    )
    return df


main
