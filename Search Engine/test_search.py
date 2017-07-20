import google

keyword='apple'

res_gen = google.search(keyword, stop=10)

res = []

for site in res_gen:
    if site not in res:
        res.append(site)


print res
