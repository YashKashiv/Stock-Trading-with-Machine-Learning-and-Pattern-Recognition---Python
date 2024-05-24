import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime
from functools import reduce
import time

date, bid, ask = np.loadtxt('GBPUSD/GBPUSD1d.txt', unpack=True,
                            delimiter=',',
                            converters={0: lambda x: mdates.date2num(datetime.strptime(x.decode('utf-8'), '%Y%m%d%H%M%S'))})

patternAr = []
performanceAr = []

def percentChange(startPoint, currentPoint):
    return ((float(currentPoint) - startPoint) / abs(startPoint)) * 100.0

def patternStorage():
    startTime = time.time()

    avgLine = (bid + ask) / 2
    x = len(avgLine) - 30
    y = 11
    
    while y < x:
        pattern = []
        p1 = percentChange(avgLine[y-10], avgLine[y-9])
        p2 = percentChange(avgLine[y-10], avgLine[y-8])
        p3 = percentChange(avgLine[y-10], avgLine[y-7])
        p4 = percentChange(avgLine[y-10], avgLine[y-6])
        p5 = percentChange(avgLine[y-10], avgLine[y-5])
        p6 = percentChange(avgLine[y-10], avgLine[y-4])
        p7 = percentChange(avgLine[y-10], avgLine[y-3])
        p8 = percentChange(avgLine[y-10], avgLine[y-2])
        p9 = percentChange(avgLine[y-10], avgLine[y-1])
        p10 = percentChange(avgLine[y-10], avgLine[y])

        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]

        try:
            avgOutcome = reduce(lambda a, b: a + b, outcomeRange) / len(outcomeRange)
        except Exception as e:
            print(str(e))
            avgOutcome = 0

        futureOutcome = percentChange(currentPoint, avgOutcome)

        pattern.extend([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])

        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        
        y += 1
    
    endTime = time.time()
    print(len(patternAr))
    print(len(performanceAr))
    print('Pattern storing took:', endTime - startTime)

def graphRawFX():
    fig = plt.figure(figsize=(10, 7))
    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan=40, colspan=40)
    ax1.plot(date, bid, label='Bid')
    ax1.plot(date, ask, label='Ask')
    
    percent_changes = [percentChange(ask[0], ask[i]) for i in range(len(ask))]
    ax1.plot(date, percent_changes, 'r', label='Ask % Change')

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    plt.grid(True)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask - bid), facecolor='g', alpha=0.3, label='Spread')

    plt.subplots_adjust(bottom=0.23)
    ax1.legend(loc='upper left')
    ax1_2.legend(loc='upper right')

    plt.show()

patternStorage()
graphRawFX()