# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


N = 5
lecture = (2, 4, 4, 3, 0)
lab = (2, 2, 3, 0, 2)
lectureStd = (.5, 0, 0, 0, 0)
labStd = (1, 0, 0, 0, 0)
ind = np.arange(N)    # the x locations for the groups
width = .75       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, lecture, width, color='#d62724', yerr=lectureStd)
p2 = plt.bar(ind, lab, width, bottom=lecture, yerr=labStd)

#p1 = plt.bar(ind, lecture, width, color='#d62728')
#p2 = plt.bar(ind, lab, width, bottom=lecture)


plt.ylabel('Hours')
plt.title('Classes by time and type')
plt.xticks(ind, ('M', 'T', 'W', 'T', 'F'))
plt.yticks(np.arange(0, 8, 1))
plt.legend((p1[0], p2[0]), ('Lecture', 'Lab'))

plt.show()
#Add more comments for clarification
