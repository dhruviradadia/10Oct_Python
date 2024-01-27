def chars_mixup(a,b):
    
    line_a=b[:2] + a[2:]
    line_b=a[:2] + b[2:]

    return line_a +' '+ line_b

print(chars_mixup('dhruvi ', 'radadiya'))
