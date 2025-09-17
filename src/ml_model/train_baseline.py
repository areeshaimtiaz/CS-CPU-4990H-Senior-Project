
# Baseline toy model for mapping CFG features -> optimization labels
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np

# Toy data: [nodes, edges, loops] -> label index for optimization
X = np.array([[5,6,1],[10,12,2],[3,2,0],[8,11,1],[12,15,3]])
y = np.array([0,1,0,1,2])  # 0: DCE, 1: inline, 2: unroll (toy)

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.4, random_state=42)
clf = DecisionTreeClassifier().fit(Xtr, ytr)
print(classification_report(yte, clf.predict(Xte)))
