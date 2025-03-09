## BeautifulSoup

Beautiful Soup is a Python library for pulling data out of HTML and XML files.

### Quick start

`pip install beautifulsoup4`

```
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

```

Example
```
html = """
<div class="product">
  <h2>Product Title</h2>
  <div class="price">
    <span class="discount">12.99</span>
    <span class="full">19.99</span>
  </div>
</div>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html)
product = {
    "title": soup.find(class_="product").find("h2").text,
    "full_price": soup.find(class_="product").find(class_="full").text,
    "price": soup.select_one(".price .discount").text,
}
print(product)
{
    "title": "Product Title", 
    "full_price": "19.99", 
    "price": "12.99",
}
```

```
from bs4 import BeautifulSoup
html = "<h1>test</h1>"
# automatically select the backend (not recommended as it makes code hard to share)
soup = BeautifulSoup(html)
# lxml - most commonly used backend
soup = BeautifulSoup(html, "lxml")
# html.parser - included with python
soup = BeautifulSoup(html, "html.parser")
# html5lib - parses pages same way modern browser does
soup = BeautifulSoup(html, "html5lib")
```

- `find()` and `find_all()` methods we can easily and reliably navigate the HTML tree
- Another way to find specific elements deep inside a page's structure is to use CSS selectors through beautifulsoup's `select()` and `select_one()` functions
- `get_text()` method can be used to extract all the HTML element's text.
- `.prettify()` method restructures HTML output to be more readable by humans
- `SoupStrainer` object which allows to restrict our parsing to specific HTML elements only
- `.decompose()` is a method provided by the Beautiful Soup library for removing a tag or a portion of HTML content from a parse tree.