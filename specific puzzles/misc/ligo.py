import re
import sys
import lcy2dict


morse = {
    '.-'    : 'A',
    '-...'  : 'B',
    '-.-.'  : 'C',
    '-..'   : 'D',
    '.'     : 'E',
    '..-.'  : 'F',
    '--.'   : 'G',
    '....'  : 'H',
    '..'    : 'I',
    '.---'  : 'J',
    '-.-'   : 'K',
    '.-..'  : 'L',
    '--'    : 'M',
    '-.'    : 'N',
    '---'   : 'O',
    '.--.'  : 'P',
    '--.-'  : 'Q',
    '.-.'   : 'R',
    '...'   : 'S',
    '-'     : 'T',
    '..-'   : 'U',
    '...-'  : 'V',
    '.--'   : 'W',
    '-..-'  : 'X',
    '-.--'  : 'Y',
    '--..'  : 'Z'
    }
    
def findMorse(ptx,rmd, leadtext):
    """
    a recursive function for finding all possible
    word combinations given a block of Morse strings
    ptx: plaintext
    rmd: remainder of the Morse code

    """
    # initial screen
    # if we have ptx+leadtext that is 3 letters long
    # check whether such prefix exists in dict
    #print "leadtext is %s and checking %s" % (leadtext, ptx)
    if leadtext != '+++++':

        if not lcy2dict.checkdictstart((leadtext+ptx)):
            #print "\tFAIL!"
            return []
    
    
    testlen = 4 if len(rmd) >=4 else len(rmd)
    mrsComb = []
    if testlen == 0:
        #print ptx
        return [ptx]
    for i in range(testlen,0,-1):
        if rmd[0:i] in morse:
            #print "%s with testlen @ %d iterator %d" % (ptx+rmd, testlen, i)
            mrsComb.extend(findMorse(ptx+morse[rmd[0:i]], rmd[i:], leadtext))

    
    return mrsComb
            
            
def morseSolve(mStr):
    """
    The function to solve a morse code
    with parts of the string already revealed,
    this function will divy up the work
    """
    morseParts = []
    
    while len(mStr) > 0 :
        if mStr[0] in '-.':
            morsePart = re.match(r'[-.]+', mStr).group(0)
            
            # initial filter
            # Using letter frequency and length of each letter's Morse rep
            # average letter Morse code rep length ~ 2.54167
            # Probably safe to screen out anything that's 1.5 or below

            #morseParts.append([trans for trans in findMorse('', morsePart)
            #    if len(trans)*2 < len(morsePart)])
            
            
            morseParts.append(findMorse('', morsePart,
                ''.join(morseParts) if len(morseParts) <= 1 else '+++++' ))
            
            mStr = mStr[len(morsePart):]
        else:
            morseParts.append(mStr[0])
            
            # if this is the second item
            # first item must be a list
            # test all the beginnings
            if len(morseParts) == 2:
                morseParts[0] = [trans for trans in morseParts[0]
                    if lcy2dict.checkdictstart(trans+mStr[0])]

            mStr = mStr[1:]            
            
    return join_m_combs('', morseParts)
            
def join_m_combs(testStr, mList):
    """
    this function produces all the possible 
    string segments into one continuous word
    and check whether it's in the dictionary
    It won't check the full string if the first
    block is not a prefix found in the dictionary
    """
    validWords = []
    if len(mList) == 0:
        clear_and_display("\r\tChecking %s..." % testStr)

        if lcy2dict.checkdict(testStr):
            print testStr
            return [testStr]
        else:
            #print "%s is not a valid word" % testStr
            return None
    else:
        currmPart = mList[0]
        

        
        # if it's a list
        if not isinstance(currmPart, basestring):
            for mPart in currmPart:
                # check whether current prefix
                # exists in the wordlist
                if not lcy2dict.checkdictstart(testStr+mPart):
                    
                    clear_and_display("\r\tChecking Prefix %s..." % (testStr+mPart))
                    continue
                    
                    
                    
                returnWord = join_m_combs(testStr+mPart, mList[1:])
                if returnWord != None:
                    validWords.extend(returnWord)
        else: # if it's not a list
            # check whether current prefix
            # exists in the wordlist
            if not lcy2dict.checkdictstart(testStr+currmPart):
                clear_and_display("\r\tChecking Prefix %s..." % (testStr+currmPart))
                return validWords
            validWords.extend(join_m_combs(testStr+currmPart, mList[1:]))
    return validWords
                

    
def clear_and_display(string):
    sys.stdout.write("\x1b[2K")
    print string,
    
    
    #print morseParts
            
            
code = [
    '-....-..O-.-.-.-',
    '-...R..--.-',
    '-....-..-N-..',
    'B..-...-..-..',
    'P...-.-..',
    '-...O.-.-.-..',
    'C---.-..---.-.'
    ]
    
for i, codeline in enumerate(code):

    clear_and_display("\rLine %d:\n" % (i+1))
    morseSolve(codeline)
    
    clear_and_display('')
#print findMorse('','-.-.-.-',True)