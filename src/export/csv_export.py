import pandas as pd


def export_to_csv(results, filename="output/ranking.csv"):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)