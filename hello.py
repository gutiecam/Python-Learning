## name = ["Cam", "Alex", "Jo"]

##for i, name in enumerate(name, start=100):
##    print(f"{i}. Hello, {name}!")

def get_even(numbers):
    result = []
    for n in numbers:
        if n%2 == 0:
            result.append(n)
    return result
    pass
print (get_even([1, 2, 3, 4, 5, 6]))