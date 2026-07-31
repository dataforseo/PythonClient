# AdsSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**advertiser_id** | **StrictStr** | <em>unique identifier of the advertiser account</em> |[optional]|
**creative_id** | **StrictStr** | <em>unique identifier of the advertisement</em> |[optional]|
**title** | **StrictStr** | <em>title of the element</em> |[optional]|
**url** | **StrictStr** | <em>search URL with refinement parameters</em> |[optional]|
**verified** | **StrictBool** | <em>verified advertiser account</em><br>equals <code>true</code> if advertiser account is verified by Google Ads |[optional]|
**format** | **StrictStr** | <em>format of the advertisement</em><br>possible values: <code>text</code>, <code>image</code>, <code>video</code> |[optional]|
**preview_image** | **PreviewImage** | <em>preview image of the advertisement</em> |[optional]|
**preview_url** | **StrictStr** | <em>url pointing to the ad preview</em> |[optional]|
**first_shown** | **StrictStr** | <em>date and time when the ad was shown for the first time</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” |[optional]|
**last_shown** | **StrictStr** | <em>date and time when the ad was shown the last time</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” |[optional]|