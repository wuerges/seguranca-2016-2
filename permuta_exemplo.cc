#include <iostream>
#include <vector>
using namespace std;

int main() {

  vector<char> simbolos = {'1', '2', '3', '4', '5', '6', '7', '8', 'a', 'b', 'c', 'd'};


  // ao cubo porque são 3 símbolos
  int sz = simbolos.size();
  int n = sz * sz * sz;

  for(int i = 0; i < n; ++i) {
    int p1 = i % sz;
    int p2 = (i / sz) % sz;
    int p3 = (i / sz / sz) % sz;
    cout << simbolos[p1] << simbolos[p2] << simbolos[p3] << "\n";
  }

  return 0;
}
