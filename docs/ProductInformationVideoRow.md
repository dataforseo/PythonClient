[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ProductInformationVideoRow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview** | **str** | URL of the preview image for the related video | [optional]
**url** | **str** | URL of the image | [optional]

## Example

```python
from dataforseo_client.models.product_information_video_row import ProductInformationVideoRow

# TODO update the JSON string below
json = "{}"
# create an instance of ProductInformationVideoRow from a JSON string
product_information_video_row_instance = ProductInformationVideoRow.from_json(json)
# print the JSON string representation of the object
print ProductInformationVideoRow.to_json()

# convert the object into a dict
product_information_video_row_dict = product_information_video_row_instance.to_dict()
# create an instance of ProductInformationVideoRow from a dict
product_information_video_row_form_dict = product_information_video_row.from_dict(product_information_video_row_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")