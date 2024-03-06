[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# PopularProductsElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the row | [optional]
**description** | **str** | description of the results element in SERP | [optional]
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional]
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.popular_products_element import PopularProductsElement

# TODO update the JSON string below
json = "{}"
# create an instance of PopularProductsElement from a JSON string
popular_products_element_instance = PopularProductsElement.from_json(json)
# print the JSON string representation of the object
print PopularProductsElement.to_json()

# convert the object into a dict
popular_products_element_dict = popular_products_element_instance.to_dict()
# create an instance of PopularProductsElement from a dict
popular_products_element_form_dict = popular_products_element.from_dict(popular_products_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")