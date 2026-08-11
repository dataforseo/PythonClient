# SerpScreenshotRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**task_id** | **StrictStr** | <em>task identifier</em><br><strong>required field</strong><br>unique identifier of the associated task in the <a href='https://en.wikipedia.org/wiki/Universally_unique_identifier'>UUID</a> format<br>you will be able to use it within <strong>7 days</strong> to request the results of the task at any time |[optional]|
**browser_preset** | **StrictStr** | <em>browser resolution preset</em><br>optional field<br>browser preset associated with a certain device type<br>can take the following values: <code>desktop</code>, <code>tablet</code>, <code>mobile</code> <br><strong>Note:</strong> by default, browser preset corresponds to the device type specified in the POST request |[optional]|
**browser_screen_width** | **StrictInt** | <em>width of the browser resolution</em><br>optional field<br>can be specified in the following range: <code>240-9999</code><br>default value for <code>desktop</code>: 1920<br>default value for <code>mobile</code>: 390<br>default value for <code>table</code>: 1024 |[optional]|
**browser_screen_height** | **StrictInt** | <em>height of the browser resolution</em><br>optional field<br>can be specified in the following range: <code>240-9999</code><br>default value for <code>desktop</code>: 1080<br>default value for <code>mobile</code>: 844<br>default value for <code>table</code>: 1366 |[optional]|
**browser_screen_scale_factor** | **StrictFloat** | <em>browser scale factor</em><br>optional field<br>can be specified in the following range: <code>0.5-3</code><br>default value for <code>desktop</code>: 1<br>default value for <code>mobile</code>: 3<br>default value for <code>table</code>: 2 |[optional]|
**page** | **StrictInt** | <em>number of SERP pages</em><br>optional field<br>if <code>depth</code> in the corresponding Task POST request exceeds 10 results (or 1 SERP page), specify the number of SERP pages to screenshot;<br>default value: <code>1</code> |[optional]|