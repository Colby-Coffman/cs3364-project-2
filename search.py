import numpy as np
import main

_clock = 0

def dfs(graph):
    graph_type = _infer_graph_type(graph)
    prepost = [{}, {}]
    found_table = {}
    if graph_type == "graph":
        for vertex in graph[0]:
            found_table[vertex] = False
    elif graph_type == "adjlst":
        for vertex in graph:
            found_table[vertex[0]] = False
    if graph_type == "graph":
        for vertex in graph[0]:
            if found_table[vertex] == False:
                explore(graph, vertex, "graph", found_table=found_table, prepost=prepost)
    elif graph_type == "adjlst":
        for vertex in graph:
            if found_table[vertex[0]] == False:
                explore(graph, vertex[0], "adjlst", found_table=found_table, prepost=prepost)
    global _clock
    _clock = 0
    return prepost

def topsort(graph):
    top_sorted = []
    postnums = dfs(graph)[1]
    top_sorted = sorted(postnums.items(), key=lambda item: item[1], reverse=True)
    top_sorted = main.strip_key(top_sorted)
    return top_sorted

def explore(graph, vertex, graph_type=None, found_table=None, prepost=None):
    if graph_type == None:
        graph_type = _infer_graph_type(graph)
    if found_table == None: # Added functionality
        found_table = {}
        if graph_type == "graph":
            for node in graph[0]:
                found_table[node] = False
        elif graph_type == "adjlst":
            for node in graph:
                found_table[node[0]] = False
    if prepost != None:
        global _clock
        _clock += 1
        prepost[0][vertex] = _clock
    found_table[vertex] = True
    if graph_type == "graph":
        for edge in graph[1]:
            if vertex == edge[0] and found_table[edge[1]] == False:
                explore(graph, edge[1], graph_type=graph_type, found_table=found_table, prepost=prepost)
    elif graph_type == "adjlst":
        for node in graph:
            if node[0] == vertex:
                for edge in node[1:]:
                    if edge == None: break
                    if found_table[edge] == False:
                        explore(graph, edge, graph_type=graph_type, found_table=found_table, prepost=prepost)
                break
    if prepost != None:
        _clock += 1
        prepost[1][vertex] = _clock
    return found_table





def _infer_graph_type(graph):
    if type(graph) == tuple: return "graph"
    if type(graph) == type(np.zeros((1,1))): return "adjmat"
    if type(graph) == list: return "adjlst"
    assert False, "Invalid Graph Format"
