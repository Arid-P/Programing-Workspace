#include <iostream>
using namespace std;

int search(int arr[], int s, int key){
    for(int i=0; i<s; i++)
    	if(arr[i] == key)
            return i;
    
    return -1;
}

int main() {
    int s, key;
    cin >> s;

    int arr[s];
    for(int i=0; i<s; i++)
    	cin >> arr[i];

    cout << "Enter the key\n";
    cin >> key;
    
    cout << search(arr, s, key) << endl;
    
    return 0;
}