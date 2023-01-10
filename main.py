import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter
@FuncFormatter
def tick_formatter(val, pos):
    """I convert graph units to be in the 'thousands'
    
    arguments
    val - the value at the tickmark
    pos - the position of the tickmark                  
    """
    return f'{int(val/10000)}K'       
df = pd.read_excel('data/Total_Arrests_by_County_2020.xlsx')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(25, 15))
df = df.sort_values(by='County')
df.plot(kind='barh', x='County', y='Robbery', ax=ax1, color='#434e52')
ax1.set(title='Florida Annual 2020 Crime Report By County Involving Robbery', xlabel='Robbery Arrests')
ax1.legend().set_visible(False)
plt.sca(ax1) 
plt.xticks(rotation=75)
df.plot(kind='barh', x='County', y='Population', ax=ax2)
ax2.set(title='Arrests For Robbery 2020', xlabel='Population')
ax2.xaxis.set_major_formatter(FuncFormatter(tick_formatter))
plt.show()
