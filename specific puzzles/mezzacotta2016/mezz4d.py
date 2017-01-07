import sys

#sublist= '_y____t___l______e_____ah_'
orglist= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sublist= '_yk_dga_ivlhujbtserf_cponm'

with open('mezz4dtxt.txt') as fn:
    for line in fn:
        line = line.upper()
        for char in range(0,26):
            #print char
            if sublist[char] != '_':
                line = line.replace(chr(65+char),sublist[char])
        sys.stdout.write(line)
        

        
freq1 = [0] * 26
#print freq1
with open('mezz4dtxt.txt') as fn:

    for line in fn:
        for char in line:
            if ord(char) >= 65:
                #print ord(char)
                freq1[ord(char)-65] += 1
            
freq1tup = tuple((chr(i+65), freq1[i]) for i in range(0,26))
print "Printing out the letter frequency"
print sorted(freq1tup, key = lambda tup:tup[1])[::-1]


grams = []
gfreq = []

def existInGram(substr):
    for i, gram in enumerate(grams):
        if substr == gram:
            gfreq[i] += 1
            return True
    grams.append(substr)
    gfreq.append(1)
    return False


def firstfew(num):
    with open('mezz4dtxt.txt') as fn:

        for line in fn:
            for words in line.split(' '):
            # see whether it already exists in the grams list
                #print words
                existInGram(words[0:num])
                                    
def ngramanywhere(num):
    with open('mezz4dtxt.txt') as fn:

        for line in fn:
            for words in line.split(' '):
            # see whether it already exists in the grams list
                #print words
                words = words.strip()
                base = 0
                #print "%s, %d" % (words, len(words))
                while base+num <= len(words):
                    existInGram(words[base:base+num])
                    base+=1
                    
                    
#firstfew(3)
#freq1stfew = tuple((grams[i],gfreq[i]) for i in range(0, len(grams)))
#print "Printing out the frequency of " + str(len(grams[0])) + "-grams at the beginning of each word"
#print sorted(freq1stfew, key = lambda tup: tup[1])[::-1]


n = 2
ngramanywhere(n)
ngramfew = tuple((grams[i],gfreq[i]) for i in range(0, len(grams)))
print "Printing out the frequency of " + str(n) + "-grams"
print sorted(ngramfew, key = lambda tup: tup[1])[::-1]
