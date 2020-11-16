#include <vector>
#include <climits>
#include <iostream>

using namespace std;
void matrix(int n, vector<int> v, vector < vector <unsigned long long> >& m) {


    for (int i = 1; i <= n; i++) {
        m[i][i] = 0;
    }
    for (int l = 2; l <= n; l++) {
        for (int i = 1; i <= n - l + 1; i++) {
            int j = i + l - 1;
            m[i][j] = 18446744073709551615;
            for (int k = i; k <= j - 1; k++) {
                unsigned long long q = m[i][k] + m[k + 1][j] + v[i - 1] * v[k] * v[j];
                if (q < m[i][j]) {
                    m[i][j] = q;

                }
            }
        }
    }
}

int main(void) {
    int n;
    vector<int> v;

    cin >> n;
    for (int i = 0; i < n + 1; i++) {
        int d;
        cin >> d;
        v.push_back(d);
    }
    vector<vector<unsigned long long>> m(1001, vector<unsigned long long>(1001, 0));
    matrix(n, v, m);
    cout << m[1][n];

    // solve here and print the result using cout 
    return 0;
}