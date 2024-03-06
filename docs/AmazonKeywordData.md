[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AmazonKeywordData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**keyword** | **str** | related keyword | [optional]
**location_code** | **int** | location code in a POST array | [optional]
**language_code** | **str** | language code in a POST array | [optional]
**keyword_info** | [**AmazonKeywordInfo**](AmazonKeywordInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.amazon_keyword_data import AmazonKeywordData

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonKeywordData from a JSON string
amazon_keyword_data_instance = AmazonKeywordData.from_json(json)
# print the JSON string representation of the object
print AmazonKeywordData.to_json()

# convert the object into a dict
amazon_keyword_data_dict = amazon_keyword_data_instance.to_dict()
# create an instance of AmazonKeywordData from a dict
amazon_keyword_data_form_dict = amazon_keyword_data.from_dict(amazon_keyword_data_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")