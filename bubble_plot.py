import csv
from urllib2 import urlopen
from itertools import islice
from pylab import axis, scatter, show, sqrt, text, xlabel, ylabel
import pandas

def plot_without_pandas():

    data = []

    for row in islice(csv.reader(urlopen('http://datasets.flowingdata.com/crimeRatesByState2005.csv')), 2, None):

        # fields are state, murder, forcible_rape, robbery, aggravated_assault, burglary, larceny_theft, motor_vehicle_theft, population

        data.append([row[i] for i in [1, 5, 6, 8]])

        text(row[1], row[5], row[0], size=11, horizontalalignment='center')

    data = zip(*data)

    sct = scatter(map(float, data[0]), map(float, data[1]), c=map(float, data[2]), s=sqrt(map(int, data[3])), linewidths=2, edgecolor='w', alpha=0.75)

    axis([0, 11, 200, 1280]) # DC is an outlier!

    xlabel('Murders per 100,000 population')
    ylabel('Burglaries per 100,000 population')

    show()

def draw_text(row):

    text(row['murder'], row['burglary'], row['state'], size=11, horizontalalignment='center')

def plot_with_pandas():

    data = pandas.read_csv(urlopen('http://datasets.flowingdata.com/crimeRatesByState2005.csv'), skiprows=[1])

    data.apply(draw_text, axis=1)

    sct = scatter(data['murder'], data['burglary'], c=data['larceny_theft'], s=sqrt(data['population']), linewidths=2, edgecolor='w', alpha=0.75)

    axis([0, 11, 200, 1280]) # DC is an outlier!

    xlabel('Murders per 100,000 population')
    ylabel('Burglaries per 100,000 population')

    show()

if __name__ == '__main__':

    #plot_with_pandas()
    plot_without_pandas()
