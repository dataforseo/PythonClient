# GoogleFinanceNewsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the news article | [optional] 
**url** | **str** | URL to the page of the market index on Google Finance | [optional] 
**source** | **str** | name of the news source name of the website where the news article is published | [optional] 
**image_url** | **str** | featured image URL URL of the news article’s featured image | [optional] 
**timestamp** | **str** | date and time of the value readout in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2025-02-10 09:40:00 +00:00 | [optional] 
**quotes** | [**List[GoogleFinanceAssetPairElement]**](GoogleFinanceAssetPairElement.md) | market indexes quoted in the news article information about market indexes quoted in the google_finance_news_element | [optional] 

## Example

```python
from dataforseo_client.models.google_finance_news_element import GoogleFinanceNewsElement

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFinanceNewsElement from a JSON string
google_finance_news_element_instance = GoogleFinanceNewsElement.from_json(json)
# print the JSON string representation of the object
print(GoogleFinanceNewsElement.to_json())

# convert the object into a dict
google_finance_news_element_dict = google_finance_news_element_instance.to_dict()
# create an instance of GoogleFinanceNewsElement from a dict
google_finance_news_element_from_dict = GoogleFinanceNewsElement.from_dict(google_finance_news_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


