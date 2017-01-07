import sys


string = """
Multiple lions off circus  were purloined. Identifiable, since barcoded the absent lions present dangerous
situation even for experts that accompany leos. Because the big critters are out, things becoming frantic.
Apparently planned, people stole the  big leos. Keepers and the all new temp guard hired Monday authorised
evacuation, noting a siren rang.  Through ringing alarm the lion region and a big exhibit around  circuses
depopulate rapidly, except heist gang who - using lorry had the big leo abductees all out.  Fraud pierrots
pretended work for animal trainer;the cat robbers drove quickly fleeing location, but the vehicle abandon,
switched other and police unaware location after. Then officers rapidly took cover in case shots fired cat
thieves et al. In a min a lad ( a local ) came . Signs of a fight in alley rear of the 7-11 in a suburb of
nearby spot were found also.Investigator viewing the site over four days but not able find robbers hideout
using scene data here. More investigator needed. One girl said seen lion and its lead near library.  Maybe
escape lion girl said, fuzz did not go. What was seen was just lynx said Sgt Jon Lane when covers transmit
public bulletins these days for HQ. One week was confused just leos  missing confused fuzz, however breaks
often later on.  Leads  for new way help !  Send Sgt Lane mark with LION for his fast action. Lions reward
offers also are posted! Aid for get leo captured will get max $$$$$$ reward. Zookeep friends annual passes
petting new leo litter. Any lad  or lass helper could put own moniker newborn twins.Vigilance will provide
the big $ ! Next will check phone for a sign of leads on lions. Vet of lions may also do a check of how we
expect leonines suffer via this ordeal abducted. Analyst describes the way abductees marketed through crim
market online. African big cat preserve management denies involved but say Interpol officers express claim
stolen beast  goes the way for new card of ID. This  claim  denied for that  safari reserve however; usual
dispose routes the East Asian. Yet even so all stole animal normal appears training performs big cat Vegas
gambling show. All new big cat are seen of new cadre officer track the cats  helping  finish it. Soon this
trade slowdown wanted. Hopeful eventual it will kill market, freed all the captured leonines the gang have
stolen allowing return. Zookeep desire big cat steal reverse robber jailed security improve lion can stay.
"""
string = string.replace(';',' ').replace('.', ' ').replace(',', ' ').replace('   ', ' _ ').replace('  ','_ ')

if 1 == 0:
    for word in string.split(' '):
        if word.lower().startswith('k'):
            print word

            
            
if 1 == 0:

    for word in string.split(' '):
        if word[0] in 'btck':
            for char in word:
                if ord(char) > 32:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write(char)
        else:
            for char in word:
                if ord(char) > 32:
                    sys.stdout.write('0')
                else:
                    sys.stdout.write(char)
        sys.stdout.write(' ')
        
        
if 1 == 0:
    for word in string.split(' ')[::-1]:

        sys.stdout.write(' ')
        if word.lower().startswith('k') or word.lower().startswith('b') or word.lower().startswith('c') or word.lower().startswith('t'):
            for char in word[::-1]:
                if ord(char) > 32:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write(char)

        else:
            for char in word[::-1]:
                if ord(char) > 32:
                    sys.stdout.write('0')
                else:
                    sys.stdout.write(char)


                    
                    
if 1 == 1:

    for word in string.split(' '):
        if word[0].lower() in 'btck':
            sys.stdout.write(word)
            sys.stdout.write(' ')
        else:
            pass


