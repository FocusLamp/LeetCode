/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

/*
 * Recursion (DFS)
 */
class Solution {
public:
    bool evaluateTree(TreeNode* root) {
        if (root-> left == nullptr and root-> right == nullptr) {
            // Handle the case it there is no leafs.
            return root -> val;
        }
    

        // Storing the evaluations of the tree leaf's

        bool evaluateLeftSubtree = evaluateTree(root -> left);
        bool evaluateRightSubtree = evaluateTree(root -> right);
        bool evaluateRoot;

        if (root -> val == 2) {
            evaluateRoot = evaluateLeftSubtree || evaluateRightSubtree;
        } else {
            evaluateRoot = evaluateLeftSubtree && evaluateRightSubtree;
        }

        return evaluateRoot;

    }
};
