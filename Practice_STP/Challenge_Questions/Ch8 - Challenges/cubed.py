def default(c):
    try:
        print(float(c) ** 3)
    except(ValueError):
        print("Must be a real number")