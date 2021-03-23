# hanapin
Simple web search library

## Install

    $ pip3 install hanapin

## Usage
### Google
```python3
from hanapin import Google

# you can explicitly add the count result with the `count` argument, 
#   `search = Google(query="hello", count=1)`
# search results may not yield the exact specified count
search = Google(query="hello")
```
### Bing
```python3
from hanapin import Bing

# you can explicitly add the count result with the `count` argument, 
#   `search = Bing(query="hello", count=1)`
# search results may not yield the exact specified count
search = Bing(query="hello")
```

### DuckDuckGo
```python3
from hanapin import DuckDuckGo

# explicitly setting search results count is not applicable,
search = DuckDuckGo(query="hello")
```

### Get search results
Scraped search results are `only` the first ones the can be seen from the search engine's results.
- Search results are accesible from the class object's `.results()` function.
```python3
for i in search.results():
    print(i["title"], "::", i["link"])
```


### &copy; TheBoringDude | [MIT License](https://github.com/TheBoringDude/hanapin/blob/main/LICENSE)