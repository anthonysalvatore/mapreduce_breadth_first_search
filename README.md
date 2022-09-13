# mapreduce_breadth_first_search

Creating a parallel breadth first search program using MapReduce.
Mapper emits distances from adj. list.
Reducer determines shortest distance for each node.
Driver program loops mapper & reducer until no difference in output from reducers.


Run from inside HDFS master node, with graph.txt in the input file and all other files on the master node.
Convert from CR LF to LF in python files before running on HDFS.
