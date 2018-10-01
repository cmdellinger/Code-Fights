from operator import itemgetter
def serverFarm(jobs, servers):
    jobs = sorted(list(enumerate(jobs)), key=itemgetter(1), reverse=True)
    server_load = [[0,[]] for i in range(servers)]
    for process in jobs:
        soonest = sorted(server_load, key=itemgetter(0))[0]
        soonest[0] += process[1]
        soonest[1].append(process[0])
    return [processes for load, processes in server_load]