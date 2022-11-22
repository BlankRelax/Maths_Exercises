num_1 = int(input("Enter a num"))
num_2 = int(input("Enter another num"))
higher_number = 0
lower_number = 0

if num_1>num_2:
    higher_number = num_1
    lower_number = num_2
else:
    higher_number = num_2
    lower_number = num_1


for i in range(1,higher_number+1):
    if higher_number % i ==0 and lower_number % i == 0:
        gcd = i
print(gcd)

