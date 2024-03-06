[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# MerchantAmazonReviewsTasksReadyResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier of the completed task unique task identifier in our system in the UUID format | [optional]
**se** | **str** | search engine specified when setting the task | [optional]
**se_type** | **str** | type of search engine can take the following values: shopping | [optional]
**date_posted** | **str** | date when the task was posted (in the UTC format) | [optional]
**tag** | **str** | user-defined task identifier | [optional]
**endpoint_advanced** | **str** | URL for collecting the results of the Amazon Reviews Advanced task | [optional]
**endpoint_html** | **str** | URL for collecting the results of the Amazon Reviews HTML task | [optional]

## Example

```python
from dataforseo_client.models.merchant_amazon_reviews_tasks_ready_result_info import MerchantAmazonReviewsTasksReadyResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAmazonReviewsTasksReadyResultInfo from a JSON string
merchant_amazon_reviews_tasks_ready_result_info_instance = MerchantAmazonReviewsTasksReadyResultInfo.from_json(json)
# print the JSON string representation of the object
print MerchantAmazonReviewsTasksReadyResultInfo.to_json()

# convert the object into a dict
merchant_amazon_reviews_tasks_ready_result_info_dict = merchant_amazon_reviews_tasks_ready_result_info_instance.to_dict()
# create an instance of MerchantAmazonReviewsTasksReadyResultInfo from a dict
merchant_amazon_reviews_tasks_ready_result_info_form_dict = merchant_amazon_reviews_tasks_ready_result_info.from_dict(merchant_amazon_reviews_tasks_ready_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")