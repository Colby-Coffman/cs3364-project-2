import numpy as np
import main

_clock = 0 # Private global, do not modify

def dfs(graph):
    """
    An implementation of a depth first search algorithm

    Args:
        graph (abstract): A representation of a graph. Pass either an ordered pair of a list of vertexes
        as the first component and edges as the second component. Or a multidimensional list
        representing an adjacency list
    Returns:
        prepost (list): A list with its first element being a dictionary mapping
        the pre-numbers of all vertexes in the graph, and it's second element being a
        dictionary mapping the post-numbers of all vertexes in the graph
    """
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
                explore(graph, vertex, found_table=found_table, prepost=prepost)
    elif graph_type == "adjlst":
        for vertex in graph:
            if found_table[vertex[0]] == False:
                explore(graph, vertex[0], found_table=found_table, prepost=prepost)
    global _clock
    _clock = 0
    return prepost

def topsort(graph):
    """
    A function to preform topological sorting on a dag

    Args:
        graph (abstract): A representation of a graph. Pass either an ordered pair of a list of vertexes
        as the first component and edges as the second component. Or a multidimensional list
        representing an adjacency list
    Returns:
        top_sorted (list): A list in topological order of the vertexes of the graph passed
    """
    top_sorted = []
    postnums = dfs(graph)[1]
    top_sorted = sorted(postnums.items(), key=lambda item: item[1], reverse=True)
    top_sorted = main.strip_key(top_sorted)
    return top_sorted

def explore(graph, vertex, found_table=None, prepost=None):
    """
    A function that explores all vertexes reachable by the passed vertex. Will return a dictionary
    associating every vertex in the graph with a boolean value which will be true if the a given vertex
    is reachable by the passed vertex. Two graph types are supported. You can additionally pass your own
    dictionary of vertexes found. You can also choose to pass a list of two empty dictionaries to obtain the
    pre and post numbers of every vertex in the graph.

    Args:
        graph (abstract): graph (abstract): A representation of a graph. Pass either an ordered pair of a list of vertexes
        as the first component and edges as the second component. Or a multidimensional list
        representing an adjacency list
        vertex (string): A string representing a vertex in the graph to explore from
        found_table (flag=None): Pass a dictionary containing all the vertexes and a boolean value
        as the key, representing wether the vertex has already been found or not
        prepost (flag=None): Pass a list containing two empty dictionaries if you would like to obtain the pre and post
        numbers for all vertexes in the graph. The function will modify this list, putting all pre numbers in the first element
        and all post numbers in the second
    """
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
                explore(graph, edge[1], found_table=found_table, prepost=prepost)
    elif graph_type == "adjlst":
        for node in graph:
            if node[0] == vertex:
                for edge in node[1:]:
                    if edge == None: break
                    if found_table[edge] == False:
                        explore(graph, edge, found_table=found_table, prepost=prepost)
                break
    if prepost != None:
        _clock += 1
        prepost[1][vertex] = _clock
    return found_table

def _infer_graph_type(graph):
    """
    A private helper function to validate wether the passed graph is an accepted abstract
    data type. This function is not thorough and must be updated for any robust application.

    Args:
        graph (abstract): graph (abstract): A representation of a graph. Pass either an ordered pair of a list of vertexes
        as the first component and edges as the second component. Or a multidimensional list
        representing an adjacency list
    Returns:
        The function returns the string "graph" if the passed abstract graph is a tuple
        The function returns the string "adjlist" if the passed abstract graph is a list
    Raises:
        Execution is halted if the passed abstract graph is not accepted
    """
    if type(graph) == tuple: return "graph"
    if type(graph) == list: return "adjlst"
    assert False, "Invalid Graph Format"