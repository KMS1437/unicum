print("Камозин Михаил\nИИ-71\nСложный уровень\n")

print("1 задача\n")
from itertools import permutations
per = permutations('1234', 3)
for i in per:
    print(''.join(i))

print("\n2 задача\n")
from itertools import permutations
per = permutations('123', 2)
for i in per:
    print(''.join(i))

print("\n3 задача\n")
import itertools
subjects_of_sigma = ['математика', 'информатика', 'русский язык']
combins = list(itertools.product(subjects_of_sigma, repeat=2))
for combin in combins:
    print(combin[0], '\n', combin[1], '\n')
