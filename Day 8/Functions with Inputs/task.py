"""def greet():
    print(f"Hello")



def greet_with_name(name): #name is the parameter
    print(f"Hello {name}")


greet_with_name("Asad") #asad is the argument (value of the data)
greet_with_name("usama")
greet_with_name("zubair")
"""

"""You are given a list (or array) of numbers and a target number.
 Your goal is to find two numbers in the list that add up to the target. 
 Instead of returning the numbers themselves, you return their positions (indices) in the list."""

nums = [2,7,11,15]

target = 9

"""
0 + 1, 0 + 2, 0 + 3

7 + 2, 7 + 11, 7 + 15

11 + 2, 11 + 7, 11 + 15

15 + 2, 15 + 7, 15 + 11
"""
new_list = []

for number in range(len(nums)): # 0, 1, 2, 3
    for number2 in range(len(nums)):
        if (nums[number] + nums[number2]) == target:
            new_list.append(number)
            new_list.append(number2)
        else:
            print("you lost")
