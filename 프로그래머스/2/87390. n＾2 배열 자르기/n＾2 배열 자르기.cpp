#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, long long left, long long right) {
    vector<int> answer;
    int a = int(left / n);
    int b = left % n;
    
    for (int i = 0; i < right - left + 1; i++) {
        answer.push_back(a > b ? a + 1 : b + 1);
        if (b > n - 2) {
            b = 0;
            a++;
        } else {
            b++;
        }
    }
    
    return answer;
}