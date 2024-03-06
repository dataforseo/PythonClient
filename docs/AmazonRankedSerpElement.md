[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AmazonRankedSerpElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**serp_item** | [**BaseAmazonSerpElementItem**](BaseAmazonSerpElementItem.md) |  | [optional]
**check_url** | **str** | direct URL to Amazon results you can use it to make sure that we provided accurate results | [optional]
**serp_item_types** | **List[Optional[str]]** | direct URL to Amazon results contains types of all search results (items) found in the returned SERP; possible item types: amazon_serp, amazon_paid, editorial_recommendations, top_rated_from_our_brands, related_searches | [optional]
**se_results_count** | **int** | total number of results in Amazon SERP | [optional]
**last_updated_time** | **str** | date and time when SERP data was last updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**previous_updated_time** | **str** | previous to the most recent update of SERP data in the ISO 8601 format: “YYYY-MM-DDThh:mm:ss.sssssssZ” example: 2020-09-12T00:07:43.0733218Z | [optional]

## Example

```python
from dataforseo_client.models.amazon_ranked_serp_element import AmazonRankedSerpElement

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonRankedSerpElement from a JSON string
amazon_ranked_serp_element_instance = AmazonRankedSerpElement.from_json(json)
# print the JSON string representation of the object
print AmazonRankedSerpElement.to_json()

# convert the object into a dict
amazon_ranked_serp_element_dict = amazon_ranked_serp_element_instance.to_dict()
# create an instance of AmazonRankedSerpElement from a dict
amazon_ranked_serp_element_form_dict = amazon_ranked_serp_element.from_dict(amazon_ranked_serp_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")