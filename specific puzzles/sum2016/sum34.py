import lcy2dict


# this checks ??CTION?RY against the dictionary 
# you supply the range of letters ? could take

if __name__ == '__main__':
    str = raw_input("Input Query: ")
    
    # count how many question marks there are
    q_counts = str.count('?')
    
    rge = []
    all = '.'
    prompt_str = str
    for i in range(q_counts):
        prompt_str = prompt_str.replace('?','_',1)
        r_input = raw_input("Allowed Letters %s: " % prompt_str)
        rge.append(r_input)
    parsed_str = lcy2dict.parse_string(str,all,rge)
    print parsed_str
    matches = lcy2dict.check_wild_card(parsed_str)
    matches = [x.lower() for x in matches]
    print set(matches)
    