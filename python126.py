# Regular Expression
import re
text = "Order"

numbers = re.findall(r"\d+", text)
print("Numbers:" , numbers)

first_num = re.search(r"\d+", text)
if first_num:
    print("First number:", first_num.group())

masked = re.sub(r"\d", "*", text)
print("Masked:" , masked)
