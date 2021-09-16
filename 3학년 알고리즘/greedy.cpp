#include<vector>
#include<algorithm>
#include <iostream>

using namespace std;
bool compare(const vector<int>& v1, const vector<int>& v2)
{
    if (v1[1] == v2[1]) {
        return v1[0] < v2[0];
    }

    return v1[1] < v2[1];
}

int solution(vector<vector<int> > arr)
{
    sort(arr.begin(), arr.end(), compare);

    int n = arr.size();
    vector<int> a = { 0 };
    int k = 0;
    for (int m = 1; m < n; m++) {
        if (arr[m][0] >= arr[k][1]) {
            a.push_back(arr[m][0]);
            k = m;
        }
    }

    int answer = a.size();
    return answer;
}
