import csv
import pandas as pd
import plotly.figure_factory as pff
import statistics
import plotly.graph_objects as go
import random 

df=pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

#calculation of population mean and standard deviation
population_mean=statistics.mean(data)
print(population_mean)
std_deviation=statistics.stdev(data)
print(std_deviation)

fig=pff.create_distplot([data],["reading_time"],show_hist=False)
fig.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,1],mode="lines",name="mean"))
fig.show()

#calculation of sample mean and standard deviation
#dataset=[]
#for i in range(0,100):
 #    random_index= random.randint(0,len(data))
  #   value = data[random_index]
   #  dataset.append(value)
#mean = statistics.mean(dataset)
#std_deviation = statistics.stdev(dataset)

#print("Mean of sample:- ",mean)
#print("std_deviation of sample:- ",std_deviation)


##  code to find the mean of 100 data points 1000 times and plot it
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

    #function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = pff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()

def standard_deviation():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()