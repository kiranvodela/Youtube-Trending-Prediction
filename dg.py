import pandas as pd
import random as rd
import math
d = []
for i in range(100):
    r1 = rd.randint(1000, 10000)
    r2 = rd.randint(1, 1000)
    r3 = rd.randint(1, 1000)
    r4 = rd.randint(1, 1500)
    r5 = rd.randint(1, 1500)
    num_of_features = 5
    out = (r1+r2+r3+r4+r5)
    threshold = 7000
    if r2<r3:
        result = 0
    else:
        result = 1
    if out>threshold:
        clss = 1
    else:
        clss = 0
    d.append([r1,r2,r3,r4,r5,clss])
df = pd.DataFrame(d,columns=['Views','Likes','Dislikes',
                             'Comments','Shares','Result'])
df.to_csv('temp.csv',index=False)
