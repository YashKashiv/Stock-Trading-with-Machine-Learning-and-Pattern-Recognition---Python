'''import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
style.use("ggplot")




def graphRawFX():
    date,bid,ask = np.loadtxt('GBPUSD/GBPUSD1d.txt', unpack=True,
                              delimiter=',',
                              converters={0:mdates.mdates.date2num('%Y%m%d%H%M%S')})

    fig=plt.figure(figsize=(10,7))

    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
    plt.subplots_adjust(bottom=.23)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    plt.grid(True)
    plt.show()

graphRawFX()'''


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
from datetime import datetime

style.use("ggplot")

def graphRawFX():
    date, bid, ask = np.loadtxt(
        'GBPUSD/GBPUSD1d.txt',
        unpack=True,
        delimiter=',',
        converters={0: lambda x: mdates.date2num(datetime.strptime(x.decode('utf-8'), '%Y%m%d%H%M%S'))}
    )

    fig = plt.figure(figsize=(10, 7))

    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan=40, colspan=40)
    ax1.plot(date, bid, label='Bid')
    ax1.plot(date, ask, label='Ask')

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    plt.subplots_adjust(bottom=.23)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    plt.grid(True)
    plt.legend()
    plt.show()

graphRawFX()