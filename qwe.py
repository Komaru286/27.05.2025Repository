def get_sq(a):
   return a * a

num = float(input("Введите число: "))
result = get_sq(num)
print(result)

def even(a):
   return a % 2 == 0

while True:
    a = int(input("Введите число: "))
    if(a == 1):
        break
    if even(a):
        print(a)






