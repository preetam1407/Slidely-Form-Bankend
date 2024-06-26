import random

# Below function is used to create random data which ensure to have mix of overlapping and non-overlapping data.
def generate_grouped_elements(num_groups, elements_per_group, max_x=120, group_height=15, vertical_spacing=20):
    elements = []
    current_top = 5
    for g in range(num_groups):
        for i in range(elements_per_group):
            x = random.randint(1, max_x)
            top_variation = random.randint(0, 5)  
            bottom_variation = random.randint(10, group_height)  
            top = current_top + top_variation
            bottom = top + bottom_variation
            elements.append({'content': f'Group {g+1} Element {i + 1}', 'x': x, 'top': top, 'bottom': bottom})
        current_top += group_height + vertical_spacing  
    return elements

# Jumbled the created data.
def jumble_elements(elements):
    random.shuffle(elements)
    return elements

def print_elements(elements, title="Elements"):
    print(f"{title}:")
    for element in elements:
        print(f"{element['content']}: x={element['x']}, top={element['top']}, bottom={element['bottom']}")

# Algorithm to arrange the elements in rows according to their coordinates and overlapping conditions.
def arrange_elements(elements):
    # Sort elements by their top coordinates
    elements.sort(key=lambda e: e['top'])

    rows = []
    # This condition check if the current element is overlapping with the already appended elements or not.
    def overlaps(e1, e2):
        return not (e1['bottom'] < e2['top'] or e1['top'] > e2['bottom'])

    for element in elements:
        # initially placed is false, if the element is not overlapping with any of the existing row then it will be placed in a new row.
        placed = False
        print(f"\nPlacing {element['content']} (top={element['top']}, bottom={element['bottom']})")
        '''
        iterating over the rows to see if overalpping is there or not. 
        here the placed varaible is switched if row is overlapping is present.
        '''
        for row in rows:
            if any(overlaps(element, other) for other in row):
                row.append(element)
                placed = True
                print(f" -> Appended to existing row. Row now has {[el['content'] for el in row]}")
                break
        if not placed:
            rows.append([element])
            print(f" -> Created new row with {element['content']}")


    i = 0
    while i < len(rows):
        merged = False
        j = i + 1
        while j < len(rows):
            if any(overlaps(elem1, elem2) for elem1 in rows[i] for elem2 in rows[j]):
                print(f"Merging row {j+1} into row {i+1}")
                rows[i].extend(rows[j])
                del rows[j]
                merged = True
                print(f"Row {i+1} after merge: {[el['content'] for el in rows[i]]}")
            else:
                j += 1
        if not merged:
            i += 1

    return rows

# Generate elements in groups
num_groups = 4
elements_per_group = 3
elements = generate_grouped_elements(num_groups, elements_per_group)

# Jumble elements before printing and processing
jumbled_elements = jumble_elements(elements.copy())
print_elements(jumbled_elements, "Jumbled Elements")

# Arrange the elements into rows
arranged_rows = arrange_elements(jumbled_elements)

# Output the arranged rows
print("\nFinal Arranged Rows:")
for idx, row in enumerate(arranged_rows, 1):
    print(f"Row {idx}: {[el['content'] for el in row]}")

