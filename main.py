import courses
import search

def strip_key(tpl_arr):
     key_arr = []
     for tuple in tpl_arr:
          key_arr.append(tuple[0])
     return key_arr

if __name__ == "__main__":
    graph = courses.parse_courses("graph.txt", "adjlst")
    topsorted_graph = search.topsort(graph)
    print("The order of classes a CS student should take to graduate: ")
    for course in topsorted_graph:
         print("\t" + course)