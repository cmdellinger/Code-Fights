import pandas as pd
def jobScheduling(requestTime, jobProcess, timeFromStart):
    # store process information in DataFrame
    jobs_df = pd.DataFrame({'number': range(len(requestTime)),
                            'requestTime': requestTime,
                            'jobProcess': jobProcess})
    # intialize tracking variables
    process_que = []
    current_process = 0
    current_time = 0
    
    for time in range(timeFromStart+1):
        # queue
        for process in jobs_df[jobs_df.requestTime == time].index:
            process_que.append(process)
        # sort queue based on shortest remaining time first (SRTF)
        process_que = list(jobs_df[jobs_df.number.isin(process_que)].sort_values(by=['jobProcess','number'], ascending=False).index)

        # run process
        # if there's a process, decrement process time
        if current_time:
            current_time -= 1
            
        # load process
        # if current process is finished, load a new one
        if not current_time:
            try:
                current_process = process_que.pop()
                current_time = jobs_df.at[current_process, 'jobProcess']
            except:
                current_process = []
    process_que.reverse()
    return process_que