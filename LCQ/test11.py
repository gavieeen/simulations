def is_point_in_triangle(a, b, c, p):
    def slope(pt1, pt2):
        if pt1[0] == pt2[0]:
            return float("inf")
        return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])

    slope1 = slope(a, b)
    slope2 = slope(b, c)
    slope3 = slope(c, a)

    # Calculate the slopes from the point P to the vertices
    s1 = slope(a, p)
    s2 = slope(b, p)
    s3 = slope(c, p)

    # Check if point P's slopes are within the bounds of the triangle's edge slopes
    if (
        int(min(slope1, slope3) <= s1 <= max(slope1, slope3))
        + int(min(slope2, slope1) <= s2 <= max(slope2, slope1))
        + int(min(slope3, slope2) <= s3 <= max(slope3, slope2)) >= 2
    ):
        return True
    else:
        return False


# Example points
a, b, c = (0, 0), (5, 5), (1, 0)
p = (3.05, 2.6125)

# Check if point p is inside the triangle formed by a, b, c
result = is_point_in_triangle(a, b, c, p)
print(result)  # This will print True if p is inside the triangle, False otherwise


# check area of point to 2 triangle points and see if all3 areas are equal to the area of the triangle