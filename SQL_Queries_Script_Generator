import pandas as pd
import os

def save_sql_queries(file_path, sheet_name, save_path):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    grouped = df.groupby('SCRIPT')

    for name, group in grouped:
        #queries = group['IN SQL'].tolist()
        #query = "SELECT\ntime_Stamp as PI_TIMESTAMP,\n\n" + "\n".join(group['IN SQL'].tolist()) + \
        #"\n\nFROM public.courbes_ptr3_10m_avg\nWHERE Time_Stamp BETWEEN NOW() - INTERVAL  '31 DAY' AND NOW();"           
        queries = group['IN SQL'].tolist()
        query = "SELECT\ntime_Stamp as PI_TIMESTAMP,\n\n" + "\n".join(group['IN SQL'].tolist())
        query = query.rsplit(',', 1)[0] + "\n\nFROM public.courbes_ptr1_10m_avg\nWHERE Time_Stamp BETWEEN NOW() - INTERVAL  '31 DAY' AND NOW();"
        file_path = os.path.join(save_path, f"{name}.sql")
        with open(file_path, "w") as f:
            f.write(query)

if __name__ == "__main__":
    file_path = r"C:\Users\JeremiahDeJesus\Documents\GitHub\SQL_Queries_Script_Generator\Queries.xlsx"
    sheet_name = "BLK01"
    save_path = "C:/Users/JeremiahDeJesus/Documents/GitHub/SQL_Queries_Script_Generator"
    save_sql_queries(file_path, sheet_name, save_path)
