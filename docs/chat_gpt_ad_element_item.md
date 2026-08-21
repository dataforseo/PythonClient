# ChatGptAdElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**is_rendered** | **StrictBool** | <em>  indicates whether the ad is displayed to the user</em><br>if `true`, the ad is present in the response and shown on the page<br>if `false`, the ad is present in the response but not displayed to the user |[optional]|
**title** | **StrictStr** | <em>name of the brand</em> |[optional]|
**snippet** | **StrictStr** | <em>source description</em> |[optional]|
**url** | **StrictStr** | <em>URL</em> |[optional]|
**domain** | **StrictStr** | <em>domain</em> |[optional]|
**image_url** | **StrictStr** | <em>URL of the image displayed in the ad</em> |[optional]|
**advertiser** | **ChatGptAdAdvertiser** | <em>information about the advertiser associated with the ad</em> |[optional]|