from pyspark import SparkConf, SparkContext
import re
import numpy as np

conf = SparkConf()
sc = SparkContext(conf=conf, appName="textEdit")


lines_a = sc.textFile("A.txt")
lines_b = sc.textFile("B.txt")

rows = lines_a.count()

matrix_a = lines_a.map(lambda l: re.split('[,.]', l))
matrix_a = matrix_a.map(lambda w: [int(i) for i in w])


def yield_1(w):
    for i in range(len(w)):
        yield(i, w[i])


matrix_a = matrix_a.map(lambda w: [(w[0], w[i]) for i in range(1, len(w))])
matrix_a = matrix_a.flatMap(lambda w: yield_1(w))

print(matrix_a.collect())

matrix_b = lines_b.map(lambda l: re.split('[,.]', l))
matrix_b = matrix_b.map(lambda w: [int(i) for i in w])

matrix_b = matrix_b.flatMap(lambda w: yield_1(w))

print(matrix_b.collect())

matrix_together = matrix_a.join(matrix_b)

print(matrix_together.collect())
matrix_together = matrix_together.map(lambda l: (l[1][0][0], l[1][0][1]*l[1][1]))
matrix_together = matrix_together.reduceByKey(lambda a, b: a + b)

print(matrix_together.collect())
#print(ans.collect())