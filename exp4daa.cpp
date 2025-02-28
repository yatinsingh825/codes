#include <iostream>

using namespace std;

struct Edge {
    int u, v, weight;
};

int findParent(int node, int parent[]) {
    while (parent[node] != -1)
        node = parent[node];
    return node;
}

void unionSets(int u, int v, int parent[]) {
    parent[findParent(u, parent)] = findParent(v, parent);
}

void kruskal(Edge edges[], int V, int E) {
    // Simple Bubble Sort for edges based on weight
    for (int i = 0; i < E - 1; i++) {
        for (int j = 0; j < E - i - 1; j++) {
            if (edges[j].weight > edges[j + 1].weight) {
                Edge temp = edges[j];
                edges[j] = edges[j + 1];
                edges[j + 1] = temp;
            }
        }
    }

    int parent[V]; 
    for (int i = 0; i < V; i++) parent[i] = -1;

    int minCost = 0, count = 0;
    cout << "MST Edges:\n";
    
    for (int i = 0; i < E && count < V - 1; i++) {
        if (findParent(edges[i].u, parent) != findParent(edges[i].v, parent)) {
            cout << edges[i].u << " - " << edges[i].v << " : " << edges[i].weight << endl;
            minCost += edges[i].weight;
            unionSets(edges[i].u, edges[i].v, parent);
            count++;
        }
    }

    cout << "Minimum Cost: " << minCost << endl;
}

int main() {
    cout << "Yatin Singh 23BAI70025" << endl;
    int V = 4, E = 5;
    Edge edges[] = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};

    kruskal(edges, V, E);
    return 0;
}
