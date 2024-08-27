import pandas as pd
import argparse

def load_and_process_data(file_path):
    # issue with first row and syntax was occuring so code to get the data to load correctly w/ right columns
    df = pd.read_csv(file_path, skiprows=1, names=["General", "number_of_battles", "WAR", "aWAR"])

    # Just confirming these are both treated as numerics, csv is previous project
    df["number_of_battles"] = pd.to_numeric(df["number_of_battles"], errors='coerce')
    df["aWAR"] = pd.to_numeric(df["aWAR"], errors='coerce')
    # Code to take out generals with less than 4 battles and then sort the remaining generals by their aWAR
    #in descending order
    df_filtered = df[df["number_of_battles"] >= 4]
    df_sorted = df_filtered.sort_values(by="aWAR", ascending=False)
    
    return df_sorted

def main():
    parser = argparse.ArgumentParser(description="Process and sort generals by aWAR.")
    parser.add_argument("file_path", type=str, help="Path to the CSV file containing the generals' performance data")
    args = parser.parse_args()
      df_sorted = load_and_process_data(file_path)
    print(df_sorted)

if __name__ == "__main__":
    main()
  

