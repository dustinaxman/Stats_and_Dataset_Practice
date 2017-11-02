#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 11:57:12 2017

@author: deaxman
"""
#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%%
slpdbFrameSVM=[0.865901382728933,0.741708542713568, 0.909443269908386,0.817056114704885,0.921623253406935]
HCIdbFrameSVM=[0.750000000000000, 0.786802030456853, 0.697841726618705, 0.739656614355291, 0.805794460641399]
slpdbGLOBSVM=[0.88219,   0.77200,   0.915,   (2*0.77200*0.915/(0.915+0.77200)),  0.930127]
HCIdbGLOBSVM=[0.78215,   0.81025,  0.72013   ,   (2*0.72013*0.81025/(0.72013+0.81025)), 0.8232]

slpdbWSegSVM=[0.89552,   0.7741,   0.921,   2*0.7741*0.921/(0.7741+0.921),  0.935488]
HCIdbWSegSVM=[0.7917,   0.80114,  0.7364   ,   2*0.80114*0.7364/(0.80114+0.7364), 0.83153]

slackRange=[1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]

slpdbFrameSVMF1=[0.817056114704885,0.74,0.53,.46,.39,.32,.301,.2707,.2818,.22,.25]
slpdbGLOBSVMF1=[0.8374392412566686,.77,.39,.41,.31,0,.25,0.15,0,0,.21]
slpdbWSegSVMF1=[.7933,.818,0.8411847,.83614,.8114,.8125,.7916,.7712,.78,734,.6814]
fig = plt.figure()
ax = plt.axes()
ax.set_xlabel("Bound Length to True Length Ratio")
ax.set_ylabel("F1 Score")
ax.title('F1 Score Over Different Labeling Slacks')
ax.plot(slackRange,slpdbFrameSVMF1,label='Framewise SVM')
ax.plot(slackRange,slpdbGLOBSVMF1,label='Global-SVM')
ax.plot(slackRange,slpdbWSegSVMF1,label='Weakly Supervised Seg-SVM')

HCIdbFrameSVMF1=[0.739656614355291,.6192,.5811,.5211,.3418,.4480,.1251,.2253,.2116]
HCIdbGLOBSVMF1=[0.7625365366771651,.5718,.5988,.5112,.4213,.3127,.2153,0,.1521,0,0]
HCIdbWSegSVMF1=[0.741,0.7668,0.767407021605942,.7551,.7612,.7419,.7501,.7335,.7311,.6814,.6612]
fig,ax=plt.figure()
ax.set_xlabel("Bound Length to True Length Ratio")
ax.set_ylabel("F1 Score")
ax.title('F1 Score Over Different Labeling Slacks')
ax.plot(slackRange,HCIdbFrameSVMF1,label='Framewise SVM')
ax.plot(slackRange,HCIdbGLOBSVMF1,label='Global-SVM')
ax.plot(slackRange,HCIdbWSegSVMF1,label='Weakly Supervised Seg-SVM')

#%%
kValue=[1,2,3,4,5,6,7,8]
#generate fp and fn and total error graph as we choose k different from 3 for SLPDB
slpdbtotError=[.71115,.7481,0.84552,.8217,.8110,.7653,.7317,.7268]
slpdbfp=[]
slpdbfn=slpdbtotError-slpdbfp
fig,ax=plt.figure()
ax.set_xlabel("K")
ax.set_ylabel("Percentage Error")
ax.title('Error Rates by K Value')
ax.plot(kValue,slpdbtotError,label='Total Error')
ax.plot(kValue,slpdbfp,label='False Positive Rate')
ax.plot(kValue,slpdbfn,label='False Negative Rate')
#generate fp and fn and total error graph as we choose k different from 3 for HCIDB
hcidbtotError=[.7124,.7316,0.76118,.7581,.7519,.7320,.71,.7011]
hcidbfp=[]
hcidbfn=hcidbtotError-hcidbfp
fig = plt.figure()
ax = plt.axes()
ax.set_xlabel("K")
ax.set_ylabel("Percentage Error")
ax.title('Error Rates by K Value')
ax.plot(kValue,hcidbtotError,label='Total Error')
ax.plot(kValue,hcidbfp,label='False Positive Rate')
ax.plot(kValue,hcidbfn,label='False Negative Rate')
