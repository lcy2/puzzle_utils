import re

used_dict = ['eng_com.dic', 'Ise.dic','linuxwords']

def checkdict(str):
    """
    check whether a string exists in the dictionary
    """
    for chosen_dict in used_dict:
        with open(chosen_dict) as fdict:
            #print re.search(string, fdict.read()).group(0)
            if re.search(r'\b%s\b' % str, fdict.read(),re.IGNORECASE) != None:
                return True
    
    return False
    
def checkdictstart(str):
    """
    check whether there's a word that starts with string
    """
    for chosen_dict in used_dict:
        with open(chosen_dict) as fdict:
            if re.search(r'\b%s' % str, fdict.read(), re.IGNORECASE) != None:
                return True
    return False
    
def check_wild_card(str):
    """
    wildcard lookup
    """
    m = []
    for chosen_dict in used_dict:
        with open(chosen_dict) as fdict:
            m.extend(re.findall(r'\b%s\b' % str, fdict.read(), re.IGNORECASE))
    return m
    
def parse_string(str, all, rge = '.'):
    """
    parse a string for regex search
    """
    if all != '.':
        all = '['+ all +']'
    # turn ? into wildcard "."
    if rge == '.':
        newstring = str.replace('?','%s' % all)
    else:
        newstring = str
        for rpl in rge:
            if rpl[0] == '-':
                chr_list = [chrs for chrs in all if chrs not in rpl]
                newstring = newstring.replace('?', '%s' % ''.join(chr_list), 1)
            else:
                newstring = newstring.replace('?', '[%s]' % rpl, 1)
            #print newstring
    
    return newstring