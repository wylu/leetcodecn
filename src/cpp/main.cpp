#include <bits/stdc++.h>
using namespace std;

void printVectorInt(vector<int>& vct) {
    printf("[");
    int n = vct.size();
    if (n > 0) printf("%d", vct[0]);
    for (int i = 1; i < n; i++) printf(",%d", vct[i]);
    printf("]\n");
}

int main(int argc, char const* argv[]) {
    // multiset<int> nums{2, 4, 0, 0, 8, 1};
    // printf("*nums.begin(): %d\n", *nums.begin());
    // nums.erase(0);
    // printf("*nums.begin(): %d\n", *nums.begin());
    // printf("nums.count(0): %ld\n", nums.count(0));

    // unordered_map<int, int> m{{2, 1}, {4, 1}, {0, 2}, {8, 1}};
    // printf("m[5]=%d\n", m[5]);

    vector<int> vals;
    vals.reserve(5);
    for (int i = 0; i < 10; i++) {
        printf("size: %ld, cap: %ld\n", vals.size(), vals.capacity());
        vals.push_back(i);
    }
    printVectorInt(vals);
    return 0;
}
