#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    int arr[n];
    fill_n(arr, n, 1);
    
    int lost_len = lost.size();
    int res_len = reserve.size();
    for (int i = 0; i < lost_len; i++) {
        arr[lost[i] - 1] -= 1;
    }
    for (int j = 0; j < res_len; j++) {
        arr[reserve[j] - 1] += 1;
    }

    for (int k = 0; k < n; k++) {
        if (arr[k] == 0) {
            if (k - 1 >= 0 && arr[k - 1] > 1) {
                arr[k] += 1;
                arr[k - 1] -= 1;
                answer += 1;
            } else if (k + 1 < n && arr[k + 1] > 1) {
                arr[k] += 1;
                arr[k + 1] -= 1;
                answer += 1;
            }
        } else {
            answer += 1;
        }
    }
    
    return answer;
}