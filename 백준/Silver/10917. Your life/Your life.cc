#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define min(a, b) ((a) < (b)) ? (a) : (b)

int  n, m;
queue<int> q;
vector<int> g[100001];
int check[100001];

void bfs(int node) {
	q.push(node);
	check[node] = 0;
	while (!q.empty()) {
		int n = q.front(); q.pop();
		for (int i = 0; i < g[n].size(); i++) {
			if (check[g[n][i]] == -1) {
				q.push(g[n][i]);
				check[g[n][i]] = check[n] + 1;
			}
		}
	}
}

int main() {
	cin >> n >> m;

	int x, y;
	for (int i = 0; i < m; i++) {
		cin >> x >> y;
		g[x].push_back(y);
	}

	for (int i = 1; i <= n; i++) {
		check[i] = -1;
	}

	bfs(1);
	
	if (check[n] == -1) cout << -1;
	else cout << check[n];

	return 0;
}