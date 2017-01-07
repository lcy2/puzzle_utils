# order by a certain letter


wordlist = ['AKUND','APING','ASTER','AVAST', 'BANKS', 'BOUTS','CHILI', 'CHOIR','DONOR','ELECT','FORGE','FRODO','GROUD','GRAVE','INCUS','LEVIS','MODEL','MOUNT','OCTET','ORRIS','OUGHT','OVERT','PLAYS','RAPID','RATES','RECAP','REPEL','SAPPY','SHARK','SLICK','SMOKE','SPORT','STEER','TAKAR','TONES','TUSSY','VIDEO','VIRUS','WANDS','WRING']


revlist = sorted([x[3::-1] for x in wordlist])

for x in revlist:
    print(x[::-1])
    
    
    
    
    
#wordlist = ['RECAP','REPEL','STEER']
