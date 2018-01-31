import stackexchange
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.cm as cm
import numpy as np
import seaborn as sns
import random

# Set default Seaborn style
sns.set()

#Connect to SO site
so = stackexchange.Site(stackexchange.StackOverflow)

#Initialize lists to hold  values
tag_num = 20
tag_name = list()
tag_count = list()
tag_rank = list()

#get required values from SO object
for  idx, tag in enumerate(so.tags()):
    if idx >= tag_num:
        break    
    tag_rank.append(idx+1)
    tag_name.append(str(tag.name))
    tag_count.append(tag.count)
    


#Set bubble size
bubble_size = [int(i / np.std(tag_count)*5000) for i in tag_count]


def millions(x, pos=0):
    """Expects value and tick position
     returns string formatted for thousands and millions
     """
    #length of float value within thousands boundry
    if len(str(x)) <=8 :
        return '%1.1fK' % (x*1e-3)
    #length of float value within millions boundry
    return '%1.1fM' % (x*1e-6)

#Choose some random colors
colors=cm.rainbow(np.random.rand(2 * tag_num))
#colors = ['b', 'c', 'y', 'm', 'r']

#set formatter for Y axis
formatter = FuncFormatter(millions)

# Setfont dictionaries for plot title and axis titles
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} 
axis_font = {'fontname':'Arial', 'size':'14'}

#create scatter plot
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)
#sc = ax.scatter(tag_rank,tag_count,s=bubble_size,marker='o', color=colors)
l = list()
for n,c,r,s in zip(tag_name,tag_count,tag_rank,bubble_size):
    col = random.sample(colors,1)
    
    v1 = ax.scatter(r, c, marker='.', color=col,
                    alpha=0.5, s= s,)
    v = ax.scatter(r, c, marker='o', color=col,
                    alpha=0.5, label=n)
    l.append(v)    
    plt.annotate("#{}".format(r),xy=(r, c), ha="center", va="center")
    
    
    

#increase x, y axis limit 10% more
#ymin = ax.get_ylim()[0]
ymax = ax.get_ylim()[1]
xmax = ax.get_xlim()[1]
plt.ylim(0, 1.10 * ymax)
plt.xlim(0, xmax)

#label each bubble with rank and name
"""
for n,c,r,s in zip(tag_name,tag_count,tag_rank,bubble_size):
    plt.annotate("#{}".format(r),xy=(r, c), ha="center", va="center")
    plt.annotate(n ,xy=(r, c), xytext=(0,np.sqrt(s)/2.+5), 
                textcoords="offset points", ha="left", va="bottom")
"""
tag_data = (zip(tag_rank,tag_name,map(millions, tag_count)))
tag_data = map(lambda z: "#{} {} {}".format(z[0], z[1].title(), z[2]), tag_data)

plt.legend(l,
           tag_data,
           scatterpoints=1,
           loc='upper right',
           ncol=3,
           fontsize=12,
           title='Top Tags',
           numpoints=1,
           frameon=True,).get_frame().set_edgecolor("limegreen")
#plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Top Tags')
#Label axis
plt.ylabel('Tag Count', **axis_font)
plt.xlabel('Tag Rank', **axis_font)
plt.title('Top {} Tags By Counts'.format(tag_num), **title_font)
#plt.legend().get_frame().set_linewidth(2.0)
#plt.legend().get_frame().set_edgecolor("red")
plt.show()
