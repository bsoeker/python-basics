from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age can not be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as err:
    pass
"""


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""


print("Code with raising exceptions = ", timeit(stmt=code1, number=10000))
print("Code without = ", timeit(stmt=code2, number=10000))

# Also notice that the except body is passed and if it did include some handling logic,
# the execution time would be even higher
