# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

binary = []
hex = []
hex_check = 0
hex_basic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

x = int(input("Enter a number: "))
for i in range(0, 1000):
    y = random.randint(0, 100)
    if x == y:
        print("Is this your number? ", y)
        print("Took this many rolls: ", i)

        binary_answer = x
        hex_answer = x

        for w in range(0, x):
            # Binary part

            binary.append(binary_answer % 2)
            binary_answer = int(binary_answer / 2)

            # Hex part
            hex_check = hex_answer % 16

            for n in range(0, 16):
                if hex_basic[n] == hex_check:
                    hex.append(hex_basic[n])
            hex_answer = int(hex_answer / 16)

        binary.reverse()
        hex.reverse()

        for b in range(0, x):
            if binary[b] == 1:
                del binary[0:b]
                break
        for a in range(0, x):
            if hex[a] != 0:
                del hex[0:a]
                break

        print("This is the number in binary: 0b", end ='')

        for i in range (0,len(binary)):
            print(binary[i], end='')
        print('')

        print("This is the number in hex: 0x", end ='')

        for i in range(0,len(hex)):
            if hex[i] < 10:
                print(hex[i],end='')

            else:

                if hex[i] == 10:
                    print('A', end='')
                if hex[i] == 11:
                    print('B', end='')
                if hex[i] == 12:
                    print('C', end='')
                if hex[i] == 13:
                    print('D', end='')
                if hex[i] == 14:
                    print('E', end='')
                else:
                    print('F', end='')

        print('')
        break
