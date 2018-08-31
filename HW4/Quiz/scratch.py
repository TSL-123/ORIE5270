from pyspark import SparkConf, SparkContext
import re
import numpy as np

conf = SparkConf()
sc = SparkContext(conf=conf, appName="textEdit")

f = open('B.txt', "r")

lines = sc.textFile("A.txt")

B = []

for line in f:
    num = ''
    for char in line:
        if char == ',':
            B.append(int(num))
            num = ''
        else:
            num = num + char
    B.append(int(num))

B = np.array(B)

matrix = lines.map(lambda l: re.split('[,.]', l))
matrix = matrix.map(lambda w: [int(i) for i in w])


ans = matrix.map(lambda l: [np.matmul(l, B.transpose())])

print(ans.collect())