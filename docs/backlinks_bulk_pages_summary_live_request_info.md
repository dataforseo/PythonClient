# BacklinksBulkPagesSummaryLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**targets** | **List[Optional[StrictStr]]** | domains, subdomains or webpages to get summary data for<br>required field<br>a domain or a subdomain should be specified without https:// and www.<br>a page should be specified with absolute URL (including http:// or https://)<br>you can specify up to 1000 pages, domains, or subdomains in each request.<br>note that the URLs you set in a single request cannot belong to more than 100 different domains. |[optional]|
**include_subdomains** | **StrictBool** | indicates if the subdomains of the target will be included in the search<br>optional field<br>if set to false, the subdomains will be ignored<br>default value: true |[optional]|
**rank_scale** | **StrictStr** | defines the scale used for calculating and displaying the rank, domain_from_rank, and page_from_rank values<br>optional field<br>you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale<br>possible values:<br>one_hundred — rank values are displayed on a 0–100 scale<br>one_thousand — rank values are displayed on a 0–1000 scale<br>default value: one_thousand<br>learn more about how this parameter works and how ranking metrics are calculated in this Help Center article |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|