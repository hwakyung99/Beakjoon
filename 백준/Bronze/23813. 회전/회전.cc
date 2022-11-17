#include <iostream>
#include <cmath>
using namespace std;

int main() {
	string  n;
	cin >> n;

	int len = n.size();
	int sum = 0;

	for (int i = 0; i < len; i++) {
		sum += (n[i] - 48);
	}
	
	long ans = 0;
	for (int i = 0; i < len; i++) {
		ans += sum  * pow(10, i);
	}
	
	cout << ans;

	return 0;
}