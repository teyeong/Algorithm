#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int makeOne(int N) {
    vector<int> dp(N + 1, 0);
    for (int i = 2; i <= N; i++) {
        // 1을 뺀 경우
        dp[i] = dp[i - 1] + 1;
        
        // 2로 나누어 떨어지는 경우
        if (i % 2 == 0) {
            dp[i] = min(dp[i], dp[i / 2] + 1);
        }
        
        // 3으로 나누어 떨어지는 경우
        if (i % 3 == 0) {
            dp[i] = min(dp[i], dp[i / 3] + 1);
        }
    }
    return dp[N];
}

int main()
{
    int N;
    cin >> N;
    cout << makeOne(N);
    
    return 0;
}