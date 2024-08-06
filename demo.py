def  sum_of_list(numbers):
    total=0
    for num in numbers:
        total += num
    return total
numbers=[1,2,3,4,5,6,7,8,9,10,11]
result= sum_of_list(numbers)
print(f"The list is:{numbers}")
print(f"The sum of numbers in the given list is:  {result}")