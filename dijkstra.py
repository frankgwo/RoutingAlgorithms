# Solution of Assignment 2 of EE6108
# A Python implement of Dijkstra Algorithm.
# by GUO DONGFANG, G1801224L, MSc of CommEng, EEE, NTU


# Class to represent a graph
class Graph:

    # A function to find the nodes with minimum dist value, from the queue of nodes with undetermined distance
    def min_distance(self, dist, queue):
        # Initialize min value to infinite and min_index as -1
        minimum = float("Inf")
        min_index = -1
        # from the dist array, pick the one which has min value and is still in the queue
        for i in range(len(dist)):
            if i in queue and dist[i] < minimum:
                minimum = dist[i]
                min_index = i
        return min_index

    # A function to generate the lines of the output table
    def line_list(self, set, dist, iteration):
        line_head = 'Iter'+str(iteration)
        line_list = [line_head]
        for i in range(len(dist)):
            routing = str(dist[i])
            line_list.append(routing)
        line_list.append(str(set))
        return line_list

    # Dijkstra's algorithm
    # Find shortest distances from all the nodes to the target
    def dijkstra(self, graph, target):
        row = len(graph)
        col = len(graph[0])

        # dist[i] will hold the shortest distance from target to i
        # Initialize all distances to infinite
        dist = [float("Inf")] * row

        # Distance of target node from itself is always 0
        dist[target] = 0

        # Add all nodes in the to-be-determined queue, make a empty set of already found ones
        queue = []
        for i in range(row):
            queue.append(i)
        found_set = []
        output_lines = []

        # Find shortest path for all nodes
        while queue:
            # Pick the minimum dist node from the queue
            u = self.min_distance(dist, queue)   # the found node!

            # add already found nodes into set and remove it from the queue
            found_set.append(u)
            found_set.sort()
            queue.remove(u)

            # Update dist[j] only if it is in queue, there is an edge from founded node u
            # to current node j, and total weight of path from target to current j through
            # founded u is smaller than current value of dist[j]
            for j in range(col):
                if graph[u][j] and j in queue:
                    if dist[u] + graph[u][j] < dist[j]:
                        dist[j] = dist[u] + graph[u][j]
            line = self.line_list(found_set, dist, len(found_set)-1)
            output_lines.append(line)

        # Output the result into the txt, in a table form as the PPT shows.
        f = open(table_path, 'w')
        # Make the table header
        header = "Iterations"
        for i in range(row):
            node_name = "Node" + str(i)
            header = header + '\t' + node_name
        header = header + '\t' + "Set N"
        f.write(header + '\n')
        # Write the routing information
        for row in output_lines:
            row_str = "\t".join(row)
            f.write('\n')
            f.write(row_str)
        f.close()
        print("The result has been printed in the ./OUTPUT_dijkstra.txt ! Check it out :)")


# Configuration of path
graph_path = './INPUT_dijkstra.txt'          # path of input graph
table_path = './OUTPUT_dijkstra.txt'          # path of output table

# Read the txt to get the input graph.
with open(graph_path, 'r') as f:
    graph = []
    data = f.readlines()
    for line in data:
        line_data = line.split()
        line_data = list(map(int, line_data))
        graph.append(line_data)

# Input the target node
print("------a Python implement of Dijkstra's algorithm------")
print("------------------by GUO DONGFANG---------------------")
print("Please make sure the adjacency matrix of your graph has been correctly written into ./INPUT_dijkstra.txt!")
print("There are totally {} nodes in your input graph.".format(len(graph)))
target = input("Please input your target node (choose from 0 to {}):".format(len(graph)-1))

# Run! and output the solution table
g = Graph()
g.dijkstra(graph, int(target))
input("Press Enter to exit.")