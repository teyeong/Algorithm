#include <iostream>

using namespace std;

int main()
{
    int income = 0, outcome = 0, sum = 0, max = 0;
    
    for (int i = 0; i < 4; i++) {
        cin >> outcome >> income;
        sum += income - outcome;
        if (sum > max) {
            max = sum;
        }
    }
    
    cout << max;
    

    return 0;
}