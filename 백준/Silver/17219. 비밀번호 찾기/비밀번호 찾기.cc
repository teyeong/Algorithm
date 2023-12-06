#include <iostream>
#include <unordered_map>

using namespace std;

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    unordered_map<string, string> memo;
    
    int N, M;
    cin >> N >> M;
    
    string savedSite, pw;
    for (int i = 0; i < N; i++) {
        cin >> savedSite >> pw;
        memo.insert(make_pair(savedSite, pw));
    }
    
    unordered_map<string, string>::iterator iter;
    string site;
    for (int j = 0; j < M; j++) {
        cin >> site;
        auto ans = memo.find(site);
        if (ans != memo.end()) {
            cout << ans->second << '\n';
        }
    }
    
    return 0;
}