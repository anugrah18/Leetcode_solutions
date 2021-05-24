from collections import defaultdict,OrderedDict

class Node:
    def __init__(self, value, count):
        self.val = value
        self.count = count


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeKeys = {}
        self.nodeCounts = defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key: int) -> int:
        if key not in self.nodeKeys:
            return -1

        node = self.nodeKeys[key]
        del self.nodeCounts[node.count][key]

        if not self.nodeCounts[node.count]:
            del self.nodeCounts[node.count]

        node.count += 1
        self.nodeCounts[node.count][key] = node

        if not self.nodeCounts[self.minCount]:
            self.minCount += 1

        return node.val

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return

        if key in self.nodeKeys:
            self.nodeKeys[key].val = value
            self.get(key)
            return

        if len(self.nodeKeys) == self.capacity:
            lfuKey, lfuCount = self.nodeCounts[self.minCount].popitem(last=False)
            del self.nodeKeys[lfuKey]

        newNode = Node(value, 1)
        self.nodeKeys[key] = newNode
        self.nodeCounts[1][key] = newNode
        self.minCount = 1

lfu= LFUCache(2)
print(lfu.put(1, 1))
print(lfu.put(2, 2))
print(lfu.get(1))
print(lfu.put(3, 3))
print(lfu.get(2))
print(lfu.get(3))
print(lfu.put(4, 4))
print(lfu.get(1))
print(lfu.get(3))
print(lfu.get(4))

