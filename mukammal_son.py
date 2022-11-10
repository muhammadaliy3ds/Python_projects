def mukammal_son(m):
    """Mukammal sonni aniqlaydigan dastur"""
    x_list = list(range(1, m))
    nb = []
    for n in x_list:
        if m % n == 0:
            nb.append(n)
    if m == sum(nb):
        return print(f"{m}-mukammal son!")
    else:
        return print(f"{m}-murakkab son!")

mukammal_son(33550336)
