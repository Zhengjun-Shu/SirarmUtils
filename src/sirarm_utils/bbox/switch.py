def xyxy2xywh(position):
    """
    将边界框位置[x1,y1,x2,y2]转换为[x_center,y_center,w,h]
    :param position: 边界框位置[x1,y1,x2,y2]
    :return: 边界框位置[x_center,y_center,w,h]
    """
    x1, y1, x2, y2 = position
    w = x2 - x1
    h = y2 - y1
    x_center = x1 + w / 2
    y_center = y1 + h / 2
    return [x_center, y_center, w, h]


def xywh2xyxy(position):
    """
    将边界框位置[x_center,y_center,w,h]转换为[x1,y1,x2,y2]
    :param position: 边界框位置[x_center,y_center,w,h]
    :return: 边界框位置[x1,y1,x2,y2]
    """
    x_center, y_center, w, h = position
    x1 = x_center - w / 2
    y1 = y_center - h / 2
    x2 = x_center + w / 2
    y2 = y_center + h / 2
    return [x1, y1, x2, y2]


def xyxy2xyrh(position):
    """
    将边界框位置[x1,y1,x2,y2]转换为[x_center,y_center,r,h]
    :param position: 边界框位置[x1,y1,x2,y2]
    :return: 边界框位置[x_center,y_center,r,h]
    """
    x1, y1, x2, y2 = position
    w = x2 - x1
    h = y2 - y1
    x_center = x1 + w / 2
    y_center = y1 + h / 2
    return [x_center, y_center, w / h, h]


def xyrh2xyxy(position):
    """
    将边界框位置[x_center,y_center,r,h]转换为[x1,y1,x2,y2]
    :param position: 边界框位置[x_center,y_center,r,h]
    :return: 边界框位置[x1,y1,x2,y2]
    """
    x_center, y_center, r, h = position
    x1 = x_center - r * h / 2
    y1 = y_center - h / 2
    x2 = x_center + r * h / 2
    y2 = y_center + h / 2
    return [x1, y1, x2, y2]
