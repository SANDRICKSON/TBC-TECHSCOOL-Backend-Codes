def kilometres_to_miles(num):
    return num / 1.6


def calculate_volume(a=1, b=1,c=1):
    return a*b*c

def calculate_average(*nums):
    if len(nums)==0:
        return 0
    return sum(nums) / len(nums)

def get_vowels(*words):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return [word for word in words if word and word[0] in vowels]


print(kilometres_to_miles(9))
print(calculate_volume(2, 3, 4))
print(calculate_volume(2, 3))
print(calculate_volume(2))
print(calculate_average(9, 6, 4, 2, 3))
print(get_vowels("Asia", "Africa", "Sandro", "Gvantsa", "Eka"))