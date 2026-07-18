def nested_list_parse(nested_list, visited_list = []):
 new_nodes = []

 for node in nested_list:
  if str(type(node)) == "<class 'list'>":
   for sub_node in node:
    if str(type(sub_node)) == "<class 'list'>":
     new_nodes.append(sub_node)

    else:
     visited_list.append(sub_node)

  else:
   visited_list.append(node)

 if new_nodes:
  return nested_list_parse(new_nodes)
 
 else:
  return visited_list
 



print(nested_list_parse([1, [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]]]))