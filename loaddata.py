from varsity.models import Varsity
import sys
import pandas as pd
f=pd.read_csv('varsitylist.csv',sep=',')
for i in range (1,146):
    # print(f["University Name"][i])
    j=Varsity.objects.filter(univarsity_nickname=f["Nickname"][i])
    if j:
        continue
    else:
        item=Varsity.objects.create(
        univarsity_name=f["University Name"][i],
        univarsity_nickname=f["Nickname"][i],
        foundation=int(f["Founded"][i]),
        location=f["Location"][i],
        division=f["Division"][i],
        specailization=f["Specialization"][i],
        phdgranting=f["Ph.d Granting"][i],
        category=f["Type"][i],
        link=f["Link"][i]
        )