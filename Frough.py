# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:58:49 2019

@author: Sutapa
"""

import copy
""""U=[]
A=[]
n=int(input("Enter the number of objects:"))
m=int(input("Enter the number of attributes:"))
def createList():
#Creating the list of objects
    for i in range(n):
        U.append(input("Enter the Object name:"))
    print(U)
        
#Creating the list of attributes
    for j in range(m):
        A.append(input("Enter the attribute name: "))
    print(A)
        """
import csv
#import numpy as np

with open('dogs.csv') as f:
    reader = csv.reader(f, delimiter=',', skipinitialspace=True)
    data=list(reader)
    n=len(data)#rows
    first_row = data[0]
    m = len(first_row)#columns
    
    A=[('a'+str(i)) for i in range(m)]

#Creating the I=(U,A) table
"""Val=[[]for i in range(n)]

def createI():
    for i in range(n):
        for j in range(m):
            Val[i].append(input(f"Enter the attribute value for Object-{U[i]} Attribute-{A[j]}:"))

    print(f"Val=",Val)
"""
#Creating the discernibility matrix    
Dis=[[]for i in range(n-1)]   

def createDiscernibilityMatrix():
     
    for i in range(n-1):
        for k in range(i+1,n):
            a=[]
            for j in range(m):
                if(data[i][j]!=data[k][j]):
                    a.append(A[j])
                else:
                    continue
            Dis[i].append(a)
    print(Dis)        

#Creating S which is list of all cells ,corresponding to the non empty cells of Dis
S=[]

def createS():
    for row in Dis:
        if (row): 
            for cell in row:
                if(cell):
                    S.append(cell)
             
    #print("S before sorting:",S)
    S.sort(key=len)
    #print("S after sorting:",S)
    print(f"S done:)")

#Creating T list from S    
T=[]

def alternate(S):
    t=[]
    c=0
    v=[0 for cell in S]
    while(c!=len(S)):
        if v[c]==0:
            t.append(S[c])
            v[c]=1
            k=S[c]
            i=0
            for cell in S:
                if cell==k:
                    v[i]=1
                else:
                    count=0
                    for element in k:
                        if element in cell:
                            count=count+1
                    if(count==len(k)):
                        v[i]=1
                i=i+1
            c=c+1
        else:
            c=c+1
    #print("T=",T)
    return t
    
def modifyList():
    for eachList in T:
        i=1
        l=len(eachList)
        count=1
        while(count<l):
            eachList.insert(i,'+')
            i=i+2
            count=count+1
            
#Performing SumOfProducts on given two list

def mulList(Aa,B):
    C=[]
    for a in Aa:
        if a!='+': #condition to use only if modifyList function is used (for output formatting)
            for b in B:
                if b!='+':#condition to be usedonly of modifyList funtion is used (for output formatting)
                    if b in Aa:
                        C.append(b)
                    elif b in a:
                        C.append(a)
                    else:
                        if(type(a)==list):
                            k=copy.deepcopy(a)
                            k.append(('.'+b))
                            C.append(k)
                        else:
                            C.append((a+'.'+b))
                else:
                    C.append(b)
        else:
            C.append(a)
    return C



MinReduct=[]



#Simplifying SumOfProducts and Finding the set of reducts as well as the minimum reduct
def combine(T):
    Com=copy.deepcopy(T[0])
    for eachlist in T:
        if(eachlist!=T[0]):
            Com=mulList(Com,eachlist)
            #print(Com)
    #print("Final list",Com)
    s=set(Com)
    #print(s)
    #print(type(s))
    FL=list(s)
    FL.sort(key=len)
    #FL.remove('+')
    #print(FL)
    Reduct=alternate(FL)
    print(f"Reduct(s)=",Reduct)
    MinReduct=[[element]for element in Reduct]
    MinReduct=min(MinReduct,key=len)
    print(f"MinReduct=",MinReduct)
    
#compiling the program
def main():
    #createList()
    #createI()
    createDiscernibilityMatrix()    
    createS()                
    T=alternate(S)
    print(f"T=",T)
    combine(T)
    