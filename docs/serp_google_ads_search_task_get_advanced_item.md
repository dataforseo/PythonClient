# SerpGoogleAdsSearchTaskGetAdvancedItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**advertiser_id** | **StrictStr** | unique identifier of the advertiser account |[optional]|
**creative_id** | **StrictStr** | unique identifier of the advertisement |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**url** | **StrictStr** | search URL with refinement parameters |[optional]|
**verified** | **StrictBool** | verified advertiser account<br>equals true if advertiser account is verified by Google Ads |[optional]|
**format** | **StrictStr** | format of the advertisement<br>possible values: text, image, video |[optional]|
**preview_image** | **PreviewImage** | preview image of the advertisement |[optional]|
**preview_url** | **StrictStr** | url pointing to the ad preview |[optional]|
**first_shown** | **StrictStr** | date and time when the ad was shown for the first time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” |[optional]|
**last_shown** | **StrictStr** | date and time when the ad was shown the last time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” |[optional]|