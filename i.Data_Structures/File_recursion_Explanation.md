Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"


First get the list of all files & directories in the given path.
For each item, 
if that is a file and ends with input suffix, then add to the filepath_list
If that is a directory, do recursive function call on that dir for all sub directories.
Time complexity is O(n) and space complexity O(n)
