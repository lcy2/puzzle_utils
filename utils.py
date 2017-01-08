import re

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


def checkdict(target_str, target_dict = used_dict):
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
    
def checkdictstart(str):
    """
    check whether there's a word that starts with string
    """

    
def check_wild_card(str):
    """
    wildcard lookup
    """
    
def parse_string(oldstr, all, rge = '.'):
    """
    parse a string for regex search
    """
    
    return 

if __name__ == '__main__':
#    mergedicts(used_dict, 'merged_dicts')
