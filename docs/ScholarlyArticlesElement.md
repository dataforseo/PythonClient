[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ScholarlyArticlesElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the row | [optional]
**url** | **str** | URL | [optional]
**author** | **str** | author | [optional]
**description** | **str** | description of the results element in SERP | [optional]

## Example

```python
from dataforseo_client.models.scholarly_articles_element import ScholarlyArticlesElement

# TODO update the JSON string below
json = "{}"
# create an instance of ScholarlyArticlesElement from a JSON string
scholarly_articles_element_instance = ScholarlyArticlesElement.from_json(json)
# print the JSON string representation of the object
print ScholarlyArticlesElement.to_json()

# convert the object into a dict
scholarly_articles_element_dict = scholarly_articles_element_instance.to_dict()
# create an instance of ScholarlyArticlesElement from a dict
scholarly_articles_element_form_dict = scholarly_articles_element.from_dict(scholarly_articles_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")