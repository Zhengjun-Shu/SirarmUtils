
def yaml_concat(dst:dict,src:dict):
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            dst[k] = yaml_concat(dst[k], v)
        else:
            dst[k] = v
    return dst