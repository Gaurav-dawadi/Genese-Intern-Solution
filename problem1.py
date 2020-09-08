def compute():

    num = 2**1000

    sum = 0

    for x in str(num):

        sum = sum + int(x)

    return str(sum)

print(compute())        