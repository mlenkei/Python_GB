
points = [1, 3, 3, 3, 4]
print(points)
for i in range(1, len(points)):
    maxPoint = max(points)
    minPoint = min(points)
    if (points[i] == maxPoint):
        points[i] = minPoint

print(maxPoint)
print(minPoint)
print(points)