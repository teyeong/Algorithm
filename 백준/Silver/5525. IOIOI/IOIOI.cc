#include <iostream>

using namespace std;

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int N, M;
    cin >> N >> M;

    char S[M];
    for (int i = 0; i < M; i++) {
        cin >> S[i];
    }
    
    int ans = 0;
    
    for (int j = 0; j < M; j++) {
        int cnt = 0;
        if (S[j] == 'I') {
            while (S[j + 1] == 'O' && S[j + 2] == 'I') {
                cnt++;
                if (cnt == N) {
                    ans++;
                    cnt--;
                }
                j += 2;
            }
        }
    }
    
    cout << ans;

    return 0;
}