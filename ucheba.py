
# def gcd3(a: int, b: int) -> int:
#     """Наибольший общий делитель (НОД) для неотрицательных целых чисел."""
#     assert a >= 0 and b >= 0, "Числа должны быть неотрицательными"
    
#     if a == 0 or b == 0:
#         return max(a, b)
#     return gcd3(b % a, a)

# print(gcd3(48, 18))
from collections import defaultdict
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 25},
    {"name": "David", "age": None},
    {"name": "Eve"},
    {"name": "Frank", "age": 30},
]
res = defaultdict(list)
for user in users:
    age = user.get("age")
    if age is not None and isinstance(age, int):
        res[age].append(user["name"])
print(res)