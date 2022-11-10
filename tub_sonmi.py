def tub_son(x):
    """Sonning tub yoki murakkab
    ekanligini aniqlovchi funksiya"""
    x_list = list(range(2,x))
    qoldiqlar = []
    if x == 2:
        return print((f'{x}-tub son!'))
    for k in x_list:
        qoldiqlar.append(x % k)
    if 0 in qoldiqlar:
        return print(f'{x}-murakkab son!')
    else:
        return print(f'{x}-tub son!')

tub_son(1001)






# x = int(input(""))
# x_list = list(range(2,x))
# qoldiqlar = []
#
# for k in x_list:
#     qoldiqlar.append(x % k)
#
# print(qoldiqlar)
# 0 in qoldiqlar

# lt = [0, 2, 4, 6]
# print(1 in lt)