name = "John"
age = 20
lang = "Python"
hours = 3
# John is 20 year old.He studies Python 3 hours a day
print(name,"is",age,"year old.He is studies",lang,hours,"hours of a day")

# using fstring
print(f"{name} is {age} year old.he is studies {lang} {hours} hours of a day")

sub1 = 78
sub2 = 87
sub3 = 83

# print(f"{name} scored {sub1 + sub2 + sub3} marks in total")
percent = (sub1 + sub2 + sub3) / 3
print(f"{name} got {percent}%")