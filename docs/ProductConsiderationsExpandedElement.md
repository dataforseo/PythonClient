[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ProductConsiderationsExpandedElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of a given link element | [optional]
**featured_title** | **str** | the title of the featured snippets source page | [optional]
**breadcrumb** | **str** | breadcrumb of the Ad element in SERP | [optional]
**snippet** | **str** | text alongside the link title | [optional]
**domain** | **str** | website domain | [optional]
**url** | **str** | URL | [optional]
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**related_searches** | **List[Optional[str]]** | search queries related to the elment | [optional]
**about_this_result** | [**AboutThisResultElement**](AboutThisResultElement.md) |  | [optional]

## Example

```python
from dataforseo_client.models.product_considerations_expanded_element import ProductConsiderationsExpandedElement

# TODO update the JSON string below
json = "{}"
# create an instance of ProductConsiderationsExpandedElement from a JSON string
product_considerations_expanded_element_instance = ProductConsiderationsExpandedElement.from_json(json)
# print the JSON string representation of the object
print ProductConsiderationsExpandedElement.to_json()

# convert the object into a dict
product_considerations_expanded_element_dict = product_considerations_expanded_element_instance.to_dict()
# create an instance of ProductConsiderationsExpandedElement from a dict
product_considerations_expanded_element_form_dict = product_considerations_expanded_element.from_dict(product_considerations_expanded_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")