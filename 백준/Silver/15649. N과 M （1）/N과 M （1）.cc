#include <iostream>

using namespace std;

int N, M;
int arr[9];
bool visited[9];

void dfs(int cnt) {
    if (cnt == M) {
        for (int i = 0; i < M; i++) {
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return;
    }
    for (int j = 1; j <= N; j++) {
        if (!visited[j]) {
            visited[j] = 1;
            arr[cnt] = j;
            dfs(cnt + 1);
            visited[j] = false;
        }
    }
}

int main () {
    cin >> N >> M;
    dfs(0);
    return 0;
}