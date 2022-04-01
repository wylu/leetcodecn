#include <bits/stdc++.h>
using namespace std;

#define PII pair<int, int>

void printVectorInt(vector<int>& vct) {
    printf("[");
    int n = vct.size();
    if (n > 0) printf("%d", vct[0]);
    for (int i = 1; i < n; i++) printf(",%d", vct[i]);
    printf("]\n");
}

void priorityQueueCustomCmp() {
    auto cmp = [](const PII& a, const PII& b) -> bool {
        return a.second > b.second;
    };
    priority_queue<PII, vector<PII>, decltype(cmp)> busy(cmp);

    busy.emplace(1, 5);
    busy.emplace(2, 4);
    busy.emplace(3, 3);
    busy.emplace(4, 2);
    busy.emplace(5, 1);

    while (!busy.empty()) {
        PII cur = busy.top();
        printf("first=%d, second=%d\n", cur.first, cur.second);
        busy.pop();
    }
}

int main(int argc, char const* argv[]) {
    // vector<int> arr{1, 2, 3, 4, 5};
    // printVectorInt(arr);

    priorityQueueCustomCmp();
    return 0;
}
