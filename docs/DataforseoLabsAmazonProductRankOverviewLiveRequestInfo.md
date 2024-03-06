[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsAmazonProductRankOverviewLiveRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asins** | **List[str]** | product IDs to compare required field product IDs to receive ranking data for; the maximum number of ASINs you can specify in this array is 1000; you can receive the asin parameter by making a separate request to the Amazon Products endpoint | [optional]
**location_name** | **str** | full name of the location required field if don’t specify location_code you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only; example: United States | [optional]
**location_code** | **int** | location code required field if don’t specify location_name you can receive the list of available locations with their location_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only; example: 2840 | [optional]
**language_name** | **str** | full name of the language required field if don’t specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English | [optional]
**language_code** | **str** | language code required field if don’t specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_amazon_product_rank_overview_live_request_info import DataforseoLabsAmazonProductRankOverviewLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAmazonProductRankOverviewLiveRequestInfo from a JSON string
dataforseo_labs_amazon_product_rank_overview_live_request_info_instance = DataforseoLabsAmazonProductRankOverviewLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsAmazonProductRankOverviewLiveRequestInfo.to_json()

# convert the object into a dict
dataforseo_labs_amazon_product_rank_overview_live_request_info_dict = dataforseo_labs_amazon_product_rank_overview_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsAmazonProductRankOverviewLiveRequestInfo from a dict
dataforseo_labs_amazon_product_rank_overview_live_request_info_form_dict = dataforseo_labs_amazon_product_rank_overview_live_request_info.from_dict(dataforseo_labs_amazon_product_rank_overview_live_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")