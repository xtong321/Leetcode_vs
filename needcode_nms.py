"""
implement nms in object detection to get the final filtered objects
"""

import numpy as np
from typing import List


def my_nms(init_dets, thres):
    """
    inarg: dets -- list of input initial detection, with [x1, y1, x2, y2, score]
    inarg: thres -- threshold of valid detection
    return:
        ans: list of clustered detection results whole score >= thres
    """
    #if not init_dets:
    #    return None
    x1 = init_dets[:, 0]
    y1 = init_dets[:, 1]
    x2 = init_dets[:, 2]
    y2 = init_dets[:, 3]
    scores = init_dets[:, 4]

    # sort dets with descented score
    order = scores.argsort()[::-1]
    areas = (x2-x1+1)*(y2-y1+1)

    res = []
    while order.size > 0:
        i = order[0]
        res.append(i) # the det with the highest score

        # overlap area
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        # area
        w = np.maximum(0.0, xx2-xx1+1)
        h = np.maximum(0.0, yy2-yy1+1)
        inter = w*h

        # iou filter
        iou = inter / (areas[i] + areas[order[1:]] - inter)
        idx = np.where(iou <=thres)[0]
        order = order[idx+1]

    return res
    # return filtered_det
    #bboxes = init_dets[res]



boxes = np.array([
    [100, 100, 210, 210, 0.72],
    [250, 250, 420, 420, 0.8],
    [220, 220, 320, 330, 0.92],
    [100, 100, 210, 210, 0.72],
    [230, 240, 325, 330, 0.81],
    [220, 230, 315, 340, 0.9]
])

boxes = np.array([
    [201, 201, 220, 220, 0.72],
    [200, 200, 220, 220, 0.9]
])

keep = my_nms(boxes, thres=0.7)
print("filtered_res:", keep)

        