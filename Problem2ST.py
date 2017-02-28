#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:22:32 2017

@author: shawnthomas
"""
"""
Homework 1- Problem 2
Grow a DLA cluster from the bottom.
Walks emerge from the top and and stick to the bottom.

"""

'''
Libraries
'''
import numpy as np
import matplotlib.pyplot as p  

'''
Global variables
'''

a = np.zeros((200, 200)) #array
stepChoices=[[-1,0],[0,-1],[1,0],[0,1]] #list of possible steps
a[199,0:199]=1 #sets the bottom as the sticking point for the walkers
startPos=[]
im = p.imshow(a, cmap='viridis')


'''
Functions
'''

def top2bottomDLA():
    '''
    Local variables are only defined in the function itself
    '''
    walkerLength=0
    
    p.ion()
    startX=np.random.randint(0,200) # this chooses a random integer for startX from 0-200
    startAx=0 # constricts walker to generate from top of figure
   
    if startAx==0: startPos=np.array([0,startX]) #creates a starting position for a walker

    
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
'''
Program Execution
'''
#We want 1000 walkers to stick to the structure
for i in range(0,3000): # sets there to be 3000 walkers
    print "Walker running: "+str(i) # shows in the console which walker is running currently
    walkerLength=top2bottomDLA()  
    print "Total Length: "+str(walkerLength)
          

# make a figure of the size of the array
p.figure(2)
# show the array
p.imshow(a, cmap='viridis')
p.show()