def compute_triangle_indices(n, m):
    indices = []
    for i in range(n):
        for j in range(m):
            # Calculate the indices of the four corners of the grid cell
            top_left = i * (m + 1) + j
            top_right = top_left + 1
            bottom_left = top_left + (m + 1)
            bottom_right = bottom_left + 1

            # First triangle (top-left)
            indices.append((top_left, top_right, bottom_left))

            # Second triangle (bottom-right)
            indices.append((top_right, bottom_right, bottom_left))

    return indices

# Example usage for a 2x2 grid
triangle_indices = compute_triangle_indices(2, 2)
for tri in triangle_indices:
    print(tri)
