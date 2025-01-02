def check_collision_circle_rectangle(circle_center, circle_radius, rectangle):
    circle_x, circle_y = circle_center
    rectangle_x, rectangle_y, rectangle_width, rectangle_height = rectangle

    closest_x = max(rectangle_x, min(circle_x, rectangle_x + rectangle_width))
    closest_y = max(rectangle_y, min(circle_y, rectangle_y + rectangle_height))

    distance_squared = (circle_x - closest_x) ** 2 + (circle_y - closest_y) ** 2

    return distance_squared <= circle_radius ** 2
