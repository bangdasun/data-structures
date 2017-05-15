COMS W3134 Data Structure in Java HW5 Version 1.0 05/01/2017
Java version "1.8.0_111"
Javac version "1.8.0_121"
###############################################################################################
Student information
Name: Bangda Sun
UNI: bs2996
Email: bs2996@columbia.edu
###############################################################################################
HW4 file list:
1. written.pdf
2. Dijkstra.java
3. Display.java
4. Edge.java
5. Vertex.java
6. citypairs.txt
7. cityxy.txt
8. README.txt
###############################################################################################
How to compile java file:
Open windows 7 cmd, then move to the directory which included the java file:
"cd workspace/hw5/src"

javac Edge.java
javac Vertex.java
javac Dijkstra.java
javac Display.java

Run the java GUI:
java Display
###############################################################################################
Code description:

Dijkstra.java
I did the modification to Dijkstra.java: 
(1) Implement the method of computeAllEuclideanDistances() based on computeEuclideanDistance().

(2) Implement doDijkstra(String s) method to compute the shortest distance 

(3) Implement getDijkstraPath(String s, String t), which will return the shorest path between the
start city s and the end city t.
############################################################################################### 