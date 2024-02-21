#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char s[100000], t[100000];
    while (cin >> s >> t) {
        int s_index = 0, cnt = 0;
        for (int i = 0; i < strlen(t); i++) {
            if (s[s_index] == t[i]) {
                cnt++;
                s_index++;
            }
        }
    
        if (strlen(s) == cnt) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }

    return 0;
}