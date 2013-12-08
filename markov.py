import random
import re

string = """Breast reduction for men is the fastest growing part of the cosmetic surgery industry for the second year running, plastic surgeons have said.

The number of such operations rose from 323 in 2008 to 581 last year - an 80% increase - the British Association of Aesthetic Plastic Surgeons said.

Pressure created by men's magazines was partly to blame, one surgeon said.

Cosmetic surgery appears to be defying the recession, with an overall increase in the number of procedures.

Nine out of 10 cosmetic procedures carried out by members of the British Association of Aesthetic Plastic Surgeons (Baaps) in 2009 were performed on women, with breast enlargement the most popular operation.

	
The public's interest in aesthetic surgery appears to remain strong and indeed growing quite considerably among UK males despite the the economic downturn
Nigel Mercer, Baaps

But the most dramatic rises were seen in the world of male surgery - an overall increase of more than a fifth over the year.

Surgeons carried out 581 breast reductions, compared to 323 the previous year.

The top two operations for men were rhinoplasty - or "nose-job", and blepharoplasty - surgery on the skin around the eyes.

Consultant plastic surgeon Rajiv Grover said that while the problem of so-called "man-boobs" - or "gynaecomastia" in official language - was not a new one, it had been thrust into prominence by media coverage.

He said: "Many men are feeling the pressure from men's magazines that weren't even being published five or six years ago.

"In addition, they are just realising that they can get something done about it."

Lifestyle not scalpel

However, he said that in many cases, surgery could be avoided by simple changes to lifestyle.

"Quite a few cases are caused by obesity, and we often say to men to look at their lifestyles before thinking about the scalpel."

A total of more than 36,000 surgical procedures were carried out by Baaps members, a 6.7% increase over last year. Women had 5.4% more procedures than in 2008.

Baaps president Nigel Mercer said: "The public's interest in aesthetic surgery appears to remain strong and indeed growing quite considerably among UK males despite the economic downturn." """

# """Ok. I appreciate this very much. I am just starting to use it so it's no surprise I went about it the wrong way. I was looking at the book "Learning Python" (O'Reilly edition) and they start by explaining two ways to run programs: directly from the Python Command Line in interactive mode (which means that all the work is lost upon exiting) or typing the commands in a text file and running it from the Dos (say) command line using "python nameoffile". I wanted to do something intermediary: having my program in a text file but loading it in the Python environment and running it there. I could not find how to do this from the book except using import."""

class Chain(object):
    """Markov Chain generator"""
    def __init__(self, source):
        self.dict = {0:RandomList([])} # 0 = start of lines
        for s in source:
            self.load(s)

    def load(self, source):
        words = source.strip().split(' ')
        if len(words) <= 1:
            return
        self.dict[0].append(words[0])
        for i in range(len(words)):
            word = words[i]
            try:
                next_word = words[i + 1]
            except IndexError:
                next_word = None
            if self.dict.has_key(word):
                self.dict[word].append(next_word)
            else:
                self.dict[word] = RandomList([next_word])

    def chain(self):
        result = ''
        li = []
        words = RandomList(self.dict.keys()) 
        word = self.dict[0].rand_element()
        while word != None:
            result += word + ' '
            if re.match(r'.+\.', word):
                break
            word = self.dict[word].rand_element()
        return result

def n():
    return Chain(string.splitlines()).chain()

class RandomList(list):
    def rand_element(self):
        return self[random.randrange(0, len(self))]

print n()
    
