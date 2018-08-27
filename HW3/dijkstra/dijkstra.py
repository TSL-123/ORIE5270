import heapq
import numpy as np


class graph_class(object):
    def __init__(self, filename, source, destination):
        self.source = source
        self.destination = destination
        self.graph_dict = {}
        self.nodes = []
        self.dis = {}
        self.F = []
        self.S = set([])
        self.trace = {}
        f = open(filename, "r")
        while True:
            line1 = f.readline()
            line2 = f.readline()
            if not line1:
                break
            line1 = int(line1)
            self.nodes.append(line1)
            line2 = line2.strip()
            node = ''
            weight = ''
            local_dict = {}
            for i in line2:
                if i == '(':
                    current = 'node'
                elif i == ',':
                    current = 'weight'
                elif i == ')':
                    local_dict[int(node)] = int(weight)
                    node = ''
                    weight = ''
                    current = 'none'
                elif current == 'node':
                    node = node+i
                elif current == 'weight':
                    weight = weight+i
            self.graph_dict[line1] = local_dict

    def dij_search(self):
        global que
        que = []
        if self.source not in self.nodes or self.destination not in self.nodes:
            return None
        for i in self.nodes:
            self.dis[i] = np.inf
            self.trace[i] = None
        self.dis[self.source] = 0
        heapq.heappush(self.F, (self.dis[self.source], self.source))
        #print(self.F)
        while bool(self.F):
            current_node = heapq.heappop(self.F)
            #print(current_node[1])
            self.S.add(current_node[1])
            for key in self.graph_dict[current_node[1]]:
                #print(key)
                if key not in self.S:
                    temp = min(self.dis[key], self.dis[current_node[1]]+self.graph_dict[current_node[1]][key])
                    if temp < self.dis[key]:
                        self.dis[key] = temp
                        alist = [i for i in self.F if i[1] != key]
                        heapq.heappush(alist, (self.dis[key], key))
                        self.trace[key] = current_node[1]
                        self.F = alist
        next_node = self.destination
        while next_node is not None:
            que.append(next_node)
            next_node = self.trace[next_node]
        que.reverse()
        return self.dis[self.destination], que


def find_shortest_path(name_txt_file, source, destination):
    g = graph_class(name_txt_file, source, destination)
    return g.dij_search()


if __name__ == '__main__':
    print(find_shortest_path("dijkstra.txt", 1, 4))
