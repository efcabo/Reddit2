from gensim import corpora, models
from pathlib import Path

path = Path.cwd()

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


def topic_modeling(texts: list, parameters, tfidf=True):
    """
    Crea o modelo cos parámetros indicados
    """

    texts = [text for text in texts if text != []]

    dictionary = corpora.Dictionary(texts)

    corpus = [dictionary.doc2bow(text) for text in texts]

    if tfidf:
        tfidf = models.TfidfModel(corpus)
        corpus = tfidf[corpus]

    lda_model = models.LdaMulticore(corpus=corpus,
                                    id2word=dictionary,
                                    num_topics=parameters['num_topics'],
                                    random_state=100,
                                    chunksize=100,
                                    passes=10,
                                    alpha=parameters['alpha'],
                                    eta=parameters['eta'])

    topics = lda_model.print_topics()

    return topics, dictionary, lda_model, corpus
