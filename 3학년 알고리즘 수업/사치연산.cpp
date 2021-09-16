
#찾아라 프로그래밍 ㅇ마에스터 사칙연산
#include <vector>
#include <string>
#include <climits>

using namespace std;
int solution(vector<string> arr)
{
    int answer = 1;
    int dym[200][200][2] = { 0 };
    vector<int> op;

    for (int i = 0; i < size(arr); i++) {
        if (arr[i] == "+")
            op.push_back(1111);
        else if (arr[i] == "-") {
            op.push_back(2222);
        }
        else {
            op.push_back(atoi(arr.at(i).c_str()));
            dym[i][i][0] = op[i];
            dym[i][i][1] = op[i];
        }
    }
    for (int i = 2; i < size(arr); i = i + 2) {
        for (int j = 0; j < size(arr) - i; j = j + 2) {
            int max = 0;
            int min = 0;
            int max_n = -INT_MAX;
            int min_n = INT_MAX;
            for (int k = j + 1; k < i + j; k = k + 2) {
                if (op[k] == 1111) {
                    max = dym[j][k - 1][0] + dym[k + 1][i + j][0];
                    min = dym[j][k - 1][1] + dym[k + 1][i + j][1];
                    if (max > max_n) {
                        max_n = max;
                    }
                    if (min < min_n) {
                        min_n = min;
                    }
                }
                if (op[k] == 2222) {
                    max = dym[j][k - 1][0] - dym[k + 1][i + j][1];
                    min = dym[j][k - 1][1] - dym[k + 1][i + j][0];
                    if (max > max_n) {
                        max_n = max;
                    }
                    if (min < min_n) {
                        min_n = min;
                    }
                }
            }
            dym[j][j + i][0] = max_n;
            dym[j][j + i][1] = min_n;
        }

    }
    return dym[0][size(arr) - 1][0];
}
