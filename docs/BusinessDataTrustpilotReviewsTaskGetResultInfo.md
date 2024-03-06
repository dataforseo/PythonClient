[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BusinessDataTrustpilotReviewsTaskGetResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | domain of the business entity | [optional]
**type** | **str** | type of element | [optional]
**se_domain** | **str** | search engine domain in a POST array | [optional]
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional]
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**title** | **str** | title of the ‘reviews’ element on Trustpilot the name of the business entity for which the reviews are collected | [optional]
**location** | **str** | location of the business entity as specified on Trustpilot address of the business entity for which the reviews are collected | [optional]
**reviews_count** | **int** | the total number of reviews | [optional]
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional]
**items_count** | **int** | the number of items in the results array you can get more results by using the depth parameter when setting a task | [optional]
**items** | [**List[BaseBusinessDataSerpElementItem]**](BaseBusinessDataSerpElementItem.md) | found reviews you can get more results by using the depth parameter when setting a task | [optional]

## Example

```python
from dataforseo_client.models.business_data_trustpilot_reviews_task_get_result_info import BusinessDataTrustpilotReviewsTaskGetResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataTrustpilotReviewsTaskGetResultInfo from a JSON string
business_data_trustpilot_reviews_task_get_result_info_instance = BusinessDataTrustpilotReviewsTaskGetResultInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataTrustpilotReviewsTaskGetResultInfo.to_json()

# convert the object into a dict
business_data_trustpilot_reviews_task_get_result_info_dict = business_data_trustpilot_reviews_task_get_result_info_instance.to_dict()
# create an instance of BusinessDataTrustpilotReviewsTaskGetResultInfo from a dict
business_data_trustpilot_reviews_task_get_result_info_form_dict = business_data_trustpilot_reviews_task_get_result_info.from_dict(business_data_trustpilot_reviews_task_get_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")