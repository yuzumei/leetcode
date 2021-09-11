import random
import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
def aucauc():
    x=[]
    y=[]
    for _ in range(100):
        x.append(random.randint(0,1))
        y.append(random.random())
    fpr, tpr, thresholds = roc_curve(x, y, pos_label=1)
    print("-----sklearn:",auc(fpr, tpr))
    sample0=[]
    sample1=[]
    for i,num in enumerate(x):
        if num==0:
            sample0.append(i)
        else:
            sample1.append(i)
    allsample=len(sample0)*len(sample1)
    sumnum=0
    for num0 in sample0:
        for num1 in sample1:
            if y[num1]>y[num0]:
                sumnum+=1
            elif y[num1]==y[num0]:
                sumnum+=0.5
    return sumnum/allsample

if __name__=='__main__':
    print(aucauc())