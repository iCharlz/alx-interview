
#!/usr/bin/python3
"""
n number of locked boxes in front of you. Each box is numbered sequentially 
from 0 to n - 1 and each box may contain keys to the other boxes.
a method that determines if all the boxes can be opened.
"""

"""
def canUnlockAll(boxes):

    if (type(boxes) is not list):
        return False    # box not in the this will return fales 

    if (len(boxes) == 0):
        return False    # box length equal to null return 0

    keys = [0]
    for i in keys:      # boxs determined all will opend
        for j in boxes[i]:
            if j not in keys and j != i and j < len(boxes) and j != 0:
                keys.append(j)
    if len(keys) == len(boxes):
        return True
    else:
        return False
    """
def canUnlockAll(boxes):
    """checks if all boxes are reachable."""
    if (not isinstance(boxes, list)):
        return False

    seen = [False for _ in range(len(boxes))]
    seen[0] = True

    # useDFS(boxes, seen, 0)
    useBFS(boxes, seen)

    # the `seen` array tracks all the visited nodes. we can then see which
    # nodes were unvisited by inspecting for False values. However, for this
    # task we only need to know if any node was unreached, which is easier.
    return all(seen)

def useBFS(boxes, seen):
    """uses iteration to visit nodes breadth-first
        and populate the seen array as each new node is visited.
    """
    for i, box in enumerate(boxes):
        if (isinstance(box, list) is not True):
            continue

        for key in box:
            if (isinstance(key, int) is not True):
                continue

            # guard against out-of-bounds array access
            if (key >= len(boxes)):
                continue

            if (i == key):
                continue

            seen[key] = True

def useDFS(boxes, seen, currentBoxIdx):
    """uses recursion to visit nodes depth-first
        and populate the seen array as each new node is visited.
    """
    currentBox = boxes[currentBoxIdx]

    if (isinstance(currentBox, list) is not True):
        return

    for key in currentBox:
        if (isinstance(key, int) is not True):
            continue

        # guard against out-of-bounds array access
        if (key >= len(boxes)):
            continue

        if (seen[key]):
            continue

        seen[key] = True
        useDFS(boxes, seen, key)
