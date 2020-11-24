import requests, json

class SearchFood:
    def byName(name):
        try:
            r = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s='+str(name))

            return json.loads(r.content)
        except:
            raise Exception('Not a string!')

    def byArea(area):
        try:
            r = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?a='+str(area))

            return json.loads(r.content)
        except:
            raise Exception('Not a string!')

    def byCategory(cat):
        try:
            r = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c='+str(cat))

            return json.loads(r.content)
        except:
            raise Exception('Not a string!')

    def categories():
        r = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php')

        return json.loads(r.content)

    def random():
        r = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')

        return json.loads(r.content)

# print(SearchFood.random())