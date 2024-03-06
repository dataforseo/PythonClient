[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# LocalPackSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional]
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | the XPath of the element | [optional]
**title** | **str** | title of a given link element | [optional]
**description** | **str** | description | [optional]
**domain** | **str** | domain where a link points | [optional]
**phone** | **str** | phone number | [optional]
**url** | **str** | URL | [optional]
**is_paid** | **bool** | indicates whether the element is an ad | [optional]
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional]
**cid** | **str** | google-defined client id | [optional]
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional]

## Example

```python
from dataforseo_client.models.local_pack_serp_element_item import LocalPackSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of LocalPackSerpElementItem from a JSON string
local_pack_serp_element_item_instance = LocalPackSerpElementItem.from_json(json)
# print the JSON string representation of the object
print LocalPackSerpElementItem.to_json()

# convert the object into a dict
local_pack_serp_element_item_dict = local_pack_serp_element_item_instance.to_dict()
# create an instance of LocalPackSerpElementItem from a dict
local_pack_serp_element_item_form_dict = local_pack_serp_element_item.from_dict(local_pack_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")