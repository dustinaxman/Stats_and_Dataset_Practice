import numpy as np
import pandas as pd

s=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
print(s)
print(s.index)
#%%
tstDict={2:6.,3:4.,1:2}
dictSeries=pd.Series(tstDict,index=[1,3,2])
print(dictSeries)
#%%
a=[1,2,3,4,5,6]
npA=np.array(a)
print(npA[npA>3])
#%%
df=pd.DataFrame({'one': pd.Series([1,2,3],index=['a','b','c']),'two': pd.Series([1,2,3,4],index=['a','b','c','d'])})
df['one']
df['three'] = df['one'] * df['two']
df
dust=df['three']
df['three']=pd.Series([1,2,3,4],index=['a','b','c','d'])
df
#%%
df
df[5:6]
left = pd.DataFrame({'key1': ['foo', 'foo'],'key2': ['foo2', 'foo2'], 'lval': [1, 2]})

right = pd.DataFrame({'key1': ['foo', 'foo'],'key2': ['foo2', 'foo2'], 'rval': [4, 5]})

print(pd.merge(left,right,on=['key1','key2']))

#%%
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                            'foo', 'bar', 'foo', 'foo'],
                      'B' : ['one', 'one', 'two', 'three',
                            'two', 'two', 'one', 'three'],
                    'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
#%%
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts.plot()
df=pd.DataFrame({'A': ts,'B': ts*2})
#%%
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 10)
y = x ** 2
fig = plt.figure()

axes = fig.add_axes([0,0,1,1]) # left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');
#%%
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls


x = np.linspace(0, 5, 10)
y = x ** 2
fig = plt.figure()

axes = fig.add_axes([0,0,1,1]) # left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');



py.iplot_mpl(fig)





