#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

    vector<float> ce;
    char ans[] = { 'S', 'N', 'U' };

    for (int i = 0; i < 3; i++) {
        float price, weight;
        cin >> price >> weight;
        price *= 10;
        weight *= 10;
        if (price >= 5000) price -= 500;
        ce.push_back(weight / price);
    }

    int max_idx = max_element(ce.begin(), ce.end()) - ce.begin();

    cout << ans[max_idx];

    return 0;
}