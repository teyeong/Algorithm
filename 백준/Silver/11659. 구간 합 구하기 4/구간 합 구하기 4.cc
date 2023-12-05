#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N, M, i, j, a, b;
    cin >> N >> M;
    int num[N], sum[N] = {0};
    
    for(i = 0; i < N; i++) {
        cin >> num[i];
        sum[i] = sum[i-1] + num[i];
    }

    for(i = 0; i < M; i++) {
        cin >> a >> b;
        cout << sum[b - 1] - sum[a - 2] << "\n";
    }
    
    return 0;
}