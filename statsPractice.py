#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 08:12:24 2017

@author: deaxman
"""
#%%
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
#%%multiply nxm mxd matrix
X=np.random.rand(4,5)
Y=np.random.rand(5,6)
Z=np.zeros((4,6))
for row in range(X.shape[0]):
    for col in range(Y.shape[1]):
        totalSum=0
        for i in range(X.shape[1]):
            totalSum+=X[row,i]*Y[i,col]
        Z[row,col]=totalSum
print(Z)
#%% Simulate a bivariate normal  
X1=np.random.multivariate_normal(np.array([1,2]),np.array([[1,0],[0,1]]),30)
X2=np.random.multivariate_normal(np.array([5,3]),np.array([[1,0],[0,1]]),30)
plt.scatter(np.concatenate([X1[:,0],X2[:,0]]),np.concatenate([X1[:,1],X2[:,1]]),c=np.concatenate([np.zeros((30,1)),np.ones((30,1))]))
#%%2 normal distributions two sets with same distributions and 2 with different
x1=np.random.normal(3,1,20)
x2=np.random.normal(1,3,20)

x3=np.random.normal(9,4,200)
x4=np.random.normal(10,4,200)

x5=np.mean(np.random.binomial(1,0.5,200))
x6=np.mean(np.random.binomial(1,0.7,200))

np.mean(x1)
np.mean(x2)
np.var(x1)
np.var(x2)





#%% confidence intervals on mean with formula
tval=stats.t.ppf(0.99,len(x1)-1)
print([np.mean(x1)-tval*np.sqrt(np.var(x1)/len(x1)),np.mean(x1)+tval*np.sqrt(np.var(x1)/len(x1))])

print([x5-tval*np.sqrt(x5*(1-x5)/len(x3)),x5+tval*np.sqrt(x5*(1-x5)/len(x3))])
#%% confidence intervals on mean with bootstrap
baseMean=np.mean(x1)
bootstrapSample=np.zeros((500,1))
for i in range(500):
    bootstrapSample[i]=baseMean-np.mean(np.random.choice(x1,len(x1)))
print([baseMean-tval*np.std(bootstrapSample),baseMean+tval*np.std(bootstrapSample)])
print(sorted(np.array(bootstrapSample))[4])
print(sorted(np.array(bootstrapSample))[-6])

#%% hypothesis test on mean with formula
tval=stats.t.ppf(0.9999999,len(x1)+len(x2)-2)
print(tval)
print((np.mean(x1)-np.mean(x2))/np.sqrt((np.var(x1)/len(x1))+(np.var(x2)/len(x2))))

#%% proportion hypothesis test  test against built in function
stats.t.cdf((x6-x5)/np.sqrt(((x5*(1-x5))/200)+((x6*(1-x6))/200)),400-2)



#%% hypothesis test on mean with bootstrap
bootDiff=np.zeros(50000)
for i in np.arange(50000):
    bootSamp=np.random.choice(np.concatenate([x1,x2]),len(x1)+len(x2))
    boot1=np.mean(bootSamp[0:len(x1)])
    boot2=np.mean(bootSamp[len(x1):])
    bootDiff[i]=boot1-boot2
np.mean((np.mean(x1)-np.mean(x2))<=bootDiff)


#%% hypothesis test on median with bootstrap

#%% generate some data!!!!!!!!! linear, (multiple) regression data   (3 different) 
x=np.random.normal(0,10,500)
y=3*x+np.random.normal(0,5,500)
plt.scatter(x,y)
msrList=np.zeros(10000)
totMSE=np.zeros(10000)
MSE=np.zeros(10000)
for i in range(10000):
    x=np.random.normal(0,10,500)
    y=3*x+np.random.normal(0,.2,500)
    slope, intercept, r_value, p_value, std_err=stats.linregress(x,y)
    msrList[i]=np.mean((slope*x-np.mean(y))**2)
    totMSE[i]=np.var(y)
    MSE[i]=np.var((slope*x)-y)
np.mean(msrList[i])
9*np.var(x)+.2


#%% run regressions fast
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

#%% t test on slope EQUATION

#%%
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
np.sqrt((np.sum((slope*x-y)**2)/(498))/np.sum((x-np.mean(x))**2))

slope-stats.t.ppf(.99,498)*np.sqrt((np.sum((slope*x-y)**2)/(498))/np.sum((x-np.mean(x))**2))
slope+stats.t.ppf(.99,498)*np.sqrt((np.sum((slope*x-y)**2)/(498))/np.sum((x-np.mean(x))**2))

allSlopes=np.zeros(1000)
for i in range(1000):
    idx=np.random.choice(len(y),len(y))
    bootx=x[idx]
    booty=y[idx]
    slopetmp, intercepttmp, r_valuetmp, p_valuetmp, std_errtmp=stats.linregress(bootx,booty)
    allSlopes[i]=slopetmp
np.std(allSlopes)
sorted(allSlopes)[9]
sorted(allSlopes)[-11]




#%% confidence and pred intervals

np.sqrt(np.sum((y-x*slope)**2)/498)*np.sqrt(1+(1/500)+((5-np.mean(x))**2)/np.sum((x-np.mean(x))**2))


#%% plot residuals and residual distributions, 
plt.plot(x,y-x*slope,'.')

plt.hist(y-x*slope)

#%%  check LINE assumptions




#%% Smirnoff test for normality (residuals plus created data)

stats.kstest(y-x*slope,'norm')

#%% probability plot for test of normality (residuals plus created data)
stats.probplot(y-x*slope,dist='norm',plot=plt)


#%% logistic regression
import statsmodels.api as sm
logReg=sm.OLS(y,x)
logReg.fit().summary()
#%% wald test






#%% poisson problems!


#%%  multidimensional regression


#%% run chi squared tests for normality on them

#%% add outliers check if influential! (use their data 11.1)

#%% anova test for variation from (decompose residuals) and r2 F test


#%% use statsmodels to fit multiple linear regression with data from course and look at pvalues answer stats questions

















#%%chi square tests problem (look up)


#%% try some monte carlo programming problems like sampling from distribution and estimating (find online)

#%% MIT/CMU stats problems!


#%% work with multidimensional regression data error bounds and multi dim error bounds



#%% blocking

#%% anova

#%% statistical power calculations t-test 2 sample


#%% bootstrap parameters for log reg

#%%poisson regression




#%% stepwise regression

#%% find autoregressive function for 1 dim and 2 dim

#%% plot ACF


#%%horvitz thompson estimators


#%% hypothesis tests!



#%% plot kl divergence between actual distribution and histogram over number of samples


#%%create multivariate and polynomial (combined) automatic regression


#%% https://onlinecourses.science.psu.edu/stat414/node/319



#%%
for n in [10,20,30,40,50,100,1000]:
    plt.plot([stats.binom.pmf(k,n,.5) for k in range(n)])


