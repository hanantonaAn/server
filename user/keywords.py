import pymorphy2
import yake
import inspect
from collections import namedtuple

def SearchWords(text):
    if not hasattr(inspect, 'getargspec'):
        def getargspec(func):
            inspect_result = inspect.getfullargspec(func)
            ArgSpec = namedtuple('ArgSpec', 'args varargs keywords defaults')
            return ArgSpec(
                inspect_result.args, inspect_result.varargs,
                inspect_result.varkw, inspect_result.defaults
            )
        inspect.getargspec = getargspec

    morph = pymorphy2.MorphAnalyzer()

    words = text.split()

    filtered_words = [word for word in words if not morph.parse(word)[0].tag.POS == 'VERB']

    test_text = ' '.join(filtered_words)

    kw_extractor = yake.KeywordExtractor(top=1, stopwords=None)

    keywords = kw_extractor.extract_keywords(test_text)

    array = []
    for kw, v in keywords:
        myList = kw.split()
        array.append(myList)

    flattened_list = [item for sublist in array for item in sublist]    
    unique_words = list(set(word.lower() for word in flattened_list))  
    answer = ' '.join(unique_words)
    return answer

