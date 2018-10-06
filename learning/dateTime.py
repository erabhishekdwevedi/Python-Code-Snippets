import datetime

value = datetime.datetime.now()

print(value)
print(value.strftime("%c"))


print(value.year)
print(value.strftime("%B"))
print(value.microsecond)

print(value.strftime("%c"))