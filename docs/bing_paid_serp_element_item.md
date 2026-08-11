# BingPaidSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | <em>domain of the ad element in SERP</em> |[optional]|
**title** | **StrictStr** | <em>title of the ad element in SERP</em> |[optional]|
**description** | **StrictStr** | <em>description of the ad element in SERP</em> |[optional]|
**url** | **StrictStr** | <em>relevant URL of the ad element in SERP</em> |[optional]|
**breadcrumb** | **StrictStr** | <em>breadcrumb of the ad element in SERP</em> |[optional]|
**website_name** | **StrictStr** | <em>website name in SERP</em> |[optional]|
**is_image** | **StrictBool** | <em>indicates whether the element contains an <code class='prettyprint'>image</code></em> |[optional]|
**is_video** | **StrictBool** | <em>indicates whether the element contains a <code class='prettyprint'>video</code></em> |[optional]|
**checks** | **List[Optional[StrictStr]]** |  |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | <em>images of the element</em><br>            if there are none, equals <code>null</code> |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | <em>words highlighted in bold within the results <code>description</code></em> |[optional]|
**extra** | **Dict[str, Optional[StrictStr]]** | <em>additional information about the result</em> |[optional]|
**description_rows** | **List[Optional[StrictStr]]** | <em>extended description</em><br>            if there is none, equals <code>null</code> |[optional]|
**links** | **List[Optional[AdLinkElement]]** | <em>links featured in the organic result</em> |[optional]|
**price** | **PriceInfo** | <em>price of booking a place for the specified dates of stay</em> |[optional]|
**rating** | **RatingInfo** | <em>the item's rating </em><br>            the popularity rate based on reviews and displayed in SERP |[optional]|