#include <stdio.h>
#include <iostream>
using namespace std;

#define MAX_SIZE 10001

int stack[MAX_SIZE];
int t = -1;

int empty() {
	if (t < 0) return 1;
	return 0;
}

void push(int x) {
	stack[++t] = x;
}

int pop() {
	if (empty()) {
		return -1;
	}
	return stack[t--];
}

int size() {
	return t + 1;
}

int top() {
	if (empty()) {
		return -1;
	}
	return stack[t];
}

int main() {
	int n, x;
	string s;
	cin >> n;

	while (n > 0) {
		cin >> s;
		if (s == "push") {
			cin >> x;
			push(x);
		}
		else if (s == "pop") {
			cout << pop() << "\n";
		}
		else if (s == "size") {
			cout << size() << "\n";
		}
		else if (s == "empty") {
			cout << empty() << "\n";
		}
		else if (s == "top") {
			cout << top() << "\n";
		}
		n--;
	}

	return 0;
}