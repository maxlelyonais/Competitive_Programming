import math

# level is the wrong part
def combine(val1, val2, level):
    if val1 == val2:
        return val1
    if level % 2 == 1:  
        return val1 if (val1 - val2) % 3 == 2 else val2
    else:               
        return val1 if (val1 - val2) % 3 == 1 else val2

def build(tree, arr, node, left, right, level):
    if left == right:
        tree[node] = arr[left]
    else:
        mid = (left + right) // 2
        build(tree, arr, node*2, left, mid, level-1)
        build(tree, arr, node*2+1, mid+1, right, level-1)
        tree[node] = combine(tree[node*2], tree[node*2+1], level)

def update(tree, node, left, right, pos, new_val, level):
    if left == right:
        tree[node] = new_val
    else:
        mid = (left + right) // 2
        if pos <= mid:
            update(tree, node*2, left, mid, pos, new_val, level-1)
        else:
            update(tree, node*2+1, mid+1, right, pos, new_val, level-1)
        tree[node] = combine(tree[node*2], tree[node*2+1], level)

if __name__ == "__main__":
    n, m = map(int, input().split())
    tool_map = {"papel": 0, "piedra": 1, "tijera": 2}
    reversed_map = ["papel", "piedra", "tijera"]

    tools = input().split()
    parsed_tools = [tool_map[t] for t in tools]

    size = len(parsed_tools)
    tree = [-1] * (4 * size)

    height = math.ceil(math.log2(size))
    build(tree, parsed_tools, 1, 0, size-1, height)

    for _ in range(m):
        pos_str, tool_str = input().split()
        pos = int(pos_str) - 1
        tool = tool_map[tool_str]
        update(tree, 1, 0, size-1, pos, tool, height)
        print(reversed_map[tree[1]])
