/* Dijkstra.cpp */
#include <string>
#include <vector>
using namespace std;
#define INF 999

void findPathDijkstra(vector<int> parent, int src, string& path) {
  if (parent[src] == -1) return;
  findPathDijkstra(parent, parent[src], path);
  path += "->" + to_string(src + 1);
}

vector<string> Dijsktra(vector<vector<int>>& graph, int start, int end) {
  vector<string> result(2);
  start--;
  end--;
  size_t V = graph.size();
  vector<int> D(V, INF);
  vector<bool> T(V, true);
  vector<int> P(V);
  D[start] = 0;
  P[start] = -1;

  while (T[end]) {
    int min_length = INF;
    int min_index = start;
    for (size_t i = 0; i < V; i++) {
      int weight = D[i] + graph[min_index][i];
      if (T[i] && weight < min_length) {
        min_length = D[i];
        min_index = i;
      }
    }
    T[min_index] = false;

    for (size_t i = 0; i < V; i++) {
      if (T[i] && graph[min_index][i] > 0) {
        int weight = D[min_index] + graph[min_index][i];
        if (weight < D[i]) {
          P[i] = min_index;
          D[i] = weight;
        }
      }
    }
  }
  result[0] = to_string(start + 1);
  findPathDijkstra(P, end, result[0]);
  result[1] = to_string(D[end]);
  return result;
}