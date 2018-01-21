import stackexchange
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.cm as cm
import numpy as np
import math
import seaborn as sns

so = stackexchange.Site(stackexchange.StackOverflow)

# Set default Seaborn style
sns.set()

#Print top 10 tags and their count
tag_num = 10
tag_name = list()
tag_count = list()
tag_rank = list()

for  idx, tag in enumerate(so.tags()):
    if idx >= 10:
        break
    tag_rank.append(idx+1)
    tag_name.append(tag.name)
    tag_count.append(tag.count)
    
#Choose some random colors
colors=cm.rainbow(np.random.rand(2 * tag_num))

#Set bubble size
bubble_size = [(float(i) / tag_count[0])*1000  for i in tag_count]


def millions(x, pos):
    'The two args are the value and tick position'
    if len(str(x)) <=8 :
        return '%1.1fK' % (x*1e-3)
    
    return '%1.1fM' % (x*1e-6)

formatter = FuncFormatter(millions)

#create scatter plot

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)
ax.scatter(tag_rank,tag_count,s=bubble_size,marker='o', color=colors)
#ax.scatter(tag_rank,tag_count,s=bubble_size,marker='o', c=bubble_size )
#ax.scatter(tag_rank,tag_count,s=bubble_size, color=colors)

#label each bubble
for i in range(tag_num):
    plt.annotate(tag_name[i],xy=(tag_rank[i], tag_count[i]),xycoords=tag_name[i])


#Label axis
#plt.tight_layout()
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8
plt.xlabel('Tag Count')
plt.ylabel(' Tag Rank')
plt.title('Top Ten Tags By Counts',y=1.05)
plt.show()

#Look inside object
#dir(t)
