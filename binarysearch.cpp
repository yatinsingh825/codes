#include <iostream>
using namespace std;

int binary_search(int start, int end, int key, int arr[]) {
    while (start <= end) {
        int mid = start + (end - start) / 2; 
        
        if (arr[mid] == key)
            return mid; 

      
        if (arr[mid] > key)
            end = mid - 1;
        else /
            start = mid + 1;
    }
    return -1; 
}

int main() {
    cout<<"Yatin Singh 23BAI70025"<<endl;
    int arr[5];
    int key;
    for(int i = 0;i<5;i++){
        cin>>arr[i];
    }
    cout<<"array:";
    for(int i = 0;i<5;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    


    cout << "Enter the key to search: ";
    cin >> key;


    int result = binary_search(0, 4, key, arr);

    if (result != -1)
        cout << "Key found at index: " << result << endl;
    else
        cout << "Key not found" << endl;

    return 0;
}
