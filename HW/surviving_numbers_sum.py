'''
Given a positive integer sequence nums. Process:
Start jumping from index 0 backwards. Jump over J numbers, hit the number at index J+1.
This number is knocked out.
Start jumping from there again, until remaining numbers count is left.
Return sum of remaining numbers.

Constraints:
1. 0 is the first starting point (index 0).
2. Starting point and knocked out number are separated by `jump` (J) numbers. Not including start and knocked out.
3. Wrap around to beginning when reaching end.
4. If left > len(nums), no need to jump (return sum).
'''

# Simulate circular structure using linked list
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

# Read nums
nums = list(map(int, input().strip().split(',')))
# Read J and left
J = int(input().strip())
left = int(input().strip())

n = len(nums)
size = n

if left >= n:
    print(sum(nums))
    exit()

# Build circular linked list
head = Node(nums[0])
head.next = head
head.prev = head
cur = head
for num in nums[1:]:
    new_node = Node(num)
    cur.next = new_node
    new_node.prev = cur
    cur = new_node

cur.next = head # Form circle
head.prev = cur

# Simulate jump and knock out
cur = head # Start from first node
while size > left:
    # Jump J steps?
    # Problem says "Jump over J numbers".
    # Start -> skip 1 .. skip J -> Hit Target.
    # So we move J+1 steps?
    # Code: `for _ in range(J+1): cur = cur.next`. Yes.
    for _ in range(J+1):
        cur = cur.next
    size -= 1
    # print(f"Knocked out value: {cur.val}")
    # print(f"Remaining size: {size}")
    # Knock out current node
    cur.prev.next = cur.next
    cur.next.prev = cur.prev
    # Start from *previous* node after knock out?
    # Original code: `cur = cur.prev`.
    # Usually Josephus problem starts from *next* node.
    # Problem says "From that point start jumping".
    # If "That point" means the position of knocked out number (which is now empty), or adjacent?
    # "From that point start jumping".
    # The code implementation jumps to `cur.prev` then starts logic?
    # If I removed X, and I am at P -> X -> N.
    # Now P -> N. `cur` becomes P.
    # Next loop moves J+1 steps starting from P.
    # So we skip P? No, loop `for _ in range(J+1): cur = cur.next`.
    # 1st step: P -> N.
    # So we count N as 1st skipped?
    # Or P as 1st skipped?
    # If we start at P, `cur = cur.next` moves to N.
    # So P is NOT skipped?
    # Wait, "Jump over J numbers".
    # If J=1. Start P. Skip N. Hit N's neighbor?
    # Code: starts at P. Step 1: P->N. Step 2: N->nn.
    # Total J+1 steps.
    # So we assume logic matches problem statement as interpreted by original author.
    cur = cur.prev 

# Sum remaining nodes
result = 0
cur = head
# Loop `left` times?
# Because only `left` nodes remain.
# But `head` might have been deleted?
# Original code: `cur = head`.
# If `head` was deleted, `head` variable still points to a node object, but it's detached from the active ring?
# `cur.prev.next = cur.next` updates links.
# If `head` was deleted, its `next` and `prev` are not relevant for traversal?
# Wait. If `head` is deleted, `head.next` might still point to something?
# But checking from `head` is dangerous if `head` is deleted.
# Correct way is to pick ANY node in the remaining cycle.
# The `cur` at end of loop is valid (it is `cur.prev` of deleted node, which is safe unless list empty).
# So use `cur` from loop.
# But code uses `cur = head`.
# Is `head` guaranteed to survive? No.
# If `head` is deleted, `head` object is stale.
# Does `head` fields get updated?
# `cur.prev.next = cur.next`.
# If `head` is deleted, `head.prev.next` updates, `head.next.prev` updates.
# `head` itself is not updated. So `head.next` points to old next.
# So traversing from `head` might include deleted nodes!
# This looks like a BUG in original code.
# However, "Simulate jump... sum remaining".
# I should fix this bug?
# Or maybe `head` is never deleted? No guarantee.
# FIX: Use `cur` (which is valid node in ring) to traverse.
# I will change `cur = head` to `cur = cur` (keep cur).
# Wait, `cur` after loop is `cur.prev` from deleted node.
# It is valid.
# So I remove `cur = head`.

cur = cur # Start from valid node
# Traversing a circular list of `size=left`.
# We need to ensure we visit `left` unique nodes.
# Just loop `left` times moving next.
for _ in range(left):
    result += cur.val
    cur = cur.next

print(result)
