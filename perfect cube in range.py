start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
   # finding the cube root of the number
   root = num ** (1/3)
   # checking if the cube root is an integer
   if int(root + 0.5) ** 3 == num:
       print(num)
