#  syntax error
# module not found
# value error
#
a = [1, 2, 3]
a.remove(1)


x = -5
# if x < 0:
#     raise Exception("x should be positive")


# assert x >= 0, "x is not positive"

try:
    a = 5 / 0
except Exception as e:
    print("an error happend", e)
else:
    print("everything is fine")
finally:
    print("cleaning up")
