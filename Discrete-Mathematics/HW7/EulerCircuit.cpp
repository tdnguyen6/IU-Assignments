#include <iostream>
#include <vector>
using namespace std;

void findEulerPath(int vertices, int* edges, bool directed, int start,
                   vector<int>& answer) {
  for (int next = 0; next < vertices; next++) {
    if (*((edges + start * vertices) + next) > 0) {
      *((edges + start * vertices) + next) -= 1;
      if (!directed) *((edges + next * vertices) + start) -= 1;
      findEulerPath(vertices, edges, directed, next, answer);
    }
  }
  answer.push_back(start);
}

int main(int argc, char const* argv[]) {
  const int vertices = 10;
  int edges[vertices][vertices] = {
      {0, 1, 1, 0, 0, 0, 0, 0, 0, 0}, {1, 0, 1, 1, 1, 0, 0, 0, 0, 0},
      {1, 1, 0, 0, 1, 1, 0, 0, 0, 0}, {0, 1, 0, 0, 1, 0, 1, 1, 0, 0},
      {0, 1, 1, 1, 0, 1, 0, 1, 1, 0}, {0, 0, 1, 0, 1, 0, 0, 0, 1, 1},
      {0, 0, 0, 1, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 1, 1, 0, 1, 0, 1, 0},
      {0, 0, 0, 0, 1, 1, 0, 1, 0, 1}, {0, 0, 0, 0, 0, 1, 0, 0, 1, 0}};

  vector<int> EulerCircuit;
  int start_vertice;
  cout << "Input starting vertice: ";
  cin >> start_vertice;
  findEulerPath(vertices, (int*)edges, false, start_vertice - 1, EulerCircuit);

  cout << "Euler path is: ";
  for (int i = 0; i < EulerCircuit.size(); i++) {
    cout << EulerCircuit[i] + 1;
    if (i < EulerCircuit.size() - 1) cout << "->";
  }

  return 0;
}
