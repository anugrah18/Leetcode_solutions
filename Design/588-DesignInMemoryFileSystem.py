class Node:
    def __init__(self, content):
        self.content = content
        self.next = {}
        self.isFile = False


class FileSystem:

    def __init__(self):
        self.head = Node('head')

    def ls(self, path: str):
        path = path.split('/')

        curr = self.head
        fileName = ''
        for i in path:
            if i != '':
                if i in curr.next:
                    fileName = i
                    curr = curr.next[i]
                else:
                    return []
        if not curr.isFile:
            return sorted(curr.next.keys())
        else:
            return [fileName]

    def mkdir(self, path: str) -> None:
        curr = self.head
        path = path.split('/')

        for i in path:
            if i != '':
                if i in curr.next:
                    curr = curr.next[i]
                else:
                    curr.next[i] = Node('')
                    curr = curr.next[i]

    def addContentToFile(self, filePath: str, content: str) -> None:
        filePath = filePath.split('/')
        curr = self.head
        for i in filePath:
            if i != '':
                if i in curr.next:
                    curr = curr.next[i]
                else:
                    curr.next[i] = Node('')
                    curr = curr.next[i]
        curr.content += content
        curr.isFile = True

    def readContentFromFile(self, filePath: str) -> str:
        filePath = filePath.split('/')
        curr = self.head
        for i in filePath:
            if i != "":
                if i in curr.next:
                    curr = curr.next[i]
                else:
                    return ""
        return curr.content if curr.isFile else ""

X= FileSystem()
print(X.ls("/"))
print(X.mkdir("/a/b/c"))
print(X.addContentToFile("/a/b/c/d","hello"))
print(X.ls("/"))
print(X.readContentFromFile("/a/b/c/d"))
