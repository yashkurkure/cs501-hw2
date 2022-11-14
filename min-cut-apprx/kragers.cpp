// Karger's algorithm to find Minimum Cut in an
// undirected, unweighted and connected graph.
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <chrono>
#include <fstream>
#include <string>

using namespace std::chrono;

 
// a structure to represent a unweighted edge in graph
struct Edge
{
    int src, dest;
};
 
// a structure to represent a connected, undirected
// and unweighted graph as a collection of edges.
struct Graph
{
    // V-> Number of vertices, E-> Number of edges
    int V, E;
 
    // graph is represented as an array of edges.
    // Since the graph is undirected, the edge
    // from src to dest is also edge from dest
    // to src. Both are counted as 1 edge here.
    Edge* edge;
};
 
// A structure to represent a subset for union-find
struct subset
{
    int parent;
    int rank;
};
 
// Function prototypes for union-find (These functions are defined
// after kargerMinCut() )
int find(struct subset subsets[], int i);
void Union(struct subset subsets[], int x, int y);
 
// A very basic implementation of Karger's randomized
// algorithm for finding the minimum cut. Please note
// that Karger's algorithm is a Monte Carlo Randomized algo
// and the cut returned by the algorithm may not be
// minimum always
int kargerMinCut(struct Graph* graph)
{
    // Get data of given graph
    int V = graph->V, E = graph->E;
    Edge *edge = graph->edge;
 
    // Allocate memory for creating V subsets.
    struct subset *subsets = new subset[V];
 
    // Create V subsets with single elements
    for (int v = 0; v < V; ++v)
    {
        subsets[v].parent = v;
        subsets[v].rank = 0;
    }
 
    // Initially there are V vertices in
    // contracted graph
    int vertices = V;
 
    // Keep contracting vertices until there are
    // 2 vertices.
    while (vertices > 2)
    {
       // Pick a random edge
       int i = rand() % E;
 
       // Find vertices (or sets) of two corners
       // of current edge
       int subset1 = find(subsets, edge[i].src);
       int subset2 = find(subsets, edge[i].dest);
 
       // If two corners belong to same subset,
       // then no point considering this edge
       if (subset1 == subset2)
         continue;
 
       // Else contract the edge (or combine the
       // corners of edge into one vertex)
       else
       {
          //printf("Contracting edge %d-%d\n",
          //       edge[i].src, edge[i].dest);
          vertices--;
          Union(subsets, subset1, subset2);
       }
    }
 
    // Now we have two vertices (or subsets) left in
    // the contracted graph, so count the edges between
    // two components and return the count.
    int cutedges = 0;
    for (int i=0; i<E; i++)
    {
        int subset1 = find(subsets, edge[i].src);
        int subset2 = find(subsets, edge[i].dest);
        if (subset1 != subset2)
          cutedges++;
    }
 
    return cutedges;
}
 
// A utility function to find set of an element i
// (uses path compression technique)
int find(struct subset subsets[], int i)
{
    // find root and make root as parent of i
    // (path compression)
    if (subsets[i].parent != i)
      subsets[i].parent =
             find(subsets, subsets[i].parent);
 
    return subsets[i].parent;
}
 
// A function that does union of two sets of x and y
// (uses union by rank)
void Union(struct subset subsets[], int x, int y)
{
    int xroot = find(subsets, x);
    int yroot = find(subsets, y);
 
    // Attach smaller rank tree under root of high
    // rank tree (Union by Rank)
    if (subsets[xroot].rank < subsets[yroot].rank)
        subsets[xroot].parent = yroot;
    else if (subsets[xroot].rank > subsets[yroot].rank)
        subsets[yroot].parent = xroot;
 
    // If ranks are same, then make one as root and
    // increment its rank by one
    else
    {
        subsets[yroot].parent = xroot;
        subsets[xroot].rank++;
    }
}
 
// Creates a graph with V vertices and E edges
struct Graph* createGraph(int V, int E)
{
    Graph* graph = new Graph;
    graph->V = V;
    graph->E = E;
    graph->edge = new Edge[E];
    return graph;
}

//returns 1 with a probability of 2%
int prob2perc(){

    // Pickm a random number between [0, 50)
    int random = rand()%50;

    // random no is 7 with the probability of 1/50 ≈ 0.02 or 2%
    if(random == 7){
        return 1;
    }
    return 0;
}

//returns 1 with a probability of 3%
int prob3perc(){

    // Pickm a random number between [0, 33)
    int random = rand()%34;

    // random no is 7 with the probability of 1/33 ≈ 0.03 or 3%
    if(random == 7){
        return 1;
    }
    return 0;
}

//returns 1 with a probability of 10%
int prob10perc(){

    // Pickm a random number between [0, 10)
    int random = rand()%10;

    // random no is 7 with the probability of 1/10 ≈ 0.1 or 10%
    if(random == 7){
        return 1;
    }
    return 0;
}

//returns 1 with a probability of 50%
int prob50perc(){

    // Pickm a random number between [0, 2)
    int random = rand()%2;

    // random no is 1 with the probability of 1/2 ≈ 0.5 or 50%
    if(random == 1){
        return 1;
    }
    return 0;
}


struct Graph* generateGraph(int vertices){
    printf("Generating graph size = %d\n", vertices);
    if(vertices <= 0){
        return NULL;
    }
    int num_edges = 0;
    int num_vertices = vertices;

    int max_possible_edges = vertices*(vertices-1);

    Edge* edges = new Edge[max_possible_edges];

    int edge_count = 0;
    for(int i = 0; i < num_vertices - 1; i++){
        for(int j = i + 1; j < num_vertices; j++){
            if(prob3perc()){
                edges[edge_count].src = i;
                edges[edge_count].dest = j;
                edge_count++;
            }
        }
    }

    // Add 1 to adjust to counting numbers instead of index
    num_edges = edge_count;

    struct Graph* g = createGraph(num_vertices, num_edges);

    printf("\tNum edges = %d (max = %d)\n", num_edges, max_possible_edges);
    for(int i = 0; i < num_edges; i++){
        g->edge[i].src = edges[i].src;
        g->edge[i].dest = edges[i].dest;
        //printf("\tAdding edge: %d - %d\n", g->edge[i].src, g->edge[i].dest);
    }
    return g;
}
 
// Driver program to test above functions
int main()
{
    srand(time(NULL));

    int gsizes[17] = {950,1000};

    for(int i = 0; i < 17; i++){

        int size = gsizes[i];
        int iters = size*size;

        std::string fname = std::to_string(size) + ".csv";
        std::ofstream file;
        file.open(fname);

        struct Graph* g = generateGraph(size);

        std::cout << "Running on |V| = " << size << std::endl;
        file  << "iter, cut, min_cut, runtime" << std::endl;
        int min_cut = g->E;
        for(int j = 0; j < iters; j++){


            auto start = high_resolution_clock::now();
            int cut = kargerMinCut(g);
            auto stop = high_resolution_clock::now();
            auto duration = duration_cast<nanoseconds>(stop - start);
            if(cut < min_cut){
                min_cut = cut;
            }
            file << j << ", " << cut << ", " << min_cut << ", " << duration.count() << std::endl;
        }
        printf("\n");
    }
    return 0;
}