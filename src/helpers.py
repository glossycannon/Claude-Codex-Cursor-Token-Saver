# Build: 7b7462f061ac845bd6981d2a0c90d0fb

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
