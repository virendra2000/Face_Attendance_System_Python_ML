import pandas as pd
from datetime import datetime as d
def searchnentry(name):
    dataset = pd.read_csv("Attendance.csv")
    t1 = dataset.set_index('Name')
    t=t1.index.get_loc(name)
    x1 = str(dataset.iloc[t,2])
    x2 = d.now().strftime("%X")
    a1 = int(x1[0:2])
    a2 = int(x2[0:2])
    hours = a2 - a1
    print(hours)
    with open('Attendance.csv', 'a+') as f:
        if hours >= 1:
            now = d.now()
            dtDate = now.strftime('%x')
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtDate},{dtString}')
            f.close()
        if hours < 1:
            pass
