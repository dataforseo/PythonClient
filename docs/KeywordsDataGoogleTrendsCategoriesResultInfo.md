[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# KeywordsDataGoogleTrendsCategoriesResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_code** | **int** | unique google trends category identifier | [optional]
**category_name** | **str** | name of the google trends category | [optional]
**category_code_parent** | **int** | the code of the superordinate category example: \&quot;category_code\&quot;: 1100, \&quot;category_name\&quot;: \&quot;Superhero Films\&quot;, \&quot;category_code_parent\&quot;: 1097 where category_code_parent corresponds to: \&quot;category_code\&quot;: 1097, \&quot;category_name\&quot;: \&quot;Action &amp; Adventure Films\&quot; | [optional]

## Example

```python
from dataforseo_client.models.keywords_data_google_trends_categories_result_info import KeywordsDataGoogleTrendsCategoriesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataGoogleTrendsCategoriesResultInfo from a JSON string
keywords_data_google_trends_categories_result_info_instance = KeywordsDataGoogleTrendsCategoriesResultInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataGoogleTrendsCategoriesResultInfo.to_json()

# convert the object into a dict
keywords_data_google_trends_categories_result_info_dict = keywords_data_google_trends_categories_result_info_instance.to_dict()
# create an instance of KeywordsDataGoogleTrendsCategoriesResultInfo from a dict
keywords_data_google_trends_categories_result_info_form_dict = keywords_data_google_trends_categories_result_info.from_dict(keywords_data_google_trends_categories_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")