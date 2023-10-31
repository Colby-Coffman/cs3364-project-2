import courses
import search


def strip_key(tpl_arr):
     """
     A helper function to create a list out of the first components of a list of ordered
     pairs

     Args:
          tpl_arr (list): A list of tuples
     Returns:
          key_arr (list): A list of the first components of tpl_arr
     """
     key_arr = []
     for tuple in tpl_arr:
          key_arr.append(tuple[0])
     return key_arr

if __name__ == "__main__":
    """
    Parses a list of courses and outputs the order in which the courses must be taken
    """
    graph = courses.parse_courses("graph.txt", "adjlst")
    topsorted_graph = search.topsort(graph)
    print("The order of classes a CS student should take to graduate: ")
    for course in topsorted_graph:
         print("\t" + course)