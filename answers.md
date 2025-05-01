# CMPS 2200 Recitation 08

## Answers

**Name:**________Anh Pham_________________
**Name:**_________________________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**
- The work of this algorithm is O((V + E) log V), just like regular Dijkstra’s, since we use a priority queue and process each edge and node once. The span is O(V log V), because the longest chain of dependent operations comes from the priority queue's extract-min step, which we do once per vertex and each takes log V time.



- **2b)**
- The get_path function reconstructs the shortest path from the source to a given destination using the parent dictionary built by BFS. It walks backward from the destination, following each node’s parent, until it reaches the source. Then it reverses the collected nodes to produce the path in the correct order. The result is returned as a string (excluding the destination node itself). This adds only O(k) work and span for a path of length k, which keeps the overall complexity unchanged.

