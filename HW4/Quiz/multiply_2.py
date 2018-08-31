from pyspark import SparkConf, SparkContext
import re
import numpy as np

conf = SparkConf()
sc = SparkContext(conf=conf, appName="textEdit")


lines_a = sc.textFile("A.txt")
lines_b = sc.textFile("B.txt")


matrix_a = lines_a.map(lambda l: re.split('[,.]', l))
matrix_a = matrix_a.map(lambda w: [int(i) for i in w])
matrix_b = lines_b.map(lambda l: re.split('[,.]', l))
matrix_b = matrix_b.map(lambda w: [int(i) for i in w])


ans = matrix_a.map(lambda la: [np.matmul(la, lb) for lb in range(lines_B)])

print(ans.collect())