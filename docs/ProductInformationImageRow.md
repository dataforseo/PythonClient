[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ProductInformationImageRow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt** | **str** | alternative text of the related product image | [optional]
**url** | **str** | URL of the image | [optional]

## Example

```python
from dataforseo_client.models.product_information_image_row import ProductInformationImageRow

# TODO update the JSON string below
json = "{}"
# create an instance of ProductInformationImageRow from a JSON string
product_information_image_row_instance = ProductInformationImageRow.from_json(json)
# print the JSON string representation of the object
print ProductInformationImageRow.to_json()

# convert the object into a dict
product_information_image_row_dict = product_information_image_row_instance.to_dict()
# create an instance of ProductInformationImageRow from a dict
product_information_image_row_form_dict = product_information_image_row.from_dict(product_information_image_row_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")