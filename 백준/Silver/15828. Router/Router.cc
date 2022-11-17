#include <iostream>
#include <queue>
using namespace std;

int main() {
	int  n;
	cin >> n;

	queue<int> router;
	int packet;
	
	while (1)
	{
		cin >> packet;
		if (packet == -1) break;
		else if (packet == 0) {
			router.pop();
		}
		else if (router.size() < n) {
			router.push(packet);
		}
	}
	
	if (router.empty()) cout << "empty";
	else {
		while (!router.empty()){
			cout << router.front() << " ";
			router.pop();
		}
	}
	
	return 0;
}