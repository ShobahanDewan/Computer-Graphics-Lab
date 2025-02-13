import matplotlib.pyplot as plt


def midpoint_line(x1, y1, x2, y2):
  
    dx = x2 - x1
    dy = y2 - y1

    
    p = 2*dy - dx
    points = []


    if abs(dy) > abs(dx):
        x1, y1, x2, y2 = y1, x1, y2, x2
        dx, dy = dy, dx

 
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

 
    points.append((x1, y1))
    

    while x1 < x2:
        x1 += 1
        if p < 0:
            p = p + 2*dy
        else:
            if y1 < y2:
                y1 += 1
            else:
                y1 -= 1
            p = p + 2*(dy - dx)

        points.append((x1, y1))

    return points

x1, y1 = 0, 0  # Start point (x1, y1)
x2, y2 = 20, 10  # End point (x2, y2)


line_points = midpoint_line(x1, y1, x2, y2)


x_coords, y_coords = zip(*line_points)


plt.figure(figsize=(6, 6))
plt.plot(x_coords, y_coords, color='blue', marker='o')  
plt.title(f"Midpoint Line Drawing from ({x1},{y1}) to ({x2},{y2})")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
