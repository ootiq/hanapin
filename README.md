# hanapin
Simple web search library

## Install

    $ pip3 install hanapin

## Usage
### Google
```python3
from hanapin import Google

search = Google(query="hello")
```
### Bing
```python3
from hanapin import Bing

search = Bing(query="hello")
```

### DuckDuckGo
```
from hanapin import DuckDuckGo

search = DuckDuckGo(query="hello")
```

### Get search results
Scraped search results are `only` the first ones the can be seen from the search engine's results.
```python3
for i in search.results():
    print(i["title"], "::", i["link"])
```


### &copy; TheBoringDude | [MIT License](https://github.com/TheBoringDude/hanapin/blob/main/LICENSE)