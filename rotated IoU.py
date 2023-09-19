import numpy as np
def cross_point(line1, line2): #[x0,y0,x1,y1], [x2,y2,x3,y3]
    pass #wiki
    return point, n, m
def is_in_box(bbox, point): #[x0,y0,x1,y1,x3,y3,x4,y4], [s,t]
    pass
    return pass

def get_area(points): #[[x,y],[x,y],[x,y]...]
    pass
    return s

def get_iou(bbox1:list,bbox2:list):
    bbox1.add(bbox1[:2])
    bbox2.add(bbox2[:2])
    cross_points = []
    in_box_points = []
    for i in range(4):
        for j in range(4)
        cross_p, n, m = cross_point(bbox1[2*i:2*i+4],bbox2[2*j:2*j+4])
        if 0<n<1 and 0<m<1:
            cross_points.append(cross_p)
        if is_in_box(bbox2, bbox1[2*i:2*i+2]):
            in_box_points.append(bbox1[2*i:2*i+2])
    for j in range(4):
        if is_in_box(bbox1, bbox2[2*j:2*j+2]):
            in_box_points.append(bbox2[2*j:2*j+2])

    s0 = get_area(cross_points.add(in_box_points))

    w1 = np.sqrt((bbox1[0]-bbox1[2])**2 + (bbox1[1]-bbox1[3])**2)
    h1 = np.sqrt((bbox1[2] - bbox1[4]) ** 2 + (bbox1[3] - bbox1[5]) ** 2)
    s1 = w1*h1

    w2 = np.sqrt((bbox2[0] - bbox2[2]) ** 2 + (bbox2[1] - bbox2[3]) ** 2)
    h2 = np.sqrt((bbox2[2] - bbox2[4]) ** 2 + (bbox2[3] - bbox2[5]) ** 2)
    s2 = w2 * h2

    return s0/(s1+s2-s0)