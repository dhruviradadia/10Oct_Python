def reverse_string(str):
    if len(str) %4==0:
        return ''.join(reversed(str))
    return str


print(reverse_string('foxs'))
print(reverse_string('1234'))