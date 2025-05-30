# HotelLocationInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**neighborhood** | **StrictStr** | name of the neighborhood where the hotel is located |[optional]|
**neighborhood_description** | **StrictStr** | description of the neighborhood where the hotel is located |[optional]|
**maps_url** | **StrictStr** | url to the location of the hotel in google maps |[optional]|
**overall_score** | **StrictFloat** | overall score of the hotel location<br>indicates the overall score of the hotel’s location in the range from 1 to 5;<br>calculated based on data from the hotel’s proximity to nearby things to do and restaurants, transportation, and airports;<br>note that the criteria are not weighted equally in the overall score |[optional]|
**score_by_categories** | **Dict[str, Optional[StrictFloat]]** | category scores of the hotel location<br>the scores of the hotel’s location tied to the categories that indicate the proximity to nearby things to do, restaurants, transportation, and airports; |[optional]|
**latitude** | **StrictFloat** | hotel latitude<br>latitude coordinates of the hotel’s location<br>example:<br>39.4806397 |[optional]|
**longitude** | **StrictFloat** | hotel longitude<br>latitude coordinates of the hotel’s location<br>example:<br>-106.0512973 |[optional]|
**location_chain** | **List[Optional[LocationChain]]** | elements of the location chain<br>additional parameters of each element of the location chain |[optional]|