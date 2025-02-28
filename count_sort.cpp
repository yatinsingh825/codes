#include<iostream>
#include<vector>
#include<climits>  

using namespace std;

void countsort(vector<int> &v) {
    int n = v.size();  
    vector<int> ans(n);
    int max_ele = INT_MIN; 

    for(int i = 0; i < n; i++) {
        max_ele = max(v[i], max_ele);
    }

    vector<int> freq(max_ele + 1, 0);

    for(int i = 0; i < n; i++) {
        freq[v[i]]++;
    }

    for(int i = 1; i <= max_ele; i++) {  
        freq[i] += freq[i - 1];
    }

    for(int i = n - 1; i >= 0; i--) {  
        ans[--freq[v[i]]] = v[i];
    }

    for(int i = 0; i < n; i++) {
        v[i] = ans[i];
    }
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);  

    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    countsort(arr);
    
    cout << "Sorted arr: ";  
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";  
    }
    cout << endl;  

    return 0;
}
