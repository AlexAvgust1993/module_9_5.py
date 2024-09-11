class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError()

        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration()
        current = self.pointer
        self.pointer += self.step
        return current



try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()














# import sys
# from itertools import repeat
#
#
# er_iterator = repeat('4', 100_000)
# print(er_iterator)
# print(f'Размер итератора - {sys.getsizeof(er_iterator)}')
#
# ex_str = '4' * 100_000
# print(f'Размер списка - {sys.getsizeof(ex_str)}')


# class Iter:
#
#     def __init__(self):
#         self.first = 'Первый элемент'
#         self.second = 'Второй элемент'
#         self.third = 'Третий элемент'
#         self.i = 0
#
#     def __iter__(self):
#         # обнуляем счётчик перед циклом
#         self.i = 0
#         # возвращаем ссылку на себя, так как сам объект должен быть итератором
#         return self
#
#     def __next__(self):
#         # этот метод возвращает значения по требованию Пайтона (ленивые вычисления)
#         self.i += 1
#         if self. i == 1:
#             return self.first
#         if self.i == 2:
#             return self.second
#         if self.i == 3:
#             return self.third
#         if self.i == 4:
#             return 'Подсчёт закончен'
#         raise StopIteration()  # Признак того что возвращать больше нечего

# obj = Iter()
# print(obj)
# for value in obj:
#     print(value)



# obj = Iter()
#
# try:
#     while True:
#         value = obj.__next__()
#         print(value)
# except StopIteration:
#     pass



# def fibonacci(n):
#     result = []
#     a, b = 0, 1
#     for _ in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result
#
#
# for value in fibonacci(n=10):
#     print(value)




# class Fibonacci:
#
#     def __init__(self, n):
#         self.i, self.a, self.b, self.n = 0, 0, 1, n
#
#     def __iter__(self):
#         self.i, self.a, self.b = 0, 0, 1
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > 1:
#             if self.i > self.n:
#                 raise StopIteration()
#             self.a, self.b = self.b, self.a + self.b
#         return self.a
#
# fib_iterator = Fibonacci(20)
# print(fib_iterator)
# for value in fib_iterator:
#     print(value)














