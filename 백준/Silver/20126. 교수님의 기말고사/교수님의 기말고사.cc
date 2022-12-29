#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

    int n, m, s, ans = -1;
    vector<pair<int, int>> clist;

    cin >> n >> m >> s;

    clist.push_back(make_pair(0, 0));

    int x, y;
    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        clist.push_back(make_pair(x, y));
    }

    sort(clist.begin(), clist.end());

    for (int i = 0; i < n; i++) {
        if (m <= clist[i + 1].first - (clist[i].first + clist[i].second)) {
            ans = clist[i].first + clist[i].second;
            break;
        }
    }

    if (ans == -1) {
        if (m <= s - (clist[n].first + clist[n].second)) {
            ans = clist[n].first + clist[n].second;
        }
    }
    cout << ans;

    return 0;
}