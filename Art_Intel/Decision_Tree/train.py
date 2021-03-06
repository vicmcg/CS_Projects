import pickle
import csv
import sys
import numpy as np
from Tree_Model import Tree

storage = list()
with open(sys.argv[1], 'rb') as inpu:
	inputData = csv.reader(inpu)
	inputData.next()

	for row in inputData:
		row[0] = float(row[0])
		row[1] = float(row[1])
		row[2] = float(row[2])
		row[3] = float(row[3])
		row[4] = float(row[4])
		storage.append(row)
#can use any package to read the file
model =  Tree()
model.train(storage)
#with open('model.pkl','wb') as h:
    #pickle.load(model,h)
pickle.dump(model,  open('model.pkl','wb'))

