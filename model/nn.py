from sknn.mlp import Classifier, Layer
import sklearn
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

file = open("../clean-data/data.csv", "r")
data = file.readlines()
vector_x = list()
vector_y = list()
for ii in data[1:]:
  temp_vector_x = ii.split(",")
  #Because the first two features are timestamp and dow jones rating. 
  x, y = map(float, temp_vector_x[2:-2]), int(temp_vector_x[-1])
  vector_x.append(x)
  vector_y.append(y)


vector_x = np.array(vector_x)
vector_y = np.array(vector_y)

x_train, x_test, y_train, y_test = train_test_split(vector_x, vector_y, test_size = 0.3, random_state = 0)

net = Classifier(
		layers=[
			Layer("Maxout", units = 10, pieces = 2), 
			Layer("Softmax")],
		learning_rate = 0.1, 
		n_iter = 25
		)
net.fit(x_train, y_train)
score = net.score(x_test, y_test)
print score
