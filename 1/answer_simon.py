import rethinkdb as r
import pandas as pd

DB = {
    'host': '46.101.205.29',
    'db': 'kickstarter',
}

connection = r.connect(**DB).repl()

res = []
for doc in r.table('projects_recently_launched').run():
    res.append(doc)
    
df = pd.DataFrame(res)

df["days"] = (df["deadline"] - df["launched_at"]) / 60 / 60 / 24

print(df["days"].mean())