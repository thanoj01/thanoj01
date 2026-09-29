class Solution:
    def inorderTraversal(self, root):
        ans = []
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            ans.append(node.val)

            node = node.right

        return ans