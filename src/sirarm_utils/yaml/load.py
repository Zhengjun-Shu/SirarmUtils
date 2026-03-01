def yaml_load(value):
    if isinstance(value, dict):
        return value
    elif isinstance(value, str):
        import yaml
        with open(value, encoding='utf-8', errors='ignore') as f:
            return yaml.safe_load(f)
    else:
        raise TypeError(f"yaml_load() argument must be a dict or str, not {type(value).__name__}")