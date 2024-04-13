from pandas import DataFrame

Data = {'x':[1,2,3,4,3,4,3,3,2,4,2,3,4,4,1,4,2,4,3,2,1,3,1,4,2,3],
        'y':[5,6,7,8,6,5,9,8,10,6,8,5,10,8,6,7,5,8,3,4,3,2,5,1,6,3]
       }

df = DataFrame(Data,columns=['x','y'])
print(df)

import matplotlib.pyplot as plt
plt.scatter(df['x'], df['y'])
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3).fit(df)
centroids = kmeans.cluster_centers_
print(centroids) 

plt.scatter(df['x'],df['y'], c=kmeans.labels_.astype(float),s=50, alpha=0.5)
plt.scatter(centroids[:,0], centroids[:,1], c='red', s=50)
plt.show()