# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:58:34 2017

@author: anni11
"""


class NlpClassifier(object):
    def __init__(self,arr):
        self.mapp=dict()
        self.mapp2=dict()
        self.N=len(arr)
        self.m_val=1
        for i in range(len(arr)):
            self.mapp[arr[i]]=i
            self.mapp2[i]=arr[i]
        self.totalWords=[0 for i in range(5)]
        self.l=[[] for i in range(5)]
        self.prob=[dict() for i in range(len(arr))]
    
    def calculate_probability(self):
        for i in range(self.N):
            for keys in self.prob[i].keys():
                self.prob[i][keys]=self.prob[i][keys]/self.totalWords[i]
                self.m_val=min(self.m_val,self.prob[i][keys])

    def train(self,filename):
        file=open(filename,"r")
        for line in file:
            tokens=line.split()
            idx=self.mapp[tokens[-1]]
            for token in tokens:
                if token==',,,':
                    break
                self.totalWords[idx]+=1
                if token not in self.prob[idx]:self.prob[idx][token]=1
                else: self.prob[idx][token]+=1
            self.l[idx].append(tokens[0:-2])
        self.calculate_probability()
        
        
    def accuracy_test(self,fileName):
        file=open(fileName,"r")
        tot=0
        hit=0
        for line in file:
            tot+=1
            tok=line.split()
            label=tok[-1]
            tok=tok[0:-2]
            ques=""
            for s in tok:
                ques+=s
                ques+=" "
            print(self.mapp2[self.predict(ques)[0][1]])
            if self.mapp2[self.predict(ques)[0][1]]==label:
                hit+=1
        return hit/tot
        
        
    def predict(self,ques):
        l=ques.split()
        res=[]
        for i in range(self.N):
            r=1
            for s in l:
               if s in self.prob[i]:r=r*self.prob[i][s]
               else:r*=self.m_val
            res.append((r,i))
        res.sort(reverse=True)
        return res


classifier=NlpClassifier(["who","what","when","affirmation","unknown"])
classifier.train("training_data.txt")

# print(classifier.predict("who are you?"))
print(classifier.accuracy_test("accuracy_test.txt"))
