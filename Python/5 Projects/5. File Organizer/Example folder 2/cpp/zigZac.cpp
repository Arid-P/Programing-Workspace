#include <iostream>
using namespace std;

int main(){
    int r;
    cin >> r;

    for(int i=1; i<=3; i++){
        int j;
        for(j=1; j<=r; j++){
            if(i==2 && (i+j)%2==0){
                cout << "*";
            }
        	else if(i!=2 && (i+j)%4==0){
                cout << "*";
            }
            else{
                cout << " ";
            }
        }
        cout << endl;
    }

    return 0;
}