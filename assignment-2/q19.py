def string_two_ends(str):

    if len(str)<2:
        return ''
    return str[0:2] + str[-2:]



print(string_two_ends('dhruvi'))
print(string_two_ends('12'))
print(string_two_ends('x'))