def main():
    with open("puzzle.txt", "r") as f:
        puzzle = f.readlines()

    ingredients_ids = []
    ingredient_id_ranges = []

    id_ranges_section = True
    for line in puzzle:
        if line == "\n":
            id_ranges_section = False
            continue

        if id_ranges_section:
            start, end = line.split("-")
            rng = range(int(start), int(end) + 1)
            ingredient_id_ranges.append(rng)
        else:
            ingredients_ids.append(int(line))

    def is_ingredient_fresh(ingredient_id: int) -> bool:
        for r in ingredient_id_ranges:
            if ingredient_id in r:
                return True

        return False

    count = 0
    for ingredients_id in ingredients_ids:
        if is_ingredient_fresh(ingredients_id):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
