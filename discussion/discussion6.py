# 1. Consider the following code and fill in what Python would print out.

# bag1 = Bag()
# def curried(f):
#     def outer(instance):
#         def inner(*args):
#             return f(instance, *args)
#         return inner
#     return outer
# add_binding = curried(Bag.add_skittle)
# bag1_add = add_binding(bag1)
# bag1.print_bag()
#  tuple skittle is empty > error?

# bag1.add_skittle(Skittle("blue"))
# bag1.print_bag()
#  "blue"

# bag1_add(Skittle("red"))
# bag1.add_skittle(Skittle("green"))
# bag1_add(Skittle("red"))
# bag1.print_bag()

# s = bag1.take_skittle()
# bag2 = Bag()
# bag2_add = add_binding(bag2)
# bag2.print_bag()

# bag2_add(Skittle("blue"))
# bag1.print_bag()

# bag2.print_bag()

