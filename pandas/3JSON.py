import pandas as pd

df = pd.read_json('../assets/aip.json')
print(df.to_string())
print(
    pd.json_normalize(df, record_path=['children'])
)