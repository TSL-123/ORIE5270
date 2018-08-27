import numpy as np


class graph_class(object):
    def __init__(self, filename):
        self.graph_dict = {}
        self.nodes = []
        f = open(filename, "r")
        while True:
            line1 = f.readline()
            line2 = f.readline()
            if not line2:
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

    def search_cycle(self):
        global que
        que = []
        N = len(self.nodes) + 1
        for i in self.nodes:
            for j in self.nodes:
                if i != j:
                    trace = {}
                    source = i
                    destination = j
                    #print(source, destination)
                    F = {}
                    for k in self.nodes:
                        trace[k] = None
                        F[(0, k)] = np.inf
                    F[(0, destination)] = 0
                    for times in range(1, N+1):
                        for k in self.nodes:
                            F[(times, k)] = F[(times-1, k)]
                            for point in self.graph_dict[k]:
                                #print(times,k,point,F)

                                #print(times, k, point, F[(times, k)], F[(times-1, k)])
                                F[(times, k)] = min(F[(times, k)], F[(times-1, point)]+self.graph_dict[k][point])
                                if F[(times, k)] < F[(times-1, k)]:
                                    trace[k] = point
                                #print(times , k, F[(times, k)])
                    if F[(N, source)] < F[(N-1, source)]:
                        que.append(source)
                        record = set([])

                        current_point = source
                        while current_point not in record:
                            record.add(current_point)
                            que.append(trace[current_point])
                            current_point = trace[current_point]
                        delete_point = source
                        while delete_point != current_point:
                            que.pop(0)
                            delete_point = que[0]
                        return que

def find_negative_cicles(name_txt_file):
    g = graph_class(name_txt_file)
    return g.search_cycle()


if __name__ == '__main__':
        print(find_negative_cicles("bellman_ford.txt"))
