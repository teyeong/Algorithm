#include <iostream>
#include <algorithm>

using namespace std;

int N, M;
int arr[9];
int result[9];

void dfs(int cnt) {
    if (cnt == M) {
        for (int i = 0; i < M; i++) {
            cout << result[i] << ' ';
        }
        cout << '\n';
        return;
    }
    for (int j = 0; j < N; j++) {
        if (arr[j] >= result[cnt - 1]) {
            result[cnt] = arr[j];
            dfs(cnt + 1);
        }
    }
}

int main () {
    cin >> N >> M;
    for (int k = 0; k < N; k++) {
        cin >> arr[k];
    }
    sort(arr, arr + N);
    dfs(0);
}