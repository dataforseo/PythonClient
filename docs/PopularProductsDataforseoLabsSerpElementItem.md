[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# PopularProductsDataforseoLabsSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional]
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | the XPath of the element | [optional]
**items** | [**List[PopularProductsElement]**](PopularProductsElement.md) | elements of search results found in SERP | [optional]

## Example

```python
from dataforseo_client.models.popular_products_dataforseo_labs_serp_element_item import PopularProductsDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of PopularProductsDataforseoLabsSerpElementItem from a JSON string
popular_products_dataforseo_labs_serp_element_item_instance = PopularProductsDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print PopularProductsDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
popular_products_dataforseo_labs_serp_element_item_dict = popular_products_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of PopularProductsDataforseoLabsSerpElementItem from a dict
popular_products_dataforseo_labs_serp_element_item_form_dict = popular_products_dataforseo_labs_serp_element_item.from_dict(popular_products_dataforseo_labs_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")