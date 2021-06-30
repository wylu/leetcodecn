/**
 * @File    :   37.序列化二叉树.cpp
 * @Time    :   2021/06/30 09:26:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:
    void serial(TreeNode* root, string& data) {
        if (!root) {
            data += "#,";
            return;
        }
        data += to_string(root->val) + ",";
        serial(root->left, data);
        serial(root->right, data);
    }

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string data = "";
        serial(root, data);
        data.pop_back();
        return data;
    }

    TreeNode* deserial(queue<string>& data) {
        if (data.empty()) return nullptr;
        string val = data.front();
        data.pop();
        if (val == "#") return nullptr;
        TreeNode* root = new TreeNode(stoi(val));
        root->left = deserial(data);
        root->right = deserial(data);
        return root;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        queue<string> nodes;
        int j = 0, n = data.size();
        for (int i = 0; i <= n; i++) {
            if (i == n || data[i] == ',') {
                nodes.push(data.substr(j, i - j));
                j = i + 1;
            }
        }
        return deserial(nodes);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));

int main(int argc, char const* argv[]) {
    Codec codec;
    TreeNode* tree = new TreeNode(1);
    tree->left = new TreeNode(2);
    tree->right = new TreeNode(3);
    tree->right->left = new TreeNode(4);
    tree->right->right = new TreeNode(5);

    string data = codec.serialize(tree);
    cout << data << endl;

    TreeNode* root = codec.deserialize(data);

    data = codec.serialize(root);
    cout << data << endl;
    return 0;
}
