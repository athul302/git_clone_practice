num = int(input("enter the numbber"))

for i in range(2,num):

    if i % num == 0:

        print("not prime")

else:

    print("prime")