#include <iostream>
#include <queue>

using namespace std;

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int N, x;
    cin >> N;
    
    priority_queue<int> arr;
    
    for (int i = 0; i < N; i++) {
        cin >> x;
        if (x) {
            arr.push(x);
        } else {
            if (arr.empty()) {
                cout << 0 << '\n';
            } else {
                cout << arr.top() << '\n';
                arr.pop();
            }
        }
    }

    return 0;
}