while True:
    print("Press 0 to exit")

    N = int(input("Enter a number N: "))


    exit = 0
    if N == 0:
        break

    squares = []

    for num in range(1, N + 1):
        squares.append(num ** 2)
    

    print(f"✔️ {squares}")