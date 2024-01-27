def in_middal_string(str,word):
    return str[:2]+ word + str[-2:]


print(in_middal_string('[[]]','janvi'))
print(in_middal_string('{{}}','python'))
print(in_middal_string('<<>>','html'))