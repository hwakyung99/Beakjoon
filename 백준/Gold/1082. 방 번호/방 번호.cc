#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

bool cmp(pair<int, int>& a, pair<int, int>& b) {
	if (a.first == b.first) {
		return a.second > b.second;
	}
	return a.first < b.first;
}

int main() {
	int N, M;
	vector<pair<int, int>> pP;
	int iP[10];
	string ans = "";

	cin >> N;
	
	int p;
	for (int i = 0; i < N; i++) {
		cin >> p;
		pP.push_back(make_pair(p, i));
		iP[i] = p;
	}
	sort(pP.begin(), pP.end(), cmp);

	cin >> M;

	if (N == 1) {
		cout << "0" << "\n";
		return 0;
	
	}
	int cP = pP[0].first;
	int cI = pP[0].second;
	if (cI == 0) {
		if (M >= pP[1].first) {
			M -= pP[1].first;
			ans.append(to_string(pP[1].second));
		}
		else {
			cout << "0" << "\n";
			return 0;
		}
	}
	while (M - cP >= 0) {
		M -= cP;
		ans.append(to_string(cI));
	}

	for (int i = 0; i < ans.length(); i++) {
		int cur = ans[i] - '0';
		for (int j = N - 1; j > 0 && j > cur; j--) {
			if (M + iP[cur] - iP[j] >= 0) {
				M = M + iP[cur] - iP[j];
				ans[i] = j + '0';
                break;
			}
		}
	}

	cout << ans << "\n";

	return 0;
}