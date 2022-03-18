from collections import deque

firework_effects = deque([int(el) for el in input().split(', ') if int(el) > 0])
explosive_power = [int(el) for el in input().split(', ') if int(el) > 0]
arsenal = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}

while firework_effects and explosive_power:
    current_firework = firework_effects.popleft()
    current_power = explosive_power.pop()
    curr_sum = current_firework + current_power
    if curr_sum % 15 == 0:
        arsenal["Crossette Fireworks"] += 1
    elif curr_sum % 5 == 0:
        arsenal["Willow Fireworks"] += 1
    elif curr_sum % 3 == 0:
        arsenal["Palm Fireworks"] += 1
    else:
        current_firework -= 1
        if current_firework <= 0:
            pass
        else:
            firework_effects.append(current_firework)
        explosive_power.append(current_power)
    curr_sum = 0

if arsenal.get("Palm Fireworks") >= 3 and arsenal.get("Willow Fireworks") >= 3 and arsenal.get(
        "Crossette Fireworks") >= 3:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(str(el) for el in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(el) for el in explosive_power)}")
for key in arsenal:
    print(f"{key}: {arsenal.get(key)}")
