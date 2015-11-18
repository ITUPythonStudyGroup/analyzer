import rethinkdb as r

DB = {
    'host': '46.101.205.29',
    'db': 'kickstarter',
}

connection = r.connect(**DB).repl()
data = r.table('projects_recently_launched')\
    .pluck('launched_at', 'deadline')\
    .run()

durations = [touple['deadline'] - touple['launched_at'] for touple in data]
seconds = float(sum(durations) / len(durations))
days = seconds / 60 / 60 / 24
print('The average duration of campaigns is %.2f days' % days)
