from .pos_tagging import *


def search_texts(texts, search_word, search_tag):
    """
    Devolve unha lista cos textos nos que aparece a palabra indicada sempre que pertenza a categoría pasada como parámtro
    """
    toret = []

    tags = {'Nouns': ['NN', 'NNS', 'NNP', 'NNPS'],
            'Personal pronouns': ['PRP'],
            'Possesives': ['PRP$'],
            'Adverbs': ['RB', 'RBR', 'RBS'],
            'Adjectives': ['JJ', 'JJR', 'JJS'],
            'Verbs': ['VBD', 'VBG', 'VBN', 'VBP', 'VBZ']}

    for text in texts:
        tokens_tag = pos_tagging(text)

        if search_word.lower() in [word.lower() for line in tokens_tag
                                   for word, tag in line if tag in tags[search_tag]]:
            toret.append(text)

    return toret
