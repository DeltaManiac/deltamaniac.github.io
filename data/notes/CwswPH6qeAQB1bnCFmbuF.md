
# Problem

This question is asked by Amazon.

 Given a 2D board that represents a word search puzzle and a string word, return whether or the given word can be formed in the puzzle by only connecting cells horizontally and vertically.

Ex: Given the following board and words…

```
board =
[
  ['C','A','T','F'],
  ['B','G','E','S'],
  ['I','T','A','E']
]
word = "CAT", return true
word = "TEA", return true
word = "SEAT", return true
word = "BAT", return false
```

## [[python]]

```python
def exist(self, board, word):
    self.word = word
    self.found = False
    for row in range(len(board)):
        for col in range(len(board[0])):
            self.visited = []
            self.visitedSet = set()
            self.dfs(board,row,col,0)
            if self.found:
                return True
    return False


def dfs(self,board,row,col,i):

    if i == len(self.word):
        self.found = True

    if not self.found and row >= 0 and col >= 0 and row<len(board) and col<len(board[0]) and board[row][col] == self.word[i] and (row,col) not in self.visitedSet:
        self.visited += [(row,col)]
        self.visitedSet.add((row,col))
        self.dfs(board,row+1,col,i+1)
        self.dfs(board,row-1,col,i+1)
        self.dfs(board,row,col+1,i+1)
        self.dfs(board,row,col-1,i+1)

        if not self.found:
            self.visitedSet.remove(self.visited.pop())

```
## [[go]]

## [[rust]]