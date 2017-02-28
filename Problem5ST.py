#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 07:34:04 2017

@author: shawnthomas
"""
"""
Homework 1- Problem 5
Fractal Dimension of DLA Clusters
"""

'''
Libraries
'''
import numpy as np
import matplotlib.pyplot as p
import csv
import math

'''
Global Variables
'''

# array for walker
a = np.zeros((200, 200), dtype='float') # creates 200 by 200 array of zeros (floats)

stepChoices = [[0,1],[0,-1],[-1,0],[1,0]] #possible steps
a[100,100]=1 #initial point
startPos=[] 
totalsteps=[]
clustersize = 0
im = p.imshow(a, cmap='viridis')


'''
Functions
'''

def centerDLA():
    '''
    Local variables are only defined in the function itself
    '''
    walkerLength=0
    
    p.ion()
    startX=np.random.randint(0,200) # this chooses a random integer for startX from 0-200
    startAx = np.random.randint(0,4) # Choose a side
    #based on side chosen in line 43 chooses a startPos
    if startAx == 0:
        startPos = np.array([0,startX])
    elif startAx == 1:
        startPos = np.array([199,startX])
    elif startAx == 2:
        startPos = np.array([startX,0])
    elif startAx == 3:
        startPos = np.array([startX,199])
    walkerLength=0
    # Walk as long no taken position is reached
    while a[startPos[0],startPos[1]] == 0:
        walkerLength+=1
        step=np.array(stepChoices[np.random.randint(0,4)])
        #Randomly choose a step to go ()
        startPos=startPos+step
        #Add the step to the current position
        if startPos[0]>=0 and startPos[1]>=0 and startPos[0]<200 and startPos[1]<200:
             # If the new position is within the array
            # If the current position is already taken we want to extend the structure
            if a[startPos[0],startPos[1]] > 0: # Remember we initialized our drawing array with zeros. 
                # Set the last position as taken aka stick to the structure. Here we set the value in the array to the distance from the center
                a[(startPos-np.array(step))[0],(startPos-np.array(step))[1]]=np.linalg.norm(np.array([(startPos-np.array(step))[0],(startPos-np.array(step))[1]])-np.array([200,200]),2)
                # refresh the image
                im.set_data(a) # set the data
                p.draw() # draw the image
                p.pause(0.001) # give the computer time to draw
        else:
            # else go 1 step back and choose again
            startPos=startPos-np.array(step)
        p.ioff()
    return walkerLength
    
def diacircle(arr):
    # find diameter of enclosing circle
    diamax = 0
    dlastructure = np.where(arr > 0) # np.where selects values from array with given condition
    for i in zip(dlastructure[0], dlastructure[1]):
        for j in zip(dlastructure[0], dlastructure[1]):
            dia = np.linalg.norm(np.array(i)-np.array(j),2) # calculate distance between points
            if diamax < dia:
                diamax = dia
    return diamax
    
def saveListToFile(wll, path): # Note we can give it another name to be used in the function 
    with open(path, 'wb') as csvfile: # open file
        writer = csv.writer(csvfile) # create a write variable
        for i in wll:  # for loop through the list  
            writer.writerow([i]) # Use build in writer function
    csvfile.close()  # CLOSE THE FILE  !!! Common error source
    
'''
Program Execution
'''

for i in range(0,500): # sets there to be 3000 walkers
    print "Walker running: "+str(i) # shows in the console which walker is running currently
    walkerLength=centerDLA()  
    totalsteps.append(walkerLength)
    print "Total Length: "+str(walkerLength)
    clustersize += 1
    
clusterdia = diacircle(a)

# s=r^d rewritten as log(r)s = d
fractdim = math.log(clustersize,(clusterdia/2))

print "cluster diameter: " + str(clusterdia)
print "cluster size: " + str(clustersize)
print "fractal dimension: " + str(fractdim)

# Save files
saveListToFile(totalsteps,'walkerList.csv')
saveListToFile([clusterdia],'./Diameter.csv')

# make a figure from the array
p.figure(2)
# show the array as an image
p.imshow(a, cmap='viridis') 
p.show()

