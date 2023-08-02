# Z_plot.py

# Created 1 NOV 2018
#   by Zaki Rucker
#   with Alex Hardt and Corey Lutton
#   for CS 4558 Network Traffic Analysis                    

# Reference:
#   https://matplotlib.org/examples/pie_and_polar_charts/pie_demo_features.html
#   https://matplotlib.org/gallery/pie_and_polar_charts/pie_and_donut_labels.html
#   https://stackoverflow.com/questions/19852215/how-to-add-a-legend-to-matplotlib-pie-chart
#   https://matplotlib.org/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py


# A program to produce the output for an analysis of the additive effect of
# local network congestion on the RTT latency of the destination servers.


import matplotlib.pyplot as plt
import numpy as np


#open ('') as data_file:


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
#plt.figure(1)
labels = 'local gateway', 'Yahoo'
sizes = [1.6, 58.9]
explode = (0.1, 0)

fig1, ax1 = plt.subplots()
#patches, texts, foo = ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=135)
patches, texts, foo = ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=False, startangle=135)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('Total RTT')
plt.legend(patches, labels, loc="best")

plt.show()


# Stacked bar chart
#plt.figure(2)
N = 5
local = (1.1, 1.3, 1.30, 1.35, 10.27)
destination = (58.25, 19.32, 13.34, 17.20, 60.25)
localStd = (2, 3, 4, 1, 2)
dstStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, local, width, yerr=localStd)
p2 = plt.bar(ind, destination, width,
             bottom=local, yerr=dstStd)

plt.ylabel('Scores')
plt.title('RTT to destination')
plt.xticks(ind, ('Google', 'Yahoo', '...', '...', '...'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Local Gateway', 'Destination'))

plt.show()
