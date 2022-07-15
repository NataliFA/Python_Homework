# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# num = int(input("Enter the day of the week: "))

# if (num > 0 and num < 6):
#     print("No")
# elif (num == 6 or num == 7):
#     print("Yes")
# else:
#     print("Incorrect number")

# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             first = not(x or y or z)
#             second = not(x) and not(y) and not(z)
#             if (first == second):
#                 print(f'{x}  {y}  {z}   {first}  {second}  {first == second}')
            
# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# xDot = int(input(("Input X coordinate: ")))
# yDot = int(input(("Input Y coordinate: ")))

# if (xDot > 0 and yDot > 0): print("1 quarter")
# elif (xDot < 0 and yDot > 0): print("2 quarter")
# elif (xDot < 0 and yDot < 0): print("3 quarter")
# elif (xDot > 0 and yDot < 0): print("4 quarter")
# else: print("Dot located on the axes!")

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# q = int(input(("Enter quarter number: ")))

# if (q > 4 or q < 0):
#     print("Incorrect number")
# else:
#     if (q == 1):
#         print("Point coordinate range Х > 0 and У > 0")
#     elif (q == 2):
#         print("Point coordinate range Х < 0 and У > 0")
#     elif (q == 3):
#         print("Point coordinate range Х < 0 and У < 0")
#     elif (q == 4):
#         print("Point coordinate range Х > 0 and У < 0")

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# import math

# x1 = float(input("Enter point coordinate X1: "))
# y1 = float(input("Enter point coordinate Y1: "))
# x2 = float(input("Enter point coordinate X2: "))
# y2 = float(input("Enter point coordinate Y2: "))

# result = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
# print(round(result,2))
