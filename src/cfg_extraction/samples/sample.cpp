
#include <iostream>
int sum(int n) {
    int s = 0;
    for (int i = 0; i < n; ++i) {
        s += i;
    }
    return s;
}
int main() {
    std::cout << sum(1000) << std::endl;
    return 0;
}
