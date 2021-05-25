import numpy as np
import matplotlib.pyplot as plt

# creating the dataset
data = {'5/9':1, '5/10':15, '5/11':11,
        '5/12':21,'5/13':35,'5/14':34,'5/15':185}
date = list(data.keys())
people = list(data.values())
  
fig = plt.figure(figsize = (10, 6))
 
# creating the bar plot
plt.bar(date, people, width = 0.4)
plt.ylim(0,200)
plt.xlabel("日期")
plt.ylabel("人數")
plt.title("410789003")
plt.show()