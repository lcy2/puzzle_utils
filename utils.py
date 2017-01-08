import re
import timeit

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


def checkdict(target_str, target_dict):
    """
    check whether a string exists in the dictionary
    """
    for chosen_dict in target_dict:
        try:
            with open(chosen_dict) as fdict:
                #print re.search(string, fdict.read()).group(0)
                if re.search(r'\b%s\b' % target_str, fdict.read()) != None:
                    return True
        except IOError:
            continue
    
    return False
    
    
def match(query_strs, used_dict):
    """
    wildcard lookup
    """
    result_set = []

    query = '|'.join([x for x in query_strs])
    #print query

    try:
        with open(used_dict, 'r') as target_dict:
            result_set.append(re.findall(query, target_dict.read(),re.IGNORECASE))

    except IOError:
        print 'File not Found.'
        return None
    
    return result_set

def seq_match(query_strs, used_dict):
    pass
    
def parse_string(oldstr, all, rge = '.'):
    """
    wildcard search
    """
    pass 

if __name__ == '__main__':
    #print timeit.timeit("match([r'(\\b[Ab]aron\\b)(\\bThom[asdfsaw][sbf]\\b)'], 'merged_dicts')", setup = 'from __main__ import match', number = 100)

    #print timeit.timeit("match([r'\\bThom[asdfsaw][sbf]\\b'], 'merged_dicts')", setup = 'from __main__ import match', number = 100)

    print match([r'\bThom[asdfsw][sbf]\b', r'\b[Ab]aron\b'], 'merged_dicts')
    print timeit.timeit("match([r'\\bThom[asdfsw][sbf]\\b', r'\\b[Ab]aron\\b'], 'merged_dicts')", setup = 'from __main__ import match', number = 100)

    print timeit.timeit("match([r'\\b[Ab]aron\\b'], 'merged_dicts')", setup = 'from __main__ import match', number = 100)
    
    print timeit.timeit("match([r'\\bThom[asdfsw][sbf]\\b'], 'merged_dicts')", setup = 'from __main__ import match', number = 100)
