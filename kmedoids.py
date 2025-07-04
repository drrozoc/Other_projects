# -*- coding: utf-8 -*-
"""Kmedoids.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j7FXeeeeMO3PLYlU_ewK94BPT5_dHltb
"""

!pip install scikit-learn-extra

"""# **K medoids**

The following code implements K medoids algorythm:

1. Initialization: Randomly select k data points from the dataset as initial medoids.
2. Assignment: Assign each data point to the nearest medoid based on a distance metric (e.g., Euclidean distance).
3. Update Medoids: For each cluster, calculate the total cost (e.g., sum of distances) of swapping each non-medoid point with the medoid. Select the point that results in the lowest total cost as the new medoid for that cluster.
4. Repeat: Repeat the assignment and update steps until the medoids no longer change significantly or a maximum number of iterations is reached.
5. Termination: Stop the algorithm when the medoids stabilize or after a set number of iterations.
6. Output: Return the final k clusters with their respective medoids.

During the update step in the K-medoids algorithm, the algorithm evaluates the cost of swapping a non-medoid point with the current medoid. The goal is to find the point that, if chosen as the new medoid, would result in the lowest total cost for the cluster.


"""

#IMPORT LIBRARIES
from sklearn_extra.cluster import KMedoids
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import re
from sklearn.cluster import KMeans
#from sklearn_extra.cluster import KMedoids

#Reading excel file database
data = pd.read_excel('datos_troncal.xlsx')

"""
Convert to datetime objects:
The pd.to_datetime() function converts the values in the 'INTERVALO' column to
datetime objects. The format argument specifies the format of the time strings.
The dt.time attribute then extracts the time component from the datetime objects.

Extract hour and minute:
The apply() function applies a lambda function to each element in the
'INTERVALO' column. The lambda function extracts the hour and minute attributes
from the datetime object and calculates the time in hours by adding the hour
and minute divided by 60.
"""

timeToFloat = pd.to_datetime(data['INTERVALO'], format='%H:%M:%S').dt.time
Timehours = data['INTERVALO'].apply(lambda x: x.hour + x.minute / 60 + x.second / 3600)
print("Checking the time conversion success:\n",Timehours)#We verify that the convertion wwas succesfully done, for example
#00:15:00 is a quarter of an hour, therefore, the value is 0.25.
print()
print()
print("Time_newDtype:\n",Timehours.describe())

arr = data['Total general']

min_val = np.min(arr)
max_val = np.max(arr)
scaled_arr = (arr - min_val) / (max_val - min_val)

min_Time = np.min(Timehours)
max_Time = np.max(Timehours)
print(min_Time)
scaled_Time = (Timehours - min_Time) / (max_Time - min_Time)

twoD = np.column_stack((scaled_Time,scaled_arr)) #This will be the new dataset
#as it just contain the standarized values to be analyzed and fitted to the
#models

n_clusters = 2

kmedoids_model = KMedoids(n_clusters=n_clusters, random_state=0).fit(twoD)
#Random state is a parameters that allow that for every code run the variable
#initialization is deterministic so that there can be comparison between
# iterations.
cluster_labels = kmedoids_model.labels_
medoids = kmedoids_model.cluster_centers_
print(medoids)
x2_coords = [point[0] for point in medoids ]
y2_coords = [point[1] for point in medoids]
#distances = kmedoids_model.transform(data)

fig = plt.figure()
ax1 = fig.add_subplot(111) #, projection='3d')
colores=['red','green','blue','cyan','purple']
asignar2=[]
for rows in medoids:
  asignar2.append(colores[rows])
ax1.scatter(scaled_Time, scaled_arr, color = asignar2)
ax1.scatter(x2_coords, y2_coords,  color='gray')
ax1.set_xlabel('Total_persons')
ax1.set_ylabel('Time ')
plt.grid(visible=True,alpha=0.8)

"""
# **Hierarchical clustering**

Hierarchical clustering can be divided into two main types:

**Agglomerative Hierarchical Clustering:**

The agglomerative approach starts with each data point as a single cluster and then merges the closest pairs of clusters until all data points belong to a single cluster.
This method is also known as bottom-up clustering.

**Divisive Hierarchical Clustering:**

The divisive approach starts with all data points in a single cluster and then splits the clusters recursively until each data point is in its own cluster.
This method is also known as top-down clustering."""

agg_cluster = AgglomerativeClustering(n_clusters=2, linkage='ward')
agg_cluster.fit(twoD)