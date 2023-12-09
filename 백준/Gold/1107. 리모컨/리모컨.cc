#include <iostream>
#include <string>

using namespace std;

int error[10] = {0, };

bool setBtn(int n) {
    string str_n = to_string(n);
    for (int i = 0; i < str_n.length(); i++) {
        if (error[str_n[i] - '0'] == 1) {
            return false;
        }
    }
    return true;
}

int main()
{
    int N, M;
    cin >> N >> M;
    
    int current = 100;
    
    for (int i = 0; i < M; i++) {
        int k;
        cin >> k;
        error[k] = 1;
    }
    
    int cnt = abs(current - N);
    
    for (int j = 0; j <= 1000000; j++) {
        if (setBtn(j) == true) {
            int second_cnt = abs(N - j) + to_string(j).length();
            cnt = min(cnt, second_cnt);
        }
    }
    
    cout << cnt;

    return 0;
}