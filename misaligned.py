
def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
    return color_map

def print_color_map():
    color_map = generate_color_map()
    for entry in color_map:
        print(entry)
    return len(color_map)

# Strengthened Tests
color_map = generate_color_map()

# Checks misalignment. If the entries are misaligned, assert should fail
for index, entry in enumerate(color_map):
    parts = entry.split('|')
    assert len(parts) == 3, f"Entry {index} is incorrectly formatted: {entry}"
    assert parts[0].strip().isdigit(), f"Entry {index} index is not numeric: {entry}"
    assert len(parts[1].strip()) == 5 or len(parts[1].strip()) == 6, f"Entry {index} major color is misaligned: {entry}"
    assert len(parts[2].strip()) == 4 or len(parts[2].strip()) == 6, f"Entry {index} minor color is misaligned: {entry}"

result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")
