%matplotlib notebook
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
plt.figure(figsize=(4,4))
plt.subplot(111)
X1,Y1=make_classification(n_samples=150, n_features=2, n_redundant=0, n_informative=2,
                         n_clusters_per_class=1, random_state=3, class_sep=1.1, n_classes=3)
plt.scatter(X1[:,0], X1[:,1], marker="o", c=Y1, s=25, edgecolor='k')
plt.show()
