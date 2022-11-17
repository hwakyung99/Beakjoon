#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define min(a, b) ((a) < (b)) ? (a) : (b)

int  n, m;
queue<int> q;
vector<int> g[100001];
int check[100001];

int main() {
	cin >> n >> m;

	int x, y;
	for (int i = 0; i < m; i++) {
		cin >> x >> y;
		g[x].push_back(y);
	}

	q.push(1);
	while (!q.empty()) {
		int node = q.front(); q.pop();

		while (!g[node].empty()) {
			int i = g[node].back(); g[node].pop_back();

			q.push(i);
			
			if (check[i] == 0) check[i] = check[node] + 1;
			else check[i] = min(check[i], check[node] + 1);
		}
	}

	if (n == 1) cout << 0;
	else if (check[n] == 0) cout << -1;
	else cout << check[n];

	return 0;
}
