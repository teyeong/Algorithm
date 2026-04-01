#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(vector<vector<string>> plans) {
    vector<string> answer;
    
    // 시작 시간 순대로 정렬
    sort(plans.begin(), plans.end(), [](const vector<string>& a, const vector<string>& b) {
        return a[1] < b[1];
    });
    
    vector<vector<string>> waiting; // 잠시 멈춘 과제
    string current = ""; // 현재 과제 이름
    int time = 0; // 현재 시간
    long time_left = 0; // 남은 시간
    
    for (int i = 0; i < plans.size(); i++) {
        if (i == 0) { // 처음 과제
            current = plans[i][0];
            time = stoi(plans[i][1].substr(0, 2)) * 60 + stoi(plans[i][1].substr(3, 2));
            time_left = stoi(plans[i][2]);
        } else {
            int endTime = time_left + time; // 현재 과제가 끝나는 시간
            int nextTime = stoi(plans[i][1].substr(0, 2)) * 60 + stoi(plans[i][1].substr(3, 2)); // 새로운 과제가 시작하는 시간
            
            if (endTime < nextTime) {
                // 현재 과제가 먼저 끝날 경우
                answer.push_back(current);
                time = endTime;
                
                // waiting이 끊길 때까지 while문
                while (waiting.size() > 0) {
                    vector<string> lastTask = waiting.back();
                    waiting.pop_back();
                    current = lastTask[0];
                    time_left = stoi(lastTask[1]);
                    
                    endTime = time_left + time;

                    if (endTime < nextTime) {
                        // 현재 과제가 먼저 끝날 경우
                        answer.push_back(current);
                        time = endTime;
                    } else {
                        if (endTime == nextTime) {
                            answer.push_back(current);
                        } else {
                            // 새로운 과제 시작이 먼저일 경우
                            int prevTime = nextTime - time;
                            time_left -= prevTime;

                            vector<string> stopTask = { current, to_string(time_left) };
                            waiting.push_back(stopTask);
                        }
                        // while문 탈출
                        break;
                    }
                }
                
                // 새로운 과제 시작하기
                current = plans[i][0];
                time = nextTime;
                time_left = stoi(plans[i][2]);
            
            } else {               
                if (endTime == nextTime) {
                    // 과제 끝
                    answer.push_back(current);
                } else {
                    // 새로운 과제 시작이 먼저일 경우
                    int prevTime = nextTime - time;
                    time_left -= prevTime;
                    
                    vector<string> stopTask = { current, to_string(time_left) };
                    waiting.push_back(stopTask);   
                }             
                current = plans[i][0];
                time = nextTime;
                time_left = stoi(plans[i][2]);
            }
        }
    }
    
    // 현재 수행 중인 과제 먼저 끝내기
    answer.push_back(current);
    
    // 잠시 멈춘 과제 다 끝내기
    while (!waiting.empty()) {
        answer.push_back(waiting.back()[0]);
        waiting.pop_back();
    }
    
    return answer;
}