# variable declaration graph node
graph = {
    "0":{"1":4,"7":8},
    "1":{"2":8,"7":11},
    "2":{"1":8,"3":7,"5":4,"8":2},
    "3":{"2":7,"4":9,"5":14},
    "4":{"3":9,"5":10},
    "5":{"2":4,"3":14,"4":10},
    "6":{"5":2,"7":1,"8":6},
    "7":{"0":8,"6":1,"8":7},
    "8":{"2":2,"6":6,"7":7}
}
def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    # enter node in loop
    for node in unseenNodes:
        shortest_distance[node] = infinity
    # start = 0
    shortest_distance[start] = 0
    # enter node in loop
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                # way is near
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        # all way in loop
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    # node goal
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
dijkstra(graph, "0", "4")

# Shortest distance is 21
# And the path is ['0', '7', '6', '5', '4']