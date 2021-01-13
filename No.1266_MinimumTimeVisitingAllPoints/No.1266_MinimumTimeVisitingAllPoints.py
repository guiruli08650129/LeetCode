class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def time(x, y):
            hori  = abs(x[0] - y[0])
            verti = abs(x[1] - y[1])
            
            if verti == hori:
                return hori
            else:
                return max(verti, hori)
        
        steps = 0
        for i in range(1, len(points)):
            steps += time(points[i-1], points[i])
        return steps