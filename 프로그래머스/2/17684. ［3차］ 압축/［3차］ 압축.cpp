#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(string msg) {
    vector<int> answer;
    
    map<string, int> dictionary;
    int i;
    for (i = 1; i <= 26; i++) {
        string letter(1, static_cast<char>(i + 64)); 
        dictionary[letter] = i;
    }
    
    string curr = "";
    curr += msg[0];
    
    int idx = 0;
    while (msg.length() > 0) {
        if (dictionary.find(curr) != dictionary.end()) { // 있는 경우
            if (idx < msg.length() - 1) {
                curr += msg[++idx];
            } else { // 마지막인 경우
                answer.push_back(dictionary[curr]);
                msg.erase(0, curr.length());
                idx = 0;
                if (msg.length() > 0) {
                    curr = "";
                    curr += msg[0];
                }
            }
        } else { // 없는 경우
            string prev = curr.substr(0, curr.length() - 1);
            if (dictionary.find(prev) != dictionary.end()) { // 이전 단어가 사전에 있음
                answer.push_back(dictionary[prev]);
                msg.erase(0, prev.length());
                dictionary[curr] = i++;
                idx = 0;
                if (msg.length() > 0) {
                    curr = "";
                    curr += msg[0];
                }
            }
        }
    }
    
    return answer;
}