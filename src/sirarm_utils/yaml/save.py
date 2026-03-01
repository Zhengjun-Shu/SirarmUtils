def yaml_save(path, data):
    import yaml
    from pathlib import Path
    serializable_data = {}
    error_list = []
    for k, v in data.items():
        if isinstance(v, (str, int, float, bool, list, dict, tuple)) or isinstance(v, Path):
            serializable_data[k] = str(v) if isinstance(v, Path) else v
        elif v is None:
            serializable_data[k] = None
        else:
            error_list.append(f"跳过不可序列化的对象: {k} -> {type(v)}")
    with open(path, 'w') as f:
        yaml.safe_dump(serializable_data, f, sort_keys=False)
    return error_list
