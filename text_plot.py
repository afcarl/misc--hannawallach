import csv
from urllib2 import urlopen
from itertools import islice
from pylab import axis, infty, show, subplot, text
import pandas


def plot_without_pandas():

    min_population = infty
    max_population = 0

    data = []

    for row in islice(csv.reader(urlopen('http://datasets.flowingdata.com/crimeRatesByState2005.csv')), 2, None):

        # fields are state, murder, forcible_rape, robbery, aggravated_assault, burglary, larceny_theft, motor_vehicle_theft, population

        data.append([row[i] for i in [0, 1, 5, 8]])

        min_population = min(int(row[8]), min_population)
        max_population = max(int(row[8]), max_population)

    scale = (max_population - min_population) / 20.0

    axes = subplot(111)

    for state, murder, burglary, population in data:
        text(murder, burglary, state, size=(int(population) - min_population) / scale + 8, horizontalalignment='center')

    axis([0, 11, 200, 1280]) # DC is an outlier!

    axes.xaxis.set_visible(False)
    axes.yaxis.set_visible(False)

    show()


def draw_text(row, scale, min_population):

    text(row['murder'], row['burglary'], row['state'], size=(row['population'] - min_population) / scale + 8, horizontalalignment='center')


def plot_with_pandas():

    data = pandas.read_csv(urlopen('http://datasets.flowingdata.com/crimeRatesByState2005.csv'), skiprows=[1])

    min_population = data['population'].min()

    scale = (data['population'].max() - min_population) / 20.0

    axes = subplot(111)

    data.apply(draw_text, args=(scale, min_population), axis=1)

    axis([0, 11, 200, 1280]) # DC is an outlier!

    axes.xaxis.set_visible(False)
    axes.yaxis.set_visible(False)

    show()


if __name__ == '__main__':

    #plot_with_pandas()
    plot_without_pandas()
