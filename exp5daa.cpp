#include <iostream>
#include <algorithm>

using namespace std;

struct Job {
    char id;
    int deadline, profit;
};

bool compare(Job a, Job b) {
    return a.profit > b.profit;
}

void jobSequencing(Job arr[], int n) {
    sort(arr, arr + n, compare);
    
    int result[n];
    bool slot[n] = {false};
    
    for (int i = 0; i < n; i++) {
        for (int j = min(n, arr[i].deadline) - 1; j >= 0; j--) {
            if (!slot[j]) {
                result[j] = i;
                slot[j] = true;
                break;
            }
        }
    }

    cout << "Optimal job sequence: ";
    for (int i = 0; i < n; i++)
        if (slot[i])
            cout << arr[result[i]].id << " ";
}

int main() {
    cout << "Yatin Singh 23BAI70025" << endl;
    Job arr[] = {{'A', 2, 100}, {'B', 1, 50}, {'C', 2, 10}, {'D', 1, 20}, {'E', 3, 30}};
    int n = sizeof(arr) / sizeof(arr[0]);

    jobSequencing(arr, n);
    return 0;
}
