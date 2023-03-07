import csv
from fuzzywuzzy import fuzz, process


data = [] 
allData = []

def get_results(query, max_results, adv):
    starts_withs = []
    contains = []
    results = []
    query = query.lower()
    for id, dat in enumerate(data):

        if (len(starts_withs) == int(max_results)):
            break

        if dat.lower().startswith(query):
            starts_withs.append({'id': id,
                                 'data': dat})

        elif query in dat.lower():
            contains.append({'id': id,
                            'data': dat})
            
    results = (starts_withs + contains)[0:int(max_results)]

    if(adv=='true'):
        
        fuzzy_result = process.extract(query, data, scorer=fuzz.token_sort_ratio, limit=10)
        fuzzys = []
        for r in fuzzy_result:
            index = data.index(r[0])
            fuzzys.append({'id': index, 'data': r[0]})


        return get_uniques(starts_withs + contains + fuzzys)[0:int(max_results)]

    else:
        return results

def get_uniques(list):

    seen_ids = []

    unique_objects = []

    for object in list:
        if object['id'] not in seen_ids:
            unique_objects.append(object)
            seen_ids.append(object['id'])

    return unique_objects


if __name__ == '__main__':
    print()
