def is_float(value: str) -> bool:
    try:
        float(value)
    except ValueError:
        return False
    else:
        return True
