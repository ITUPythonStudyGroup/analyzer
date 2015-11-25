import rethinkdb as r
import pandas as pd
import time

DB = {
    'host': '46.101.205.29',
    'db': 'kickstarter',
}

connection = r.connect(**DB).repl()

launchedArray = []
for doc in r.table('projects_recently_launched').run():
    launchedArray.append(doc)

fundedArray = []
for doc in r.table('projects_recently_funded').run():
    fundedArray.append(doc)

launched = pd.DataFrame(launchedArray)
funded = pd.DataFrame(fundedArray)

isFunded = []

for fundedId in funded["id"]:
    for launchedId in launched["id"]:
        if launchedId == fundedId:
            isFunded.append(launchedId)


hasEnded = launched["id"][launched["deadline"] < int(time.time())]


print('The success rate is %.2f percent' % ((len(isFunded) / len(hasEnded))*100))



