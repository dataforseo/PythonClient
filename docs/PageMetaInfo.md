[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# PageMetaInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | page title | [optional]
**charset** | **int** | code page example: 65001 | [optional]
**follow** | **bool** | indicates whether a page’s ‘meta robots’ allows crawlers to follow the links on the page if false, the page’s ‘meta robots’ tag contains “nofollow” parameter instructing crawlers not to follow the links on the page | [optional]
**generator** | **str** | meta tag generator | [optional]
**htags** | **Dict[str, Optional[List[str]]]** | HTML header tags | [optional]
**description** | **str** | content of the meta description tag | [optional]
**favicon** | **str** | favicon of the page | [optional]
**meta_keywords** | **str** | content of the keywords meta tag | [optional]
**canonical** | **str** | canonical page | [optional]
**internal_links_count** | **int** | number of internal links on the page | [optional]
**external_links_count** | **int** | number of external links on the page | [optional]
**inbound_links_count** | **int** | number of internal links pointing at the page | [optional]
**images_count** | **int** | number of images on the page | [optional]
**images_size** | **int** | total size of images on the page measured in bytes | [optional]
**scripts_count** | **int** | number of scripts on the page | [optional]
**scripts_size** | **int** | total size of scripts on the page measured in bytes | [optional]
**stylesheets_count** | **int** | number of stylesheets on the page | [optional]
**stylesheets_size** | **int** | total size of stylesheets on the page measured in bytes | [optional]
**title_length** | **int** | length of the title tag in characters | [optional]
**description_length** | **int** | length of the description tag in characters | [optional]
**render_blocking_scripts_count** | **int** | number of scripts on the page that block page rendering | [optional]
**render_blocking_stylesheets_count** | **int** | number of CSS styles on the page that block page rendering | [optional]
**cumulative_layout_shift** | **float** | Core Web Vitals metric measuring the layout stability of the page measures the sum total of all individual layout shift scores for every unexpected layout shift that occurs during the entire lifespan of the page. Learn more. | [optional]
**meta_title** | **str** | meta title of the page meta tag in the head section of an HTML document that defines the title of a page | [optional]
**content** | [**HtmlContentInfo**](HtmlContentInfo.md) |  | [optional]
**deprecated_tags** | **List[Optional[str]]** | deprecated tags on the page | [optional]
**duplicate_meta_tags** | **List[Optional[str]]** | duplicate meta tags on the page | [optional]
**spell** | [**SpellInfo**](SpellInfo.md) |  | [optional]
**social_media_tags** | **Dict[str, Optional[str]]** | object of social media tags found on the page contains social media tags and their content supported tags include but are not limited to Open Graph and Twitter card | [optional]
**broken_html** | [**OnPageResourceIssueInfo**](OnPageResourceIssueInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.page_meta_info import PageMetaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PageMetaInfo from a JSON string
page_meta_info_instance = PageMetaInfo.from_json(json)
# print the JSON string representation of the object
print PageMetaInfo.to_json()

# convert the object into a dict
page_meta_info_dict = page_meta_info_instance.to_dict()
# create an instance of PageMetaInfo from a dict
page_meta_info_form_dict = page_meta_info.from_dict(page_meta_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")