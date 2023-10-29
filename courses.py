import numpy as np
import bisect
import main

def parse_courses(path: str, graph_type = None):
     vertexes = []
     edges = []
     with open(path, 'r') as file:
          data = file.readlines()
          for string in data:
               vertex = string.split(" - ")[0]
               edge = string.split('(')[1].split(")")[0]
               if len(edges) == 22:
                    print()
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
          if graph_type == "adjmat":
               return _adjmatrix((vertexes, edges))
          elif graph_type == "adjlst":
               return _adjlist((vertexes, edges))
          else:
               return (vertexes, edges)

def _adjmatrix(graph):
     matrix = np.zeros((len(graph[0]), len(graph[0])))
     print(matrix)
     matrix_table = {}
     for i in range(len(graph[0])):
          matrix_table[graph[0][i]] = i
     for edge in graph[1]:
          matrix[matrix_table[edge[0]]][matrix_table[edge[1]]] = 1
     return matrix

def _adjlist(graph):
     adjlist = []
     sorted_edges = sorted(graph[1])
     sorted_edges_firstcmp = main.strip_key(sorted_edges)
     for i in range(len(graph[0])):
          adjlist.append([graph[0][i]])
          edge_index = bisect.bisect_left(sorted_edges_firstcmp, adjlist[i][0])
          for j in range(edge_index, len(sorted_edges) + 1):
               if (j==len(sorted_edges) or adjlist[i][0] != sorted_edges_firstcmp[j]):
                    adjlist[i].append(None)
                    break
               adjlist[i].append(sorted_edges[j][1])
     return sorted(adjlist)