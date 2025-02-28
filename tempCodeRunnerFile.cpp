#include <iostream>
using namespace std;
int arr[5];
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
int partition(int l, int h) {
    int pivot = arr[h]; 
    int i = l - 1;      
    int j = h;        
    while (true) {
        do {
            i++;
        } while (arr[i] <= pivot);
        do {
            j--;
        } while (arr[j] > pivot);

        if (i >= j) {
            swap(&arr[i], &arr[h]); 
            return i;
        }

        swap(&arr[i], &arr[j]);
    }
}

void quick_sort(int l, int h) {
    if (l < h) {
        int j = partition(l, h); 
        quick_sort(l, j - 1);    
        quick_sort(j + 1, h);    
    }
}

int main() {
    cout << "Enter 5 elements: ";
    for (int i = 0; i < 5; i++) {
        cin >> arr[i];
    }

    cout << "\nArray before sorting: ";
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    quick_sort(0, 4);

    cout << "\nSorted array: ";
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
