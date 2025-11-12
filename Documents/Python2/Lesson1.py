# for i in range(6):
#     print("*" * i)



# for i in range(6):
#     print("* " * i)



# for i in range(5, 0, -1):
#     print("* " * i)
    
    
    
# for i in range(1, 6 , 1):
#     print(" " * (5-i), "*" * i)



# for i in range(1, 7 , 1):
#     print(" " * (6-i), "* " * i)




# for i in range(10):
#     print(" " * i + "*" * (2 * (10 - i) - 1))

# for i in range(2, 10 + 1):
#     print(" " * (10 - i) + "*" * (2 * i - 1))



# for i in range(1, 11):
#     print(" " * (10 - i) + "* " * i)

# for i in range(9, 0, -1):
#     print(" " * (10 - i) + "* " * i)


a = int(input())
b = int(input())
c = int(input())
print( (a + 1) // 2 + (b + 1) // 2 + (c + 1) // 2)



a = float(input())
print( (a % 30) * 12)



a = int(input())
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print("LEAP")
else:
    print("COMMON")


