enemies = 1


def increase_enemies():
    # Local Scope
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Scope
player_health = 10


def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health + potion_strength)


drink_potion()
print(player_health)
