[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# TwitterElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**tweet** | **str** | tweet message | [optional]
**var_date** | **str** | the date when the page source of the element was published | [optional]
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**url** | **str** | URL | [optional]

## Example

```python
from dataforseo_client.models.twitter_element import TwitterElement

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterElement from a JSON string
twitter_element_instance = TwitterElement.from_json(json)
# print the JSON string representation of the object
print TwitterElement.to_json()

# convert the object into a dict
twitter_element_dict = twitter_element_instance.to_dict()
# create an instance of TwitterElement from a dict
twitter_element_form_dict = twitter_element.from_dict(twitter_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")