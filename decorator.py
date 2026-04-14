# Декоратор принимает функцию f как аргумент
# def count(f):
#     total = 0

#     # Объявляем функцию, которая расширяет функционал f
#     def decorated(*args, **kwargs):
#         # Переменная total объявлена нелокальной для доступа из внутренней функции
#         nonlocal total
#         total += 1
#        # Возвращаем значение исходной функции и дополнительно total
#         return f(*args, **kwargs), total
#    # Возвращаем новую функцию как объект
#     return decorated


# @count
# def hello(name):
#     return f"Привет, {name}!"

# print(hello("Пользователь_1"))
# print(hello("Пользователь_2"))


# def fib(n):
#     n_1, n_2 = 1, 1
#     for i in range(n):
#         yield n_1
#         n_1, n_2 = n_2, n_1 + n_2


# print(", ".join(str(x) for x in fib(10)))

# # Вывод программы:
# # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55


def answer(f):
    def decorated(*args, **kwargs):
        print(f"Функция вызывается с аргументами {args}{kwargs}")
        res = f(*args, **kwargs)
        print(f"Делаем что то после вызова функции")
        return res
    return decorated

@answer
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5))
print(a_plus_b(7, 9))
