def dist(points):  # expecting this points as a list.
    points.sort()
    result = abs(points[0] - points[-1])
    return result


if __name__ == "__main__":
    assert dist([1, 2, 3]) == 2
    assert dist([1, 2, 3, 2.5]) == 2
    assert dist([1, 2, 3, 2.5, 3.5]) == 2.5
    assert dist([1, 2, 3, 2.5, 3.5, 120]) == 119
    assert dist([1, 2, 3, 2.5, 3.5, 120, -1000]) == 1120
