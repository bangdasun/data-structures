For the programming portion of the assignment, please submit only your `.java` files and your `README.txt`.  Your code should be well commented.  In addition please include a detailed README.txt file which indicates exactly what files you are submitting, what problem they solve, and how to compile and run them.

(52 points) In this problem you will implement Dijkstra's algorithm to find shortest paths between pairs of cities on a map. We are providing a a GUI that lets you visualize the map and the path your algorithm finds between two cities.
Before you start:

Download and unpack the file `programming1.zipView` in a new window, which contains the GUI, a graph implementation, and data files representing a map. The file `cityxy.txt` contains a list of cities and their (X,Y) coordinates on the map. These are the vertices in the graph. The file `citypairs.txt` lists direct, connections between pairs of cities. These links are bidirectional, if you can from NewYork to Boston, you can get from Boston to NewYork. These are the edges of the graph.

If you use an IDE, import the java files and make sure that `citxy.txt` and `citypairs.txt` are placed in the project directory. If you use `java` and `javac` from the command line put the files in the same directory as the source files.

Compile all java sources and run the program Display. This should bring up a window and display the map. You will notice that clicking on "Compute All Euclidean Distances" does nothing and that "Draw Dijkstra's Path" will throw a null pointer exception on the terminal. You will have to implement these methods yourself.

Carefully read through the classes `Vertex.java` and `Edge.java`, which represent the vertices and edges of a graph. You will not have to modify these classes for the assignment, but you need to understand how the graph is represented and what information is associated with each vertex and edge. If you do modify these files, please explain in the README.

You will only have to modify `Dijkstra.java`, which represents a graph and will contain your implementation of Dijkstra's algorithm. You will need to use the instance variable `vertexNames`, which contains a mapping from city names to `Vertex` objects after the graph is read from the data files. The main method of `Dijkstra` illustrates how the class is used by the GUI and might be useful for testing your implementation on the command line.

a. Implement the method `computeAllEuclideanDistances()` which should compute the euclidean distance between all cities that have a direct link and set the weights for the corresponding edges in the graph. Once this works correctly, the correct distances should be displayed in the GUI when clicking on "Compute All Euclidean Distances".

b. In the method `doDijkstra(String s)`, implement Dijkstra's algorithm starting at the city with name s. Use the distances associated with the edges. The method should update the `distance` and `prev` instance variables of the `Vertex` objects. You do not have to use a priority queue to store vertices that still need to be visited. Instead, keep these vertices on a list and scan through the entire list to find the minimum. We are making this simplification (at the expense of runtime) because java.util.PriorityQueue does not support the decreaseKey operation.

c. Implement the method `getDijkstraPath(String s, String t)`, which first calls `doDijstra(s)` and then uses the `distance` and `prev` instance variables of the Vertex objects to find the shortest path between s and t. The resulting path should be returned as a list of `Edge` objects. Once this works correctly, you should be able to compute and display paths in the GUI.

NOTE: The framework of `Display.java`, `Dijsktra.java`, `Vertex.java`, `Edge.java` are from the instructors and former TA Linan Qiu (https://github.com/linanqiu/data-structures-graph-viz/tree/master/dijkstra)
