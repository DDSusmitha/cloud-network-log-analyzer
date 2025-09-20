import pandas as pd
import re
import sqlite3

def parse_logs(log_file):
    log_pattern = r'(?P<ip>\S+) - - \[(?P<timestamp>.*?)\] "(?P<request>.*?)" (?P<status>\d{3}) (?P<size>\d+)'
    data = []

    with open(log_file, "r") as f:
        for line in f:
            match = re.match(log_pattern, line)
            if match:
                data.append(match.groupdict())

    df = pd.DataFrame(data)
    return df

def save_to_db(df, db_name="logs.db"):
    conn = sqlite3.connect(db_name)
    df.to_sql("logs", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Logs saved to {db_name}")

if __name__ == "__main__":
    log_path = "data/sample_logs.txt"
    df = parse_logs(log_path)
    print(df.head())  # First 5 rows
    save_to_db(df)

