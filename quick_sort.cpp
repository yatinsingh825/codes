#include <iostream>
using namespace std;

// Partition function
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Pivot element
    int i = low - 1;       // Index of smaller element
    for (int j = low; j < high; j++) { // Iterate through the array
        if (arr[j] <= pivot) {
            i++; // Increment index of smaller element
            swap(arr[i], arr[j]); // Swap elements
        }
    }
    swap(arr[i + 1], arr[high]); // Place the pivot element in the correct position
    return i + 1; // Return the partition index
}

// QuickSort function
void quick_sort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high); // Partitioning index
        quick_sort(arr, low, pi - 1);       // Sort left subarray
        quick_sort(arr, pi + 1, high);      // Sort right subarray
    }
}

int main() {
    int arr[] = {10, 80, 30, 90, 40, 50, 70}; // Declare array
    int n = sizeof(arr) / sizeof(arr[0]);     // Calculate size of array

    quick_sort(arr, 0, n - 1); // Perform QuickSort

    // Print sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
