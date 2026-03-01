import colorsys
import random


def generate_color_list(number: int = 20, mode: str = "hsv", seed=0):
    """

    Args:
        seed: Random number seed
        mode: Output mode。choices:["hsv","rgb","hex"]
        number(int): the number of the color list which will be generated

    Returns:
        the list of `mode` color
    """
    random.seed(seed)
    colors = []
    golden_ratio = 0.618033988749895
    for i in range(number):
        # 黄金比例色相分布
        hue = (i * golden_ratio) % 1.0
        # 随机饱和度和明度
        saturation = 0.7 + random.uniform(-0.2, 0.2)
        value = 0.7 + random.uniform(-0.2, 0.2)
        color = (hue, saturation, value)
        if mode == "rgb":
            color = hsv2rgb(color)
        elif mode == "hex":
            color = hsv2hex(color)
        colors.append(color)
    return colors


def hsv2rgb(hsv):
    """
    Args:
        hsv: hsv color
    Returns:
        rgb color
    """
    rgb = colorsys.hsv_to_rgb(*hsv)
    return (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))


def hsv2hex(hsv):
    """
    Args:
        hsv: hsv color
    Returns:
        hex color
    """
    rgb = hsv2rgb(hsv)
    hex = "#%02x%02x%02x" % rgb
    return hex


def hex2rgb(hex):
    """
    Args:
        hex: hex color
    Returns:
        rgb color
    """
    hex = hex.lstrip('#')
    rgb = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
    return rgb


def hex2hsv(hex):
    """
    Args:
        hex: hex color
    Returns:
        hsv color
    """
    rgb = hex2rgb(hex)
    hsv = colorsys.rgb_to_hsv(*rgb)
    return hsv


def rgb2hex(rgb):
    """
    Args:
        rgb: rgb color
    Returns:
        hex color
    """
    hex = "#%02x%02x%02x" % (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
    return hex


def rgb2hsv(rgb):
    """
    Args:
        rgb: rgb color
    Returns:
        hsv color
    """
    hsv = colorsys.rgb_to_hsv(*rgb)
    return hsv
