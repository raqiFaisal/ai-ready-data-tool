from  pands import pd 
def load_data(path):
   return pd.read_csv(path)


def handle_missing_values(data):
        return data.fillna(0)
