operation = input()
if operation == "odd_num_check":
    number = int(input())
    if number %2 != 0:
        print("yes")
    else:
        print("no")

elif operation == "perfect_square_check":
    number = int(input())
    if number>=0 and (number**0.5).is_integer():
        print("yes")
    else:
        print("no")

elif operation == "vowel_check":
    text = input().lower()
    vowels ="aeiou"
    has_vowel=False
    for char in text:
        if char in vowels:
            has_vowel=True
            break
    if has_vowel:
        print("yes")
    else:
        print("no")
    
elif operation == "divisibility_check":
    number = int(input())
    div2 = number % 2 == 0
    div3 = number % 3 == 0
    if div2 and div3:
        print("divisible by 2 and 3")
    elif div2:
        print("divisible by 2")
    elif div3:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")
elif operation == "palindrominator":
    text = input()
    reversed_part=text[:-1][::-1]
    print(text+reversed_part)
elif operation == "simple_interest":
    principal = int(input())
    n_years = int(input())
    if n_years <10:
        rate = 5
    else:
        rate = 8
    simple_interest = (principal*rate*n_years)/100
    print(round(simple_interest))
else:
    print("Invalid Operation")