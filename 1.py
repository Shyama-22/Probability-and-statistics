import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from statistics import variance
data_timegap=[8,3,5,6,3,4,2,6,11,9,5,1,7,7,12,9,13,21,11,5,2,8,2,3,5,31,16,16,4,31]
def my_mean(st,end,data):
    return mean(data[st:end])
def my_variance(st,end,data):
    return variance(data[st:end])
mean_data=[]
variance_data=[]
for i in range(1,31):
    mean_data.append(my_mean(0,i,data_timegap))
for i in range(2,31):
    variance_data.append(my_variance(0,i,data_timegap))
frequency_dict={}
def fill_freq(freq_dict,data):
    for i in data:
        if i in freq_dict:
            freq_dict[i]+=1
        else:
            freq_dict[i] = 1
        
fill_freq(frequency_dict,data_timegap)
x = list(frequency_dict.keys())
y = list(frequency_dict.values())

plt.bar(x, y)
plt.title("Frequency Distribution")
plt.xlabel('Time')
plt.ylabel('Frequency/Count')
plt.show()

import scipy.stats
from scipy.stats import expon , norm
from matplotlib.pyplot import figure

figure(figsize=(5, 5))
Expon = expon.pdf(x,0,mean_data[29])

plt.plot(x,Expon,'g',linestyle='--')
plt.title("Exponential plot!")
plt.xlabel('Time ')
plt.ylabel('Frequency ')
plt.show()
x_ax=np.arange(-15,15,1)
y_ax=norm.pdf(x_ax,loc=0,scale=mean_data)
plt.plot(x_ax,y_ax,'r',linestyle='-.')
plt.title("Normal plot!")
plt.xlabel('Time ')
plt.ylabel('Frequency ')
plt.show()

#the normal plot matches better with the gaussian.