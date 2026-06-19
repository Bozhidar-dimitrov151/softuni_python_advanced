def draw_cards(*args, **kwargs):
    monster_cards = []
    spell_cards = []
    result = ''

    for name, type in (list(args) + list(kwargs.items())):
        if type == "monster":
            monster_cards.append(f"  ***{name}")
        elif type == "spell":
            spell_cards.append(f"  $$${name}")

    if monster_cards:
        result = "Monster cards:\n" + "\n".join(sorted(monster_cards, reverse=True))
    if spell_cards:
        result += "\nSpell cards:\n" + "\n".join(sorted(spell_cards))

    return result.strip()
