import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime
from matplotlib import style

style.use("ggplot")

def graphRawFX():
    date, bid, ask = np.loadtxt('GBPUSD/GBPUSD1d.txt', unpack=True,
                                delimiter=',',
                                converters={0: lambda x: mdates.date2num(datetime.strptime(x.decode('utf-8'), '%Y%m%d%H%M%S'))})

    fig = plt.figure(figsize=(10, 7))

    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan=40, colspan=40)
    ax1.plot(date, bid, label='Bid')
    ax1.plot(date, ask, label='Ask')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    plt.grid(True)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, ask - bid, facecolor='g', alpha=0.3, label='Spread')

    plt.subplots_adjust(bottom=0.23)
    
    ax1.legend(loc='upper left')
    ax1_2.legend(loc='upper right')

    plt.show()

graphRawFX()