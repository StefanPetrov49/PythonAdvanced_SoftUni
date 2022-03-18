from collections import deque

materials = [int(el) for el in input().split()]
magic = deque([int(el) for el in input().split()])


def check_gift(number, gifts):
    if 100 <= number <= 199:
        gifts['Gemstone'] += 1
    elif 200 <= number <= 299:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= result <= 399:
        gifts['Gold'] += 1
    elif 400 <= result <= 499:
        gifts['Diamond Jewellery'] += 1


are_made = False
gem_sculp = False
gold_diam = False
gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}
while materials and magic:
    if gifts['Gemstone'] == 1 and gifts['Porcelain Sculpture'] == 1:
        are_made = True
        if gold_diam:
            pass
        else:
            gem_sculp = True

    if gifts['Gold'] == 1 and gifts['Diamond Jewellery'] == 1:
        are_made = True
        if gem_sculp:
            pass
        else:
            gold_diam = True

    curr_material = materials.pop()
    curr_magic = magic.popleft()
    result = curr_magic + curr_material
    if result < 100:
        if result % 2 == 0:
            result = (curr_material * 2) + (curr_magic * 3)
        else:
            result = result * 2
        check_gift(result, gifts)
    elif result >= 500:
        result /= 2
        check_gift(result, gifts)

    else:
        check_gift(result, gifts)

if are_made:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(el) for el in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(el) for el in magic)}")
if gem_sculp:
    print(f"Gemstone: {gifts.get('Gemstone')}")
    print(f"Porcelain Sculpture: {gifts.get('Porcelain Sculpture')}")
elif gold_diam:
    print(f"Gold: {gifts.get('Gold')}")
    print(f"Diamond Jewellery: {gifts.get('Diamond Jewellery')}")
else:
    for el in gifts:
        if gifts[el] > 0:
            print(f"{el}: {gifts.get(el)}")
