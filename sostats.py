import stackexchange
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
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
colors=cm.rainbow(np.random.rand(tag_num))

#Set bubble size
bubble_size = [(float(i) / tag_count[0])*1000  for i in tag_count]

#Convert tag to 1k notation
#y_tick_values = [("{}k".format(v)) for v in tag_count]
millnames = ['',' Thousand',' Million',' Billion',' Trillion']
def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

y_tick_values = [millify(v) for v in tag_count]

#create scatter plot
fig, ax = plt.subplots()
ax.scatter(tag_rank,tag_count,s=bubble_size,color=colors)
#plt.scatter(tag_rank,tag_count,color=colors)

#label each bubble
for i in range(tag_num):
    plt.annotate(tag_name[i],xy=(tag_rank[i], tag_count[i]))



#Label axis
#plt.tight_layout()
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8
plt.xlabel('Tag Count')
plt.ylabel(' Tag Rank')
plt.title('Top Ten Tags By Counts',y=1.05)
#plt.yticks(tag_count,y_tick_values)
#plt.grid(True)
#plt.margins(0.02) # Keeps data off plot edges
#plt.setp(ax.get_yticklabels(), rotation=30, horizontalalignment='right')
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.show()

#Look inside object
#dir(t)
