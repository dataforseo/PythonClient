# BacklinksReferringDomainsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**target** | **StrictStr** | target in a POST array |[optional]|
**total_count** | **StrictFloat** | total number of relevant items in the database<br>total number of main domains referring to your target;<br>example.com and blog.example.com are counted as one referring domain |[optional]|
**items_count** | **StrictFloat** | number of items in the items array |[optional]|
**items** | **List[Optional[BacklinksReferringDomainsLiveItem]]** | items array |[optional]|