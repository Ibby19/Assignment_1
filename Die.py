#!/usr/bin/env python
# coding: utf-8

# In[2]:


#class definition for an n-sided die

#import packages
import random


class MSdie(object): 
  #constructor here

    def __init__( self ):
        self.sides = 6
        self.roll()

  #define classmethod 'roll' to roll the MSdie
    
    def roll( self ):
        
        self.value = 1 + random.randrange(self.sides)
        
        return self.value
    
  #define classmethod 'getValue' to return the current value of the MSdie
    
    def getValue(  self ):
        
        return self.value

  #define classmethod 'setValue' to set the die to a particular value
    #def setValue(self):
def roller():
    r1 = MSdie()
    
    for n in range (4):
        print(r1.roll())

roller()

