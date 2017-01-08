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
    
    if not isinstance(query_strs, list):
        query_strs = [query_strs]

    query = '|'.join([x for x in query_strs])
    #print query

    try:
        with open(used_dict, 'r') as target_dict:
            result_set = re.findall(query, target_dict.read(),re.IGNORECASE)

    except IOError:
        print 'File not Found.'
        return None
    
    return result_set

def parse_query(wp):
    return r'\b{0}\b'.format(''.join(wp.modular_qstr))



def anagram(wp):
    """
    from one word puzzle object
    create anagram word puzzle objects of it
    """
    wp_list = [word_puzzle(list(x), modq = True) for x in itertools.permutations(wp.modular_qstr)]
    wp_list.sort(key = lambda x: x.modular_qstr)
    return wp_list


class word_puzzle(object):
    
    def __init__(self, query, subs= [], modq = False):
        
        if modq:
            self.modular_qstr = query
            self.qstr = ''

        # if a query string is supplied
        # in the form of ??fsa??fooab?
        
        else:
            self.qstr = query
            if query == '':
                raise ValueError('Please supply a query.')
            # decompose it
            elif subs == []:
                self.modular_qstr = ['.' if x == '?' else x for x in self.qstr]
            elif self.qstr.count('?') != len(subs):
                raise ValueError('Incorrect number of substitutions.')
            else:
                newsubs = [''.join(sorted(list(set(x)))) for x in subs]
                sub_iter = iter(newsubs)
                self.modular_qstr = ['[{}]'.format(sub_iter.next()) if x == '?' else x for x in self.qstr]
        
        #print self.modular_qstr

        

if __name__ == '__main__':
    pz = word_puzzle('t?o?as',subs = ['hdfjs','asdmfsa'])
    qstrs = parse_query(pz)
    print match(qstrs, 'merged_dict')

    anags = anagram(pz)
    qstrs = [parse_query(anag) for anag in anags]
    #print qstrs
    print match(qstrs, 'merged_dict')

    #print timeit.timeit("match([r'\\bThom[asdfsw][sbf]\\b', r'\\b[Ab]aron\\b'], 'merged_dicts')", setup = 'from __main__ import match', number = 100)

    #print timeit.timeit("match([r'\\b[Ab]aron\\b'], 'merged_dicts')", setup = 'from __main__ import match', number = 100)
    
    #print timeit.timeit("match([r'\\bThom[asdfsw][sbf]\\b'], 'merged_dicts')", setup = 'from __main__ import match', number = 100)
