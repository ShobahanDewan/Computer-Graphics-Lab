import matplotlib.pyplot as plt


def midpoint_circle(radius):
    
    x, y = 0, radius
    p = 1 - radius  
    

    points = []
  
    def plot_points(x, y):
        points.extend([
            (x, y), (-x, y), (x, -y), (-x, -y), 
            (y, x), (-y, x), (y, -x), (-y, -x)
        ])
    
 
    plot_points(x, y)
    
    while x < y:
        
        if p < 0:
            p = p + 2*x + 3
        else:
            p = p + 2*(x - y) + 5
            y -= 1
        
        x += 1
        plot_points(x, y)
    
    return points


radius = 50

circle_points = midpoint_circle(radius)

x_coords, y_coords = zip(*circle_points)

plt.figure(figsize=(6, 6))
plt.scatter(x_coords, y_coords, color='blue', s=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Midpoint Circle Drawing")
plt.grid(True)
plt.show()
