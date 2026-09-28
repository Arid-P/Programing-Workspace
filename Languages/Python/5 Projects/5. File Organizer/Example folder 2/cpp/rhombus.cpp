#include <iostream>
using namespace std;

int main(){
    int r, c;
    cin >> r >> c;

    for(int i=1; i<=r; i++){
        int j;
        for(j=1; j<=(r-i); j++)
            cout << " ";

        for(j=1; j<=c; j++)
            cout << "*";
        cout << endl;
    }
    
    return 0;
}