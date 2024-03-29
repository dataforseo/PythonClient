[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# StocksBoxSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional]
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | the XPath of the element | [optional]
**title** | **str** | title of a given link element | [optional]
**source** | **str** | source of the element indicates the source of information included in the top_stories_element | [optional]
**snippet** | **str** | text alongside the link title | [optional]
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional]
**url** | **str** | URL | [optional]
**domain** | **str** | domain where a link points | [optional]
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional]
**table** | [**Table**](Table.md) |  | [optional]
**graph** | [**Graph**](Graph.md) |  | [optional]

## Example

```python
from dataforseo_client.models.stocks_box_serp_element_item import StocksBoxSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of StocksBoxSerpElementItem from a JSON string
stocks_box_serp_element_item_instance = StocksBoxSerpElementItem.from_json(json)
# print the JSON string representation of the object
print StocksBoxSerpElementItem.to_json()

# convert the object into a dict
stocks_box_serp_element_item_dict = stocks_box_serp_element_item_instance.to_dict()
# create an instance of StocksBoxSerpElementItem from a dict
stocks_box_serp_element_item_form_dict = stocks_box_serp_element_item.from_dict(stocks_box_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")