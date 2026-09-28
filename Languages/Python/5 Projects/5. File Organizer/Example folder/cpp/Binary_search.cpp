#include <iostream>
using namespace std;

int search(int arr[], int s, int e, int key){
    int mid = (e - s) / 2;
    
    if(arr[mid] == key){
      return mid;
    }
    else if(arr[mid] > key){
      st = mid + 1;
      return search(arr, st, e, key);
    }
    else if(arr[mid] < key){
      e = mid - 1;
      return search(arr, st, e, key);
    }
    else{
      return -1;
    }
}

int start(int arr[], int s, int key){
    int st=0; e=s-1;
    int mid = (e - s) / 2;
    
    if(arr[mid] == key){
      return mid;
    }
    else if(arr[mid] > key){
      st = mid + 1;
      return search(arr, st, e, key);
    }
    else if(arr[mid] < key){
      e = mid - 1;
      return search(arr, st, e, key);
    }
}

int main() {
    int s, key;
    cin >> s;

    int arr[s];
    for(int i=0; i<s; i++)
    	cin >> arr[i];

    cout << "Enter the key\n";
    cin >> key;
    
    cout << start(arr, s, key) << endl;
    
    return 0;
}