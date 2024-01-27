from collections import Counter

list = [{'item': 'item1', 'amount': 500}, {'item': 'item2', 'amount': 600}, {'item': 'item2', 'amount': 750}]

result = Counter()

for d in list:
    result[d['item']] += d['amount']

print(result)