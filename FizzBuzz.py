for fizzbuzz in range(1,16):
    if fizzbuzz == 15 :
        print("FizzBuzz")
        continue

    elif  fizzbuzz % 3 == 0:
        print("Fizz")
        continue

    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue

    print(fizzbuzz)