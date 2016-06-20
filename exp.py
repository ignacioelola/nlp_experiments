import gensim
import logging
import sys

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def book_to_sentences(filename):

    with open(filename, 'rb') as infile:

        sentences = []
        sentence = []
        for line in infile.readlines():

            clean_line = line.lower().replace('-', '').replace(',', '').replace(';', '').replace(':', '').replace('?', '.').replace('!', '.').replace('_', '').replace('\n', '').replace('\r', '').replace('\xef', '').replace('\xbb', '').replace('\xbf', '')
            if '.' in clean_line:
                for i in range(0, clean_line.count('.')):
                    sentence.extend(clean_line[:clean_line.find('.')].split())
                    sentences.append(sentence)
                    clean_line = clean_line[clean_line.find('.')+1:]
                    sentence = clean_line[:clean_line.find('.')].split()
            else:
                sentence.extend(clean_line.split())

    return sentences


def train_and_most_similar(filenames, word):

    for filename in filenames:

        sentences = book_to_sentences(filename)
        model = gensim.models.Word2Vec(sentences)
        if word in model:
            print('{0} most similar words to {1} are {2}'.format(filename.replace('.txt', ''), word, str(model.most_similar(word))))
        else:
            print('{0} model does not contain the word {1}'.format(filename.replace('.txt', ''), word))


if __name__ == '__main__':

    train_and_most_similar(['ulysses.txt', 'metamorphosis.txt', 'leaves_of_grass.txt', 'alices_adventures_in_wonderland.txt'], 'man')
