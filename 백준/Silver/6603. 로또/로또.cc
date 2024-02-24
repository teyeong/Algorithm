#include <iostream>

using namespace std;

void dfs(int cnt, int k, int arr[], int S[], bool visited[]) {
    if (cnt == 7) {
        for (int i = 1; i < 7; i++) {
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return;
    }
    for (int j = 0; j < k; j++) {
        if (!visited[S[j]] && S[j] > arr[cnt - 1]) {
            visited[S[j]] = true;
            arr[cnt] = S[j];
            dfs(cnt + 1, k, arr, S, visited);
            visited[S[j]] = false;
        }
    }
}

int main () {
    
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    while (1) {
        int k;
        cin >> k;
        if (!k) {
            break;
        }
        int S[k];
        int arr[7] = {0, };
        bool visited[50] = {0, };
        for (int i = 0; i < k; i++) {
            cin >> S[i];
        }
        dfs(1, k, arr, S, visited);
        cout << '\n';
    }
    
    return 0;
}