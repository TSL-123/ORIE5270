from pyspark import SparkConf, SparkContext
import re
import numpy as np

centroids = []
length = 0


def closest_cluster(line):
    maxx = 10000000000
    maxkey = np.inf
    for i in range(length):
        temp = np.linalg.norm(np.array(line) - np.array(centroids[i]))
        if temp < maxx:
            maxx = temp
            maxkey = i
    return maxkey

def add_tuple(x, y):
    res = []
    for i in range(len(x[0])):
        res.append(x[0][i]+y[0][i])
    return res, x[1]+y[1]


def pyspark_kmeans(ctxt, datatxt):
    global length
    global centroids
    conf = SparkConf()
    sc = SparkContext(conf=conf, appName="textEdit")

    f = open(ctxt, "r")
    for line in f:
        centroids.append([float(x) for x in line.split()])
    length = len(centroids)
    print(length)

    lines = sc.textFile(datatxt)
    #lines = lines.map(lambda l: l.split())
    lines = lines.map(lambda l: [float(i) for i in l.split()])
    count = 0
    while True:
        count = count + 1
        print(count)

        cluster_lines = lines.map(lambda l: (closest_cluster(l), (l, 1)))

        total_dis = cluster_lines.map(lambda l: (1, np.linalg.norm(np.array(l[1][0]) - np.array(centroids[l[0]]))))
        total_dis = total_dis.reduceByKey(lambda a, b: a+b).collect()
        print(total_dis)
        #print(centroids_num)
        temp_cen = cluster_lines.reduceByKey(lambda x, y: add_tuple(x, y)).sortByKey(ascending=True)
        #print(temp_cen.collect())
        temp_cen = temp_cen.map(lambda l: list(np.array(l[1][0])/l[1][1])).collect()
        print(len(centroids), centroids)
        print(len(temp_cen), temp_cen)
        if temp_cen == centroids:
            break
        centroids = temp_cen
    #centroids.saveAsTextFile("temp")
    return centroids



    #lines_test = sc.textFile(ctxt)
    # lines = lines.map(lambda l: l.split())
    #lines_test = lines_test.map(lambda l: [float(i) for i in l.split()])
    #print(lines.collect())


if __name__ == '__main__':
    print(pyspark_kmeans('c1.txt', 'data.txt'))
