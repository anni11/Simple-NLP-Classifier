# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:58:34 2017
@author: anni11
"""
def cal(sentence):
    
    l=sentence.split()
    res=[]
    for i in range(5):
        r=1
        for s in l:
           if s in cnt[i]:r=r*cnt[i][s]
           else:r*=mn
        #if r==1:r=0
        res.append((r,i))
    res.sort(reverse=True)
    return res



file =open("training_data.txt","r")
mapp=dict()

mapp["when"]=0
mapp["what"]=1
mapp["who"]=2
mapp["affirmation"]=3
mapp["unknown"]=4

cnt=[dict() for _ in range(5)]

#print(cnt)

tot=[0 for i in range(5)]
l=[[] for i in range(5)]
for line in file:
    strr=line.split()
    idx=mapp[strr[-1]]
    for s in strr:
        if s==',,,':break
        tot[idx]+=1    
        if s not in cnt[idx]:cnt[idx][s]=1;
        else: cnt[idx][s]=cnt[idx][s]+1;
    l[idx].append(strr[0:-2])

mn=1
for i in range(5):
    for keys in cnt[i].keys():
        cnt[i][keys]=cnt[i][keys]/tot[i]
        mn=min(mn,cnt[i][keys])

sen="what time does the train leave";

print(cal(sen))

