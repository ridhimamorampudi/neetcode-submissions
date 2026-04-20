class CountSquares:

    def __init__(self):
        self.pts = []
        self.ptsFreq = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.ptsFreq[tuple(point)] += 1
        self.pts.append(point)
        
        

        

    def count(self, point: List[int]) -> int:
        res = 0;
        px,py = point
        for x,y in self.pts:
            if (abs(py-y) != abs(px-x)) or x==px or y == py:
                continue
            res += self.ptsFreq[(x, py)] * self.ptsFreq[(px, y)]
        return res



# [x,y]:3

# square reqs:
# if 
# x-1,y
# x-1,y+1
# x,y+1

# x+1,y
# x+1,y+1
# x,y+1

# x+1,y
# x+1,y-1
# x,y-1

# x-1,y
# x,y-1
# x-1,y-1
