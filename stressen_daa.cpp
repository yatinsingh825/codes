#include <iostream>
using namespace std;

void display(int C[2][2]) {
    for(int i=0; i<2; i++) {
        for(int j=0; j<2; j++) {
            cout<<"C"<<i+1<<j+1<<": "<<C[i][j]<<endl;
        }
    }
}

void strassen(int A[2][2], int B[2][2], int C[2][2]) {
    int P1 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1]);
    int P2 = (A[1][0] + A[1][1]) * B[0][0];
    int P3 = A[0][0] * (B[0][1] - B[1][1]);
    int P4 = A[1][1] * (B[1][0] - B[0][0]);
    int P5 = (A[0][0] + A[0][1]) * B[1][1];
    int P6 = (A[1][0] - A[0][0]) * (B[0][0] + B[0][1]);
    int P7 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1]);

    C[0][0] = P1 + P4 - P5 + P7;
    C[0][1] = P3 + P5;
    C[1][0] = P2 + P4;
    C[1][1] = P1 - P2 + P3 + P6;
}

int main() {
    cout<<"Shardul Malhotra  23BAI70218"<<endl;
    int A[2][2], B[2][2], C[2][2];
    
    cout<<"Enter elements for first matrix:"<<endl;
    for(int i=0; i<2; i++)
        for(int j=0; j<2; j++)
            cin>>A[i][j];
            
    cout<<"Enter elements for second matrix:"<<endl;
    for(int i=0; i<2; i++)
        for(int j=0; j<2; j++)
            cin>>B[i][j];
            
    strassen(A, B, C);
    display(C);
    
    return 0;
}