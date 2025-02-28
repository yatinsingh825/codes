#include <iostream>
using namespace std;

int main() {
    int arr[] = {7, 10, 1, 3, 6, 9, 2};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    
    int largest = arr[n - 1];
    int smallest = arr[0];
    cout << "Sell at " << largest << ", buy at " << smallest << ", profit = " << largest - smallest << endl;
    
    return 0;
}
