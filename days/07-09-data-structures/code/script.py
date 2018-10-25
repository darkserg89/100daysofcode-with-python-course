# -*- coding: utf-8 -*-
import json
import collections

from data import us_state_abbrev,states_list
from pprint import pprint

def pop_up_element(dictionary,number):
    if len(dictionary) < number:
        raise ValueError("There is no such element in the dict")
    ord_dict = collections.OrderedDict(dictionary)
    i = 0
    for num,key in enumerate(ord_dict):
        if num==number:
            print('Element number {} has key={} and value={}'.format(num,key,ord_dict[key]))









if __name__== '__main__':
    pop_up_element(us_state_abbrev,60)
    pprint(us_state_abbrev)
