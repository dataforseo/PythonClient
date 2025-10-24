# AdsSearch

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**advertiser_id** | **string** | unique identifier of the advertiser account |[optional]|
**creative_id** | **string** | unique identifier of the advertisement |[optional]|
**title** | **string** | title of the element |[optional]|
**url** | **string** | search URL with refinement parameters |[optional]|
**verified** | **boolean** | verified advertiser account<br>equals true if advertiser account is verified by Google Ads |[optional]|
**format** | **string** | format of the advertisement<br>possible values: text, image, video |[optional]|
**preview_image** | **PreviewImage** | preview image of the advertisement |[optional]|
**preview_url** | **string** | url pointing to the ad preview |[optional]|
**first_shown** | **string** | date and time when the ad was shown for the first time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” |[optional]|
**last_shown** | **string** | date and time when the ad was shown the last time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” |[optional]|