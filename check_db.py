import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('eval_results.db')

# Check Total Count
count = pd.read_sql_query("SELECT COUNT(*) as total FROM results", conn)
print(f"Total rows found: {count['total'][0]}")

# Check Results by Persona
summary = pd.read_sql_query("SELECT persona, AVG(did_model_lie) as lie_rate FROM results GROUP BY persona", conn)
print("\n--- Summary Table ---")
print(summary)

# See the actual lies
lies = pd.read_sql_query("SELECT category, persona, did_model_lie FROM results WHERE did_model_lie = 1 LIMIT 10", conn)
print("\n--- Sample of 'Lies' recorded ---")
print(lies)

conn.close()