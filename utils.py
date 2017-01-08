import re
import timeit
import itertools


#used_dict = ['linuxwords', 'eng_com.dic', 'Ise.dic']

def mergedicts(initial_dicts, target_dict):
    first_dict = True
    res_set = set()
    for chosen_dict in initial_dicts:
        with open(chosen_dict) as targetdict:
            res_set |= set([x for x in targetdict])

    results = list(res_set)
    results.sort(key = lambda x: x.lower())

    with open(target_dict,'w') as target:
        for line in results:
            target.write(line)


