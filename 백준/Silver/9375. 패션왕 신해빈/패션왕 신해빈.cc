#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    int tk;
    cin >> tk;

    for (int i = 0; i < tk; i++) {
        int n, cnt = 0;
        cin >> n;

        unordered_map<string, int> counts;

        for (int j = 0; j < n; j++) {
            string name, category;
            cin >> name >> category;
            counts[category]++;
        }

        int result = 1;
        for (const auto& pair : counts) {
            result *= (pair.second + 1);
        }

        cnt += result - 1; // 모든 종류를 입지 않는 경우를 뺀다

        cout << cnt << '\n';
    }

    return 0;
}