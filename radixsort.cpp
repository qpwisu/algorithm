#include <iostream>
#include <string>
#include <vector>
#include <utility>
using namespace std;

int digit16(int v, int d) {
	// 양의 정수 v 의 16진수 d 번째 숫자를 반환하는 함수
	// 예를 들어 v 의 값이 78320238 (= 0x04ab126e) 이고 d 가 1 이라면 6 을 반환
	// 예를 들어 v 의 값이 78320238 (= 0x04ab126e) 이고 d 가 4 라면 11 (= 0xb) 을 반환
	v = v >> d * 4;
	return v & 0xf;
}

void countingSort16(vector<pair<int, string> >& v, int d);

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
	//radixsort
	for (int d = 0; d < 8; d++) countingSort16(v, d);

	for (int i = 0; i < n; i++) {
		cout << v[i].first << ' ' << v[i].second << endl;
	}
	return 0;
}

void countingSort16(vector<pair<int, string> >& v, int d)
{
	vector<pair<int, string>> origin;
	vector<int> count;

	for (int i = 0; i < 16; i++)
		count.push_back(0);

	for (int i = 0; i < v.size(); i++)
		origin.push_back(v[i]);

	for (int i = 0; i < origin.size(); i++)
		count[digit16(origin[i].first, d)] += 1;

	for (int i = 1; i < 16; i++)
		count[i] += count[i - 1];

	for (int i = origin.size() - 1; i >= 0; i--)
	{
		v[count[digit16(origin[i].first, d)] - 1] = origin[i];
		count[digit16(origin[i].first, d)] -= 1;
	}
}




#radixsort 내가 쓴거
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <queue>
#include<cmath>
#include<cstring>
using namespace std;



void reverseString(char* s) {	// 문자열의 앞뒤를 reverse
	int size1 = strlen(s);
	char temp;
	for (int i = 0; i < size1 / 2; i++) {
		temp = s[i];
		s[i] = s[(size1 - 1) - i];
		s[(size1 - 1) - i] = temp;
	}
}
int digit16(int v, int d) {
	// 양의 정수 v 의 16진수 d 번째 숫자를 반환하는 함수
	// 예를 들어 v 의 값이 78320238 (= 0x04ab126e) 이고 d 가 1 이라면 6 을 반환
	// 예를 들어 v 의 값이 78320238 (= 0x04ab126e) 이고 d 가 4 라면 11 (= 0xb) 을 반환
	v = v >> d * 4;
	return v & 0xf;
}
void dec2hex(int d, char* buf) {
	int i = 0;
	char code[] = { '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F' };
	do {
		buf[i++] = code[d % 16];
	} while ((d /= 16) > 0);

	buf[i] = '\0';
	reverseString(buf);
}
void countingSort16(vector<pair<int, string> >& v, int d) {
	queue<pair<int, string>> que[16];
	for (int i = 0; i < v.size(); i++) {
		char cv[10];
		int aaa = v[i].first;
		dec2hex(aaa, cv); //백터에든 숫자를 16진수로 변환	
		int lencv = 0;
		for (int x = 0; x < 10; x++) {
			if (cv[x] == '\0') {
				lencv = x;

				break;
			}
		}
		if (d > lencv - 1) { //d보다 자리수가 적은경우는 que[0]에 넣어줌 
			que[0].push(pair<int, string>(v[i].first, v[i].second));
			continue;
		}

		// 16진수로 변환된것에 d번째 자리를 0~16큐에 알맞게 푸쉬 
		int xxx = lencv - (d + 1);
		char cxx = cv[xxx];
		if (cxx >= 'A' && cxx <= 'F') {
			cxx = cxx - 17;
			int m = cxx - '0';
			m = m + 10;
			que[m].push(pair<int, string>(v[i].first, v[i].second));
			continue;
		}
		int m = cxx - '0';

		que[m].push(pair<int, string>(v[i].first, v[i].second));
	}
	//큐에 들어있는걸 0~16을 차례대로 빼서 벡터에저장 
	int aa = 0;
	for (int x = 0; x < 16; x++) {
		if (que[x].size() == 0) {
			continue;
		}
		while (!que[x].empty())
		{
			v[aa] = que[x].front();
			que[x].pop();
			aa++;
		}
	}
}


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
	//radixsort
	for (int d = 0; d < 8; d++) countingSort16(v, d);

	for (int i = 0; i < n; i++) {
		cout << v[i].first << ' ' << v[i].second << endl;
	}
	return 0;

}