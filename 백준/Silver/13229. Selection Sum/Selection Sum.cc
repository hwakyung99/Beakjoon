#include <iostream>
using namespace std;

int arr[100001];

int main() {
	int  n;
	cin >> n;
	
	int num;
	for (int i = 0; i < n; i++) {
		cin >> num;
		arr[i] = arr[i - 1] + num;
	}

	int m;
	cin >> m;

	int start, end;
	for (int i = 0; i < m; i++) {
		cin >> start >> end;
		cout << arr[end] - arr[start - 1] << "\n";
	}
	return 0;
}