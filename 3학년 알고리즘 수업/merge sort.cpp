#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <climits>
#include<algorithm>
#include<cmath>
using namespace std;
int main(void) {
	int n;
	vector<pair<int, string> > v;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int d;
		string s;
		cin >> d >> s;
		v.push_back(pair<int, string>(d, s));
	}
	// merge sort
	int p = 0;
	int r = v.size() - 1;
	int q = floor(r / 2);
	int n1 = q - p;
	int n2 = r - q;
	vector<pair<int, string> > v1;
	vector<pair<int, string> > v2;
	for (int i = 0; i <= n1; i++) {
		v1[i] = v[i];
	}
	for (int i = 0; i + n1 + 1 <= r; i++) {
		v2[i] = v[i + n1 + 1];
	}
	int x = 0;
	int m = 0;
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	for (int k = 0; k <= r; k++) {
		if (v1[x].first <= v2[m].first) {
			v[k] = v1[x];
			n += 1;
		}
		else {
			v[k] = v2[x];
			m += 1;
		}

	}



	for (int i = 0; i < n; i++) {
		cout << v[i].first << ' ' << v[i].second << endl;
	}

	return 0;
}

