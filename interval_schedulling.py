#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /Users/maion/OneDrive/Documentos/Documentos Felipe/programs/ruby/Python/PyCharmProjects/testes/interval_schedulling.py
# Project: /Users/maion/OneDrive/Documentos/Documentos Felipe/programs/ruby/Python/PyCharmProjects/testes
# Created Date: Sunday, November 17th 2019, 11:24:29 pm
# Author: Felipe Maion
# -----
# Last Modified: Mon Nov 18 2019
# Modified By: Felipe Maion
# -----
# Copyright (c) 2019 MaioneSys
# 
# 
# 
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###
import re


def combine(N, jobs):
    if not N:
        return [[]]
    if not jobs:
        return []

    head = [jobs[0]]
    tail = jobs[1:]
    new_comb = [ head + list_ for list_ in combine(N - 1, tail) ]

    return new_comb + combine(N, tail)

class Job:
    def __init__(self,jobID, start=None, end=None):
        self.jobID = jobID
        self.period =  [0 for i in range(24)]

        if start and end:
            self.startStr = start
            self.endStr = end
            self.start = self.convertHour(start)
            self.end = self.convertHour(end)
        #create the list for the period the job will be running:
            self.runningPeriod()
    
    def convertHour(self,hourStr):
        hour = 0
        # Check if the string has an 'p' or 'P' in it, if so, it is evening add 12 hours.
        evening = True if 'p' in re.sub(r'[0-9]+','',hourStr) or 'P' in re.sub(r'[0-9]+','',hourStr) else False
        # Get the raw hour(remove strings): 6p.m = 6; 5a.m = 5:
        rawHour = re.sub(r'[aA-zZ]+','',hourStr) 
        if evening: 
            hour = int(rawHour) + 12 
        else: 
            hour = int(rawHour)
        return hour

    def runningPeriod(self):
        if self.start <= self.end:
            for hour,_ in enumerate(self.period):
                # Set the working period of the job as 1.
                self.period[hour] = 1 if hour + 1 >= self.start and hour + 1 <= self.end else 0
        if self.start > self.end:
            for hour,_ in enumerate(self.period):
                # Set the working period of the job as 1 for the job that ends in another day.
                self.period[hour] = 1 if hour + 1 >= self.start or hour + 1 <= self.end else 0                # self.period[hour] = 1 if hour + 1 <= self.end else 0
        return self.period
    # Define the add of two jobs, ex: [1,0,...,1] + [1,1,...,0] = [2,1,...,1]:    
    def __add__(self, job):
        self.period = [sum(x) for x in zip(job.period, self.period)]
        return self
    def __radd__(self, job):
        self.period = [sum(x) for x in zip(job.period, self.period)]
        return self
    # def what should be printed when print(job) is called:
    def __str__(self):
        return str("("+ self.startStr + " ," +  self.endStr + ")")



class Schedulling:
    def __init__(self, jobs):
        self.bestOutCome = []
        self.jobs = jobs
        self.maxRunningTime = 0
        self.schedule()

    def allCombinations(self):
        allPossibilities = []
        # Do all combinations for the jobs
        # exemple:
        # > self.allCombinations([1,2,3])
        # returns: [[[1], [2], [3]], [[1, 2], [1, 3], [2, 3]], [[1, 2, 3]]]
        for n in range(1, len(self.jobs) + 1): 
            allPossibilities.append(combine(n,self.jobs)) 
        return allPossibilities

    def schedule(self):
        possibleSollutions = {}
        bestSolutions = {}
        getCombinations = self.allCombinations()
        for positionGroup, group in enumerate(getCombinations):
            for positionPossibilities, possibilities in enumerate(group):
                temp_Job = Job(0)
                for jobs in possibilities:
                    temp_Job += jobs
                # PossibleSollutions have the key as the indexes of the getCombinations:
                possibleSollutions[str(positionGroup) + " ," + str(positionPossibilities)] = temp_Job.period
        
        for key, possibility in possibleSollutions.items():
            # Filter only the sollutions that jobs don't overlap:
             if all(i <= 1 for i in possibility):
                 bestSolutions[key] = possibility

        # Find the combinations that has the maximum amount of period running:
        itemMaxValue = max(bestSolutions.items(), key=lambda x: sum(x[1]))
        self.maxRunningTime = sum(itemMaxValue[1])
        listOfSchedules = list()
        # Iterate over all the items in dictionary to find keys with max value
        # It will find all the combinations that has the maximum period running:
        for key, value in bestSolutions.items():
            if value == itemMaxValue[1]:
                listOfSchedules.append(key)
        
        for i, solution in enumerate(listOfSchedules):
            # Split the KEY value of the dictionary to get the indexes.
            indexes = listOfSchedules[i].split(",")
            # Now we must get the objects from getCombinations according to the indexes.
            self.bestOutCome.append(getCombinations[int(indexes[0])][int(indexes[1])])
        # Return the best solutions as a list of Objects Job:
        return self.bestOutCome

    def __str__(self):
        # Print the best schedullings even if there are more than one option:

        my_str = ""
        
        for solution in self.bestOutCome:
            myPeriod = ""
            myJobs = []
            for jobs in solution:
                # That's necessary to get the time as string from the Job object:
                myPeriod += str(jobs)
                myJobs.append(str(jobs.jobID))
            my_str += "Max running time: " + str(self.maxRunningTime) + "hours. Jobs: " + str(myJobs) + " with time:"+ str(myPeriod)+ "\n"
        return my_str


# Setting the working example:
#Enter1 6pm 6am
#Enter2 9pm 4am
#Enter3 3am 2pm
#Enter4 1pm 7pm
job1 = Job(1,'6pm','6am')
job2 = Job(2, '9pm','4am')
job3 = Job(3, '3am', '2pm')
job4 = Job(4, '1pm','7pm')
job5 = Job(5, '1pm', '7pm')
jobs = [job1,job2,job3, job4, job5]
sc = Schedulling(jobs)
print(sc)
