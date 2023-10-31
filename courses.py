import numpy as np
import bisect
import main

def parse_courses(path: str, graph_type = None):
     """
     This function parses a list of courses with a unique format and returns a abstract graph.
     All other input result in unexpected behaviour.

     Args:
          path (string): The relative file location of a courses file
          graph_type (flag=None): Pass the string "adjlst" for a adjacency list representation of the graph.
     Returns:
          graph (abstract): A representation of a graph. Either an ordered pair of a list of vertexes
          as the first component and edges as the second component. Or a multidimensional list
          representing an adjacency list
     """
     vertexes = []
     edges = []
     with open(path, 'r') as file:
          data = file.readlines()
          for string in data:
               vertex = string.split(" - ")[0]
               edge = string.split('(')[1].split(")")[0]
               vertexes.append(vertex)
               if "and" in edge:
                    edge = edge.split(", ")
                    if len(edge) > 1:
                         edges.append((edge[0], vertex))
                         edge = edge[1].split(" and ")
                         edges.append((edge[0], vertex))
                         edges.append((edge[1], vertex))
                    else:
                         edge = edge[0].split(" and ")
                         edges.append((edge[0], vertex))
                         edges.append((edge[1], vertex))
               elif edge == "N/A":
                    continue
               else:
                    edges.append((edge, vertex))
          if graph_type == "adjlst":
               return _adjlist((vertexes, edges))
          else:
               return (vertexes, edges)


def _adjlist(graph):
     """
     A private helper function to create an adjacency list representation out of a graph
     
     Args:
          graph (abstract): An ordered pair of a list of vertexes 
          as the first component and edges as the second component
     """
     adjlist = []
     vertex_index_table = {}
     for i in range(len(graph[0])): # T:O(V)/S:O(V)
          vertex_index_table[graph[0][i]] = i
          adjlist.append([graph[0][i]]) 
     for edge in graph[1]: # T:O(E)
          adjlist[vertex_index_table[edge[0]]].append(edge[1]) # T:av(1)O(V) S:O(E)
     for node in adjlist: # T:O(V) S:O(V)
          node.append(None)
     return adjlist