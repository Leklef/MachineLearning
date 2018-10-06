import random
import matplotlib.pyplot as plt
from math import sqrt
from math import fabs
from math import cos
from math import sin
from math import pi


LIMIT = 100
DELTA = 0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return str(self.x) + " " +  str(self.y)

def gen_point(maximalno):
    return Point(
        random.random() * maximalno,
        random.random() * maximalno
    )

def calculate(k, points, colors, debug=False):

    
    centers = calc_centers(k, points)
    groups = {}

    was_changed = True

    plt.ion()

    kkk = 0

    while (was_changed):
        kkk += 1
        not_changed = 0

        # Clear point in group
        for i in centers:
            groups[i] = set()

        # Calculate group for every point
        for i in points:
            groups[determinate_group(i, centers)].add(i)

        draw_groups(groups, colors)

        # Refresh centers
        for i in centers:
            new_center = calc_center(groups[i])
            if fabs(new_center.x - i.x) <= DELTA and fabs(new_center.y - i.y) <= DELTA:
                not_changed += 1
            i.x = new_center.x
            i.y = new_center.y
        if not_changed == len(centers):
            was_changed = False

    if debug:
        print("\nPoints: ")
        for i in points:
            print(str(i))
        print("\nGroups:")
        for group in groups:
            print("Group with center in " + str(group))
            for point in groups[group]:
                print(point)
            print("\n")

    return groups
        
                

    
def calc_center(points):
    center = Point(0, 0)
    for point in points:
        center.x += point.x
        center.y += point.y

    count = len(points)
    if count != 0:
        center.x /= len(points) 
        center.y /= len(points)
    return center


def determinate_group(point, centers):
    min_dist = LIMIT + 1
    result = centers[0]
    for i in centers:
        dist = distance(point, i)
        if dist < min_dist:
            result = i
            min_dist = dist
            
    return result
    

def calc_centers(k, points):

    point = calc_center(points)
    max_distance_point = point
    rad = 0

    for i in points:
        if distance(i, point) > rad:
            max_distance_point = i
            rad = distance(point, max_distance_point)


    centers = []
    for i in range(k):
        centers.append(Point(
            (point.x + rad * cos(i * 2 * pi / k)),
                (point.y + rad * sin(i * 2 * pi / k))
            )
        )

    return centers
    
def distance(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def rand_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())


def draw_groups(groups, colors):
    plt.clf()
    for i, group in enumerate(groups):
        group_colors = [colors[i] for point in groups[group]]
        plt.scatter(
                [point.x for point in groups[group]],
                [point.y for point in groups[group]],
                c=colors[i]
        ) 
        plt.scatter(
                [group.x],
                [group.y],
                c='red',
                marker='^',
                s=42

        )

    plt.xlim(-LIMIT, LIMIT * 2)
    plt.ylim(-LIMIT, LIMIT * 2)

    plt.pause(1)
    plt.draw()


########################################################

k = 4
n = 128

colors = []
for i in range(k):
    colors.append(rand_color())

points = [gen_point(LIMIT) for i in range(n)]
groups = calculate(k, points, colors, False)

draw_groups(groups, colors)
plt.ioff()
plt.show()


