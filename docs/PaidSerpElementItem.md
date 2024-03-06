[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# PaidSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional]
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | the XPath of the element | [optional]
**title** | **str** | title of the result in SERP | [optional]
**domain** | **str** | domain where a link points | [optional]
**breadcrumb** | **str** | breadcrumb in SERP | [optional]
**is_image** | **bool** | indicates whether the element contains an image | [optional]
**is_video** | **bool** | indicates whether the element contains a video | [optional]
**images** | [**List[ImagesElement]**](ImagesElement.md) | images of the element | [optional]
**url** | **str** | relevant URL in SERP | [optional]
**highlighted** | **List[Optional[str]]** | words highlighted in bold within the results description | [optional]
**extra** | **Dict[str, Optional[str]]** | additional information about the result | [optional]
**description** | **str** | description of the results element in SERP | [optional]
**description_rows** | **List[Optional[str]]** | extended description if there is none, equals null | [optional]
**links** | [**List[AdLinkElement]**](AdLinkElement.md) | sitelinks the links shown below some of Google’s search results if there are none, equals null | [optional]
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional]
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional]
**website_name** | **str** | website name in SERP | [optional]

## Example

```python
from dataforseo_client.models.paid_serp_element_item import PaidSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaidSerpElementItem from a JSON string
paid_serp_element_item_instance = PaidSerpElementItem.from_json(json)
# print the JSON string representation of the object
print PaidSerpElementItem.to_json()

# convert the object into a dict
paid_serp_element_item_dict = paid_serp_element_item_instance.to_dict()
# create an instance of PaidSerpElementItem from a dict
paid_serp_element_item_form_dict = paid_serp_element_item.from_dict(paid_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")