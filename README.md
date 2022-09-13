# mapreduce_breadth_first_search

Creating a parallel breadth first search program using MapReduce.
Mapper emits distances from adj. list.
Reducer determines shortest distance for each node.
Driver program loops mapper & reducer until no difference in output from reducers.
