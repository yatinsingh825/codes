#include <iostream>
using namespace std;

// Function to sort intervals based on the start time using bubble sort
void sortIntervals(int arr[][2], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j][0] > arr[j + 1][0]) {
                // Swap intervals
                int temp0 = arr[j][0];
                int temp1 = arr[j][1];
                arr[j][0] = arr[j + 1][0];
                arr[j][1] = arr[j + 1][1];
                arr[j + 1][0] = temp0;
                arr[j + 1][1] = temp1;
            }
        }
    }
}

// Function to merge overlapping intervals
int mergeOverlap(int arr[][2], int n, int result[][2]) {
    // Sort the intervals by start time
    sortIntervals(arr, n);

    // Initialize the result array index
    int resIndex = 0;

    // Add the first interval to the result array
    result[resIndex][0] = arr[0][0];
    result[resIndex][1] = arr[0][1];

    // Check for overlaps and merge intervals
    for (int i = 1; i < n; i++) {
        // If the current interval overlaps with the last interval in result
        if (arr[i][0] <= result[resIndex][1]) {
            // Merge the intervals by updating the end time
            result[resIndex][1] = max(result[resIndex][1], arr[i][1]);
        } else {
            // No overlap, move to the next interval
            resIndex++;
            result[resIndex][0] = arr[i][0];
            result[resIndex][1] = arr[i][1];
        }
    }

    // Return the number of merged intervals
    return resIndex + 1;
}

int main() {
    int arr[][2] = {{7, 8}, {1, 5}, {2, 4}, {4, 6}};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Result array to store merged intervals
    int result[10][2]; // Assuming at most 10 intervals for simplicity

    // Merge overlapping intervals
    int mergedCount = mergeOverlap(arr, n, result);

    // Print the merged intervals
    for (int i = 0; i < mergedCount; i++) {
        cout << result[i][0] << " " << result[i][1] << endl;
    }

    return 0;
}
