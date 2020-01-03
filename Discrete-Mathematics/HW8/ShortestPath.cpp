#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>
#include "Dijkstra.cpp"
#include "Floyd.cpp"
using namespace std;

int main() {
  istream& input = cin;
  /*  Change the above line to:
        ifstream file("/path/to/data/file");
        istream& input = file;
      to input big adjacency matrices from file. */

  int verticeNum, start, end;
  cout << "Input number of vertices: ";
  input >> verticeNum;

  vector<vector<int>> adjacencyMatrix;
  cout << endl << "Input adjacency matrix" << endl;
  for (int i = 0; i < verticeNum; i++) {
    vector<int> tmp;
    for (int j = 0; j < verticeNum; j++) {
      int tmp_length;
      cout << "Input row " << i + 1 << " column " << j + 1 << ": ";
      input >> tmp_length;
      tmp.push_back(tmp_length);
    }
    adjacencyMatrix.push_back(tmp);
  }

  cout << "Your input matrix is: " << endl;
  for (int i = 0; i < verticeNum; i++) {
    for (int j = 0; j < verticeNum; j++)
      cout << setw(2) << adjacencyMatrix[i][j] << " ";
    cout << endl;
  }

  cout << "Input starting vertice: ";
  input >> start;
  cout << "Input destination vertice: ";
  input >> end;

  vector<string> result = Dijsktra(adjacencyMatrix, start, end);
  // Or change the above line to this for Floyd algorithm
  // vector<string> result = Floyd(adjacencyMatrix, start, end);

  cout << endl;
  cout << "Shortest path is: " << result[0] << endl;
  cout << "Shortest path length: " << result[1] << endl;
  return 0;
}