def generate_random_tile():
    import random
    return 2 if random.random() < 0.9 else 4

def format_grid(grid):
    return "\n".join(["\t".join(map(str, row)) for row in grid])