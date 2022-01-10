import simplesearchengine
import BOWSearchEngine
import BOWInvertedIndexEngine
import BOWInvertedIndexEngineWithCache


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)
    
    while True:
        query = input('Please input your query:')
        results = search_engine.search(query)
        print('found {} results.'.format(len(results)))
        for result in results:
            print(result)


search_engine = BOWInvertedIndexEngineWithCache.BOWInvertedIndexEngineWIthCache()
print('Start to use the {}:'.format(type(search_engine)))
main(search_engine)

