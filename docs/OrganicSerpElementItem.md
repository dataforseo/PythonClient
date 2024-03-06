[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# OrganicSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional]
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | the XPath of the element | [optional]
**domain** | **str** | domain where a link points | [optional]
**title** | **str** | title of the result in SERP | [optional]
**url** | **str** | relevant URL in SERP | [optional]
**cache_url** | **str** | cached version of the page | [optional]
**related_search_url** | **str** | URL to a similar search URL to a new search for the same keyword(s) on related sites | [optional]
**breadcrumb** | **str** | breadcrumb in SERP | [optional]
**website_name** | **str** | name of the website in SERP | [optional]
**is_image** | **bool** | indicates whether the element contains an image | [optional]
**is_video** | **bool** | indicates whether the element contains a video | [optional]
**is_featured_snippet** | **bool** | indicates whether the element is a featured_snippet | [optional]
**is_malicious** | **bool** | indicates whether the element is marked as malicious | [optional]
**is_web_story** | **bool** | indicates whether the element is marked as Google web story | [optional]
**description** | **str** | description of the results element in SERP | [optional]
**pre_snippet** | **str** | includes additional information appended before the result description in SERP | [optional]
**extended_snippet** | **str** | includes additional information appended after the result description in SERP | [optional]
**images** | [**List[ImagesElement]**](ImagesElement.md) | images of the element | [optional]
**amp_version** | **bool** | Accelerated Mobile Pages indicates whether an item has the Accelerated Mobile Page (AMP) version | [optional]
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional]
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional]
**highlighted** | **List[Optional[str]]** | words highlighted in bold within the results description | [optional]
**links** | [**List[LinkElement]**](LinkElement.md) | sitelinks the links shown below some of Google’s search results if there are none, equals null | [optional]
**faq** | [**FaqBox**](FaqBox.md) |  | [optional]
**extended_people_also_search** | **List[Optional[str]]** | extension of the organic element extension of the organic result containing related search queries Note: extension appears in SERP upon clicking on the result and then bouncing back to search results | [optional]
**about_this_result** | [**AboutThisResultElement**](AboutThisResultElement.md) |  | [optional]
**related_result** | [**List[RelatedResult]**](RelatedResult.md) | related result from the same domain related result from the same domain appears as a part of the main result snippet; you can derive the related_result snippets as \&quot;type\&quot;: \&quot;organic\&quot; results by setting the group_organic_results parameter to false in the POST request | [optional]
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional]

## Example

```python
from dataforseo_client.models.organic_serp_element_item import OrganicSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrganicSerpElementItem from a JSON string
organic_serp_element_item_instance = OrganicSerpElementItem.from_json(json)
# print the JSON string representation of the object
print OrganicSerpElementItem.to_json()

# convert the object into a dict
organic_serp_element_item_dict = organic_serp_element_item_instance.to_dict()
# create an instance of OrganicSerpElementItem from a dict
organic_serp_element_item_form_dict = organic_serp_element_item.from_dict(organic_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")