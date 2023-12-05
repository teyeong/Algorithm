#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    // 수행해야 하는 연산의 수
    int M;
    cin >> M;
    
    string command;
    int S[21] = {0, }, num;
    
    for (int i = 0; i < M; i++) {
        cin >> command;
        if (command == "add") {
            cin >> num;
            if (!S[num]) {
                S[num] = 1;
            }
        } else if (command == "remove") {
            cin >> num;
            if (S[num]) {
                S[num] = 0;
            }            
        } else if (command == "check") {
            cin >> num;
            cout << S[num] << '\n';   
        } else if (command == "toggle") {
            cin >> num;
            if (S[num]) {
                S[num] = 0;
            } else {
                S[num] = 1;
            }
        } else if (command == "all") {
            fill_n(S, 21, 1);
        } else if (command == "empty") {
            fill_n(S, 21, 0);
        }
    }

    return 0;
}