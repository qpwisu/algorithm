#include <iostream>
#include <string>
#include <vector>
#include <utility>

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

	// insertion sort
	for (int j = 1; j < n; j += 1) {

		int key = v[j].first;
		string key2 = v[j].second;

		int x = j - 1;
		while (x >= 0 && v[x].first > key) {
			v[x + 1] = v[x];
			x = x - 1;

		}
		v[x + 1].first = key;
		v[x + 1].second = key2;
	}



	// output 
	for (int i = 0; i < n; i++) {
		cout << v[i].first << ' ' << v[i].second << endl;
	}

	return 0;
}
