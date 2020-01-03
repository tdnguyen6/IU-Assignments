/* Floyd.cpp */
#include <string>
#include <vector>
using namespace std;
#define INF 999

void findPathFloyd(vector<vector<int>> parents, int start, int end, string& path) {
  if (start == end)
    path += "->" + to_string(start + 1);
  else if (parents[start][end] == -1)
    path += to_string(start + 1) + "->" + to_string(end + 1);
  else {
    findPathFloyd(parents, start, parents[start][end], path);
    path += "->" + to_string(end + 1);
  }
}

vector<string> Floyd(vector<vector<int>>& graph, int start, int end) {
  vector<string> result(2);
  vector<vector<int>> D;
  vector<vector<int>> P;
  start--;
  end--;
  size_t V = graph.size();
  for (size_t i = 0; i < V; i++) {
    vector<int> tmp;
    vector<int> tmp2;
    for (size_t j = 0; j < V; j++) {
      tmp2.push_back(i);
      if (graph[i][j] == 0) {
        graph[i][j] = INF;
        if (i != j) tmp2[j] = -1;
      }
      tmp.push_back(graph[i][j]);
    }
    D.push_back(tmp);
    P.push_back(tmp2);
  }

  for (size_t k = 0; k < V; k++) {
    for (size_t i = 0; i < V; i++) {
      for (size_t j = 0; j < V; j++) {
        if (D[i][k] + D[k][j] < D[i][j]) {
          D[i][j] = D[i][k] + D[k][j];
          P[i][j] = P[k][j];
        }
      }
    }
  }

  findPathFloyd(P, start, end, result[0]);
  result[1] = to_string(D[start][end]);
  return result;
}