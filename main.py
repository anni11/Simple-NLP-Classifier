# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:58:34 2017

@author: anni11
"""


class NlpClassifier(object):
    def __init__(self,arr):
        # initialize the variables
        self.mapp = dict()
        self.mapp2 = dict()
        self.N = len(arr)
        self.m_val = 1
        for i in range(len(arr)):
            self.mapp[arr[i]] = i
            self.mapp2[i] = arr[i]
        self.totalWords = [0 for i in range(5)]
        self.l = [[] for i in range(5)]
        self.prob = [dict() for i in range(len(arr))]
    
    def calculate_probability(self):
        # a utility function
        # calculate the probability of the words occuring in the train data to get a NaiveBayes model
        for i in range(self.N):
            for keys in self.prob[i].keys():
                self.prob[i][keys] = self.prob[i][keys] / self.totalWords[i]
                self.m_val = min(self.m_val, self.prob[i][keys])

    def train(self,filename):
        # train the model by reading from a file
        # file consists of questions and their label
        file = open(filename,"r")
        for line in file:
            if line == '\n': continue
            tokens = line.split()
            idx = self.mapp[tokens[-1]]
            for token in tokens:
                if token == ',,,':
                    break
                self.totalWords[idx] += 1
                if token not in self.prob[idx]: self.prob[idx][token] = 1
                else: self.prob[idx][token] += 1
            self.l[idx].append(tokens[0:-2])
        self.calculate_probability()
        
        
    def accuracy_test(self,fileName):
        # test the accuracy of the algorithm by segregating some data from training data
        # returns the accuracy.
        file=open(fileName,"r")
        tot=0
        hit=0
        for line in file:
            if line == '\n': continue
            tot += 1
            tok = line.split()
            label = tok[-1]
            tok = tok[0:-2]
            ques = ""
            for s in tok:
                ques += s
                ques += " "
            if self.predict(ques) == label:
                hit += 1
        return hit/tot
        
        
    def predict(self,ques):
        # ques is the question to be predicted, it's type is string
        # returns an array of tuples = (probability of the label, label index in mapp)
        l = ques.split()
        res = []
        for i in range(self.N):
            r = 1
            for s in l:
               if s in self.prob[i]: r = r * self.prob[i][s]
               else: r *= self.m_val
            res.append((r,i))
        res.sort(reverse=True)
        return self.mapp2[res[0][1]]
    
    def predict_from_file(self,filename):
        # returns an array of tuples = (question,prediction) where the questions are read from the file predict_data.txt
        file = open(filename,"r")
        res = []
        for line in file:
            if line == '\n':
                continue
            res.append((line, self.predict(line)))
        return res
        
        
classifier = NlpClassifier(["who","what","when","affirmation","unknown"])
classifier.train("training_data.txt")
print("\nAccuracy of this Naive bayes model is: ")
print(classifier.accuracy_test("accuracy_test.txt"))
print()
# add question to the file predict_data.txt for prediction
l=classifier.predict_from_file("predict_data.txt")
for x in l:
    print(x)
# ..... or simply write the query here to get the prediction
print()
print("label: " + classifier.predict("WRITE YOUR QUERY HERE TO GET THE LABEL"))


