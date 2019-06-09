
# def gen():
#     print("line 1")
#     yield 1
#     print("line 2")
#     yield 2
#     print("line 3")
#     return 3
#
#
# next(gen())
# next(gen())
# next(gen())
# g = gen()
# next(g)
# next(g)
# next(g)


# def inc():
#     for i in range(5):
#          yield i
#
#
# print(type(inc),id(inc()))
# print(type(inc()),id(inc()))
# print(next(inc()),id(inc()))
# print(next(inc()))
# print(next(inc()))
# x = inc()
# y = inc()
# print(type(x), id(x))
# print(type(y), id(y))
# print(next(x),id(x))
# print(next(x),id(x))
# print(next(x))
#
# y = (i for i in range(5))
# print(type(y))
# print(next(y))
# print(next(y))

def inc():
    def counter():
        i = 0
        while True:
            i += 1
            yield i
    c = counter()
    return lambda : next(c)

foo = inc()
print(inc()())
print(inc()())