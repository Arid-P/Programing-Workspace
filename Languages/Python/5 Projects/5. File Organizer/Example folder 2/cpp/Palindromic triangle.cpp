//this one is mine, theirs is different
#include <iostream>
using namespace std;

int main(){
  int r, i, j;
  cin>>r;
  
  for(i=1; i<=r; i++){
    int space = r - i;
    for(j=1; j<=space; j++)
      cout << "   ";
      
    for(j=i; j>=1; j--)
      cout << j << " ";
      
    for(j=2; j<=i; j++){
      cout << j << " ";
      
    cout << endl;
  }
  
  return 0;
}