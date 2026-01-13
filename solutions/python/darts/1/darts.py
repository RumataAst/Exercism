def score(x, y):
    distance_sq = x * x + y * y

    for radius_sq, points in ((1, 10), (25, 5), (100, 1)):
        if distance_sq <= radius_sq:
            return points
    return 0
