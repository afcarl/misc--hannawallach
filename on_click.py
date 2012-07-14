import numpy
from matplotlib import pyplot

def on_click(event):

    print 'Event: button=%d, x=%d, y=%d, xdata=%s, ydata=%s' % (event.button, event.x, event.y, event.xdata, event.ydata)

fig = pyplot.figure()
axes = fig.add_subplot(111)

axes.plot(numpy.random.rand(10))

cid = fig.canvas.mpl_connect('button_press_event', on_click)

pyplot.show()
