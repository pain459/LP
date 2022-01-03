def divisors(integer):
    divisors_list = []
    for i in range(1, integer + 1):
        if integer % i == 0 and i not in [1, integer]:
            divisors_list.append(i)
            # print(divisors_list)
        else:
            pass
    if len(divisors_list) == 0:
        return f'{integer} is prime'
    else:
        return divisors_list


print(divisors(12)) #should return [2,3,4,6]
print(divisors(25)) #should return [5]
print(divisors(13)) #should return "13 is prime"