"""
[이진 트리 - Binary Tree 기본]

문제 설명:
- 이진 트리의 기본 구조를 구현합니다.
- 각 노드는 최대 2개의 자식(왼쪽, 오른쪽)을 가집니다.
- 전위, 중위, 후위 순회를 구현합니다.
- 각 노드가 최대 2개의 자식 노드(왼쪽, 오른쪽)를 가질 수 있는 트리 구조.

입력:
- 트리 노드들

출력:
- 전위 순회: 루트 → 왼쪽 → 오른쪽
- 중위 순회: 왼쪽 → 루트 → 오른쪽
- 후위 순회: 왼쪽 → 오른쪽 → 루트

예제:
트리 구조:
      1
     / \
    2   3
   / \
  4   5

전위: [1, 2, 4, 5, 3]
중위: [4, 2, 5, 1, 3]
후위: [4, 5, 2, 3, 1]

힌트:
- 재귀로 간단히 구현 가능
- 순회 순서만 다름
"""

class TreeNode:
    """이진 트리 노드"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    """전위 순회: 루트 → 왼쪽 → 오른쪽"""
    return preorder_loop(root)

def preorder_recursive(root):
    result = []
    
    def traverse(node):
        if node == None:
            return

        result.append(node.value)
        traverse(node.left)
        traverse(node.right)
        return

    traverse(root)
    return result

def preorder_loop(root):
    result = []
    stack = []

    node = root
    while node:
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        if not stack:
            break
        node = stack.pop()

    return result

def inorder(root):
    """중위 순회: 왼쪽 → 루트 → 오른쪽"""
    return inorder_loop(root)

def inorder_recursive(root):
    result = []
    
    def traverse(node):
        if node == None:
            return

        traverse(node.left)
        result.append(node.value)
        traverse(node.right)
        return

    traverse(root)
    return result

def inorder_loop(root):
  result = []
  stack = []

  node = root
  while node is not None:
    if node.left:
        stack.append(node)
        node = node.left
    else: 
        result.append(node.value)
        node = node.right
        while not node and stack:
          node = stack.pop()
          result.append(node.value)
          node = node.right

  return result

def postorder(root):
    """후위 순회: 왼쪽 → 오른쪽 → 루트"""
    return postorder_loop(root)

def postorder_recursive(root):
    result = []
    
    def traverse(node):
        if node == None:
            return

        traverse(node.left)
        traverse(node.right)
        result.append(node.value)
        return

    traverse(root)    
    return result

def postorder_loop(root):
    result = []
    stack = []
    last_visit = None

    node = root
    while node is not None:
        while node.left:
            stack.append(node)    
            node = node.left
        if node.right:
            stack.append(node)
            node = node.right
        else:
            result.append(node.value)
            last_visit = node                       
            while stack:
                node = stack[-1].right
                if node and node is not last_visit:
                    break
                else:
                    last_visit = stack.pop()
                    result.append(last_visit.value) 
                    node = None                    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 트리 생성:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("=== 이진 트리 순회 ===")
    print(f"전위 순회: {preorder(root)}")
    print(f"중위 순회: {inorder(root)}")
    print(f"후위 순회: {postorder(root)}")

