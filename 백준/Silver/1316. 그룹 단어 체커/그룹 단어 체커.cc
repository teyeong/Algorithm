#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    cin >> N;
    int cnt = 0;
    for (int i = 0; i < N; i++) {
        char word[101];
        int result = 0;
        vector<char> V;
        cin >> word;
        for (int j = 0; j < strlen(word) - 1; j++) {
            if (word[j] != word[j+1]) {
                V.push_back(word[j]);
                if (find(V.begin(), V.end(), word[j + 1]) != V.end()) {
                    result = 1;
                }
            }
        }
        if (!result) {
            cnt++;
        }
    }
    
    cout << cnt;
    return 0;
}