[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AmazonKeywordInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**last_updated_time** | **str** | date and time when keyword data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:    &#39;2019-11-15 12:57:46 +00:00&#39; | [optional]
**search_volume** | **int** | average monthly search volume rate represents the (approximate) number of searches for the provided keyword idea on Amazon | [optional]

## Example

```python
from dataforseo_client.models.amazon_keyword_info import AmazonKeywordInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonKeywordInfo from a JSON string
amazon_keyword_info_instance = AmazonKeywordInfo.from_json(json)
# print the JSON string representation of the object
print AmazonKeywordInfo.to_json()

# convert the object into a dict
amazon_keyword_info_dict = amazon_keyword_info_instance.to_dict()
# create an instance of AmazonKeywordInfo from a dict
amazon_keyword_info_form_dict = amazon_keyword_info.from_dict(amazon_keyword_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")