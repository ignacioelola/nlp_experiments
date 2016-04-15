import sys
import random


def generate_trigram(words):
    if len(words) < 3:
        return
    for i in xrange(len(words) - 2):
        yield (words[i], words[i+1], words[i+2])


def load_text(chain, file_name):

    fh = open(file_name, "r")

    for line in fh.readlines():
        words = line.split()
        for word1, word2, word3 in generate_trigram(words):
            key = (word1, word2)
            if key in chain:
                chain[key].append(word3)
            else:
                chain[key] = [word3]

    return chain


if __name__ == '__main__':

    fh = open("leaves_of_grass.txt", "r")

    chain = {}

    chain = load_text(chain, 'leaves_of_grass.txt')
    chain = load_text(chain, 'metamorphosis.txt')
    chain = load_text(chain, 'alices_adventures_in_wonderland.txt')
    chain = load_text(chain, 'ulysses.txt')
    
    print len(chain)

    sword1, sword2 = random.choice(chain.keys())  # This start a sentence from a random place, I need to find a word after a . to start from the beginning (which I can't in a dictionary), Idea: look for capital letters
    new_review = [sword1, sword2]
    
    for i in range(0,200):
        try:
            while True:
                sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
                new_review.append(sword2)
                if '.' in sword2:
                    print(' '.join(new_review))
                    new_review = [sword1, sword2]

        except:
            pass
            # print('Key not found')

