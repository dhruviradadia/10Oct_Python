def count_words(str):
    counts=dict()

    words=str.split()

    

    for word in words:

        if word in counts:
            counts[word]+=1

        else:
            counts[word]=1
    return counts     

print(count_words('i can do it than i make my parents proud i love to watch bl series'))


