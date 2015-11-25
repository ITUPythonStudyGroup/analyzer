import time, rethinkdb as r

DB = {
    'host': '46.101.205.29',
    'db': 'kickstarter',
}

connection = r.connect(**DB).repl()

# Get number of projects that have reached their deadline (finished)
finished = r.table('projects_recently_launched')\
    .between(r.minval, int(time.time()), index = 'deadline')\
    .count()\
    .run()

# Get number of projects that have reached their deadline and are funded
funded = r.table('projects_recently_launched')\
    .between(r.minval, int(time.time()), index = 'deadline')\
    .eq_join('id', r.table('projects_recently_funded'))\
    .count()\
    .run()

print('Finished: %d' % finished)
print('Funded: %d' % funded)
print('Percentage: %.2f' % (float(funded) / float(finished)))
