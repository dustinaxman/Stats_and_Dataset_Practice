#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:43:02 2017

@author: deaxman
"""
#%%
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self,df):
        super().__init__()
        self.title = 'DataFrame Visualization'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.df=df
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createTable()
 
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.datatable) 
        self.setLayout(self.layout) 
 
        # Show widget
        self.show()
 
    def createTable(self):
       # Create table
        self.datatable = QTableWidget()
        
        self.datatable.setHorizontalHeaderLabels(list(self.df))
#        self.datatable.horizontalHeader().setVisible(True)
        self.datatable.setColumnCount(len(self.df.columns))
        self.datatable.setRowCount(len(self.df.index))
        for i in range(len(self.df.index)):
            for j in range(len(self.df.columns)):
                self.datatable.setItem(i,j,QTableWidgetItem(str(self.df.iget_value(i, j))))
        self.datatable.setHorizontalHeaderLabels(list(self.df))
        # table selection change
        self.datatable.doubleClicked.connect(self.on_click)
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
def showTable(df):
    app = QApplication(sys.argv)
    
    ex = App(df)
    sys.exit(app.exec_())

#%%
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
planets = sns.load_dataset('planets')
titanic = sns.load_dataset('titanic')
exercise = sns.load_dataset('exercise')
#%%
planets.head
titanic.head
classMapping={'First':1,'Second':2,'Third':3}
titanic['testClass']=titanic['class'].apply(lambda category: classMapping[category])


newtitanic=titanic.dropna()
newtitanic.loc[:,'ageGroups']=pd.qcut(newtitanic['age'],10)
malesurv=newtitanic[newtitanic['sex']=='male'].groupby('ageGroups')['survived'].mean()
femalesurv=newtitanic[newtitanic['sex']=='female'].groupby('ageGroups')['survived'].mean()
pd.DataFrame({'male':malesurv,'female':femalesurv})
plt.figure()
newtitanic.pivot_table('survived',index='ageGroups',columns='sex',aggfunc='mean').plot()
plt.figure()
sns.violinplot("sex","age", data=newtitanic,
               palette=["lightblue", "lightpink"])

plt.figure()
sns.distplot(newtitanic['age'], kde=False);

#%%
#showTable(exercise)
exercise.groupby(['diet','kind'])['pulse'].aggregate([np.mean,np.std])
exercise['pulseGroup']=pd.qcut(exercise['pulse'],10,labels=False)
exercise.groupby('id')['pulseGroup'].hist(alpha=.2)