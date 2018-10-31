# -*- coding: utf-8 -*-
'''
Can you write a simple list comprehension to convert these names to title case (brad pitt -> Brad Pitt). Or reverse the first and last name? 

Then use this same list and make a little generator, for example to randomly return a pair of names, try to make this work:

pairs = gen_pairs()
for _ in range(10):
    next(pairs)

Should print (values might change as random):

Arnold teams up with Brad
Alec teams up with Julian

Have fun!

'''
import random


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
         
         
def gen_lst(lst):
    template = '{} teams up with {}'
    while True:
        name1,*etc = random.choice(lst).split()
        name2,*etc = random.choice(lst).split()
        yield template.format(name1,name2)
if __name__ == '__main__':
    lst = [name.title() for name in NAMES]
    print(lst)
    g1 = gen_lst(lst)
    print(next(g1))
    print(next(g1))
    print(next(g1))
