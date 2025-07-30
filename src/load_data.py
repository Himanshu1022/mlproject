import pandas as pd

source_path= r"C:\Users\piyus\Downloads\archive (7).zip"
df = pd.read_csv(source_path)

destination_path = "notebook\data\stud.csv"
df.to_csv(destination_path,index=False)