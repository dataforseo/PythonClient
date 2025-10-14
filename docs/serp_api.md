# SerpApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**serpIdList**](SerpApi.md#serpIdList) | **POST**  /v3/serp/id_list  |
[**serpErrors**](SerpApi.md#serpErrors) | **POST**  /v3/serp/errors  |
[**screenshot**](SerpApi.md#screenshot) | **POST**  /v3/serp/screenshot  |
[**aiSummary**](SerpApi.md#aiSummary) | **POST**  /v3/serp/ai_summary  |
[**serpGoogleLocations**](SerpApi.md#serpGoogleLocations) | **GET**  /v3/serp/google/locations  |
[**serpGoogleLocationsCountry**](SerpApi.md#serpGoogleLocationsCountry) | **GET**  /v3/serp/google/locations/{country}  |
[**serpGoogleLanguages**](SerpApi.md#serpGoogleLanguages) | **GET**  /v3/serp/google/languages  |
[**googleOrganicTaskPost**](SerpApi.md#googleOrganicTaskPost) | **POST**  /v3/serp/google/organic/task_post  |
[**googleOrganicTasksReady**](SerpApi.md#googleOrganicTasksReady) | **GET**  /v3/serp/google/organic/tasks_ready  |
[**tasksReady**](SerpApi.md#tasksReady) | **GET**  /v3/serp/tasks_ready  |
[**googleOrganicTasksFixed**](SerpApi.md#googleOrganicTasksFixed) | **GET**  /v3/serp/google/organic/tasks_fixed  |
[**googleOrganicTaskGetRegular**](SerpApi.md#googleOrganicTaskGetRegular) | **GET**  /v3/serp/google/organic/task_get/regular/{id}  |
[**googleOrganicTaskGetAdvanced**](SerpApi.md#googleOrganicTaskGetAdvanced) | **GET**  /v3/serp/google/organic/task_get/advanced/{id}  |
[**googleOrganicTaskGetHtml**](SerpApi.md#googleOrganicTaskGetHtml) | **GET**  /v3/serp/google/organic/task_get/html/{id}  |
[**googleOrganicLiveRegular**](SerpApi.md#googleOrganicLiveRegular) | **POST**  /v3/serp/google/organic/live/regular  |
[**googleOrganicLiveAdvanced**](SerpApi.md#googleOrganicLiveAdvanced) | **POST**  /v3/serp/google/organic/live/advanced  |
[**googleOrganicLiveHtml**](SerpApi.md#googleOrganicLiveHtml) | **POST**  /v3/serp/google/organic/live/html  |
[**serpGoogleAiModeLanguages**](SerpApi.md#serpGoogleAiModeLanguages) | **GET**  /v3/serp/google/ai_mode/languages  |
[**googleAiModeTaskPost**](SerpApi.md#googleAiModeTaskPost) | **POST**  /v3/serp/google/ai_mode/task_post  |
[**googleAiModeTasksReady**](SerpApi.md#googleAiModeTasksReady) | **GET**  /v3/serp/google/ai_mode/tasks_ready  |
[**googleAiModeTasksFixed**](SerpApi.md#googleAiModeTasksFixed) | **GET**  /v3/serp/google/ai_mode/tasks_fixed  |
[**googleAiModeTaskGetAdvanced**](SerpApi.md#googleAiModeTaskGetAdvanced) | **GET**  /v3/serp/google/ai_mode/task_get/advanced/{id}  |
[**googleAiModeTaskGetHtml**](SerpApi.md#googleAiModeTaskGetHtml) | **GET**  /v3/serp/google/ai_mode/task_get/html/{id}  |
[**googleAiModeLiveAdvanced**](SerpApi.md#googleAiModeLiveAdvanced) | **POST**  /v3/serp/google/ai_mode/live/advanced  |
[**googleAiModeLiveHtml**](SerpApi.md#googleAiModeLiveHtml) | **POST**  /v3/serp/google/ai_mode/live/html  |
[**googleMapsTaskPost**](SerpApi.md#googleMapsTaskPost) | **POST**  /v3/serp/google/maps/task_post  |
[**googleMapsTasksReady**](SerpApi.md#googleMapsTasksReady) | **GET**  /v3/serp/google/maps/tasks_ready  |
[**googleMapsTasksFixed**](SerpApi.md#googleMapsTasksFixed) | **GET**  /v3/serp/google/maps/tasks_fixed  |
[**googleMapsTaskGetAdvanced**](SerpApi.md#googleMapsTaskGetAdvanced) | **GET**  /v3/serp/google/maps/task_get/advanced/{id}  |
[**googleMapsLiveAdvanced**](SerpApi.md#googleMapsLiveAdvanced) | **POST**  /v3/serp/google/maps/live/advanced  |
[**googleLocalFinderTaskPost**](SerpApi.md#googleLocalFinderTaskPost) | **POST**  /v3/serp/google/local_finder/task_post  |
[**googleLocalFinderTasksReady**](SerpApi.md#googleLocalFinderTasksReady) | **GET**  /v3/serp/google/local_finder/tasks_ready  |
[**googleLocalFinderTasksFixed**](SerpApi.md#googleLocalFinderTasksFixed) | **GET**  /v3/serp/google/local_finder/tasks_fixed  |
[**googleLocalFinderTaskGetAdvanced**](SerpApi.md#googleLocalFinderTaskGetAdvanced) | **GET**  /v3/serp/google/local_finder/task_get/advanced/{id}  |
[**googleLocalFinderTaskGetHtml**](SerpApi.md#googleLocalFinderTaskGetHtml) | **GET**  /v3/serp/google/local_finder/task_get/html/{id}  |
[**googleLocalFinderLiveAdvanced**](SerpApi.md#googleLocalFinderLiveAdvanced) | **POST**  /v3/serp/google/local_finder/live/advanced  |
[**googleLocalFinderLiveHtml**](SerpApi.md#googleLocalFinderLiveHtml) | **POST**  /v3/serp/google/local_finder/live/html  |
[**googleNewsTaskPost**](SerpApi.md#googleNewsTaskPost) | **POST**  /v3/serp/google/news/task_post  |
[**googleNewsTasksReady**](SerpApi.md#googleNewsTasksReady) | **GET**  /v3/serp/google/news/tasks_ready  |
[**googleNewsTasksFixed**](SerpApi.md#googleNewsTasksFixed) | **GET**  /v3/serp/google/news/tasks_fixed  |
[**googleNewsTaskGetAdvanced**](SerpApi.md#googleNewsTaskGetAdvanced) | **GET**  /v3/serp/google/news/task_get/advanced/{id}  |
[**googleNewsTaskGetHtml**](SerpApi.md#googleNewsTaskGetHtml) | **GET**  /v3/serp/google/news/task_get/html/{id}  |
[**googleNewsLiveAdvanced**](SerpApi.md#googleNewsLiveAdvanced) | **POST**  /v3/serp/google/news/live/advanced  |
[**googleNewsLiveHtml**](SerpApi.md#googleNewsLiveHtml) | **POST**  /v3/serp/google/news/live/html  |
[**googleEventsTaskPost**](SerpApi.md#googleEventsTaskPost) | **POST**  /v3/serp/google/events/task_post  |
[**googleEventsTasksReady**](SerpApi.md#googleEventsTasksReady) | **GET**  /v3/serp/google/events/tasks_ready  |
[**googleEventsTasksFixed**](SerpApi.md#googleEventsTasksFixed) | **GET**  /v3/serp/google/events/tasks_fixed  |
[**googleEventsTaskGetAdvanced**](SerpApi.md#googleEventsTaskGetAdvanced) | **GET**  /v3/serp/google/events/task_get/advanced/{id}  |
[**googleEventsLiveAdvanced**](SerpApi.md#googleEventsLiveAdvanced) | **POST**  /v3/serp/google/events/live/advanced  |
[**googleImagesTaskPost**](SerpApi.md#googleImagesTaskPost) | **POST**  /v3/serp/google/images/task_post  |
[**googleImagesTasksReady**](SerpApi.md#googleImagesTasksReady) | **GET**  /v3/serp/google/images/tasks_ready  |
[**googleImagesTasksFixed**](SerpApi.md#googleImagesTasksFixed) | **GET**  /v3/serp/google/images/tasks_fixed  |
[**googleImagesTaskGetAdvanced**](SerpApi.md#googleImagesTaskGetAdvanced) | **GET**  /v3/serp/google/images/task_get/advanced/{id}  |
[**googleImagesTaskGetHtml**](SerpApi.md#googleImagesTaskGetHtml) | **GET**  /v3/serp/google/images/task_get/html/{id}  |
[**googleImagesLiveAdvanced**](SerpApi.md#googleImagesLiveAdvanced) | **POST**  /v3/serp/google/images/live/advanced  |
[**googleImagesLiveHtml**](SerpApi.md#googleImagesLiveHtml) | **POST**  /v3/serp/google/images/live/html  |
[**googleSearchByImageTaskPost**](SerpApi.md#googleSearchByImageTaskPost) | **POST**  /v3/serp/google/search_by_image/task_post  |
[**googleSearchByImageTasksReady**](SerpApi.md#googleSearchByImageTasksReady) | **GET**  /v3/serp/google/search_by_image/tasks_ready  |
[**googleSearchByImageTasksFixed**](SerpApi.md#googleSearchByImageTasksFixed) | **GET**  /v3/serp/google/search_by_image/tasks_fixed  |
[**googleSearchByImageTaskGetAdvanced**](SerpApi.md#googleSearchByImageTaskGetAdvanced) | **GET**  /v3/serp/google/search_by_image/task_get/advanced/{id}  |
[**googleJobsTaskPost**](SerpApi.md#googleJobsTaskPost) | **POST**  /v3/serp/google/jobs/task_post  |
[**googleJobsTasksReady**](SerpApi.md#googleJobsTasksReady) | **GET**  /v3/serp/google/jobs/tasks_ready  |
[**googleJobsTasksFixed**](SerpApi.md#googleJobsTasksFixed) | **GET**  /v3/serp/google/jobs/tasks_fixed  |
[**googleJobsTaskGetAdvanced**](SerpApi.md#googleJobsTaskGetAdvanced) | **GET**  /v3/serp/google/jobs/task_get/advanced/{id}  |
[**googleJobsTaskGetHtml**](SerpApi.md#googleJobsTaskGetHtml) | **GET**  /v3/serp/google/jobs/task_get/html/{id}  |
[**googleAutocompleteTaskPost**](SerpApi.md#googleAutocompleteTaskPost) | **POST**  /v3/serp/google/autocomplete/task_post  |
[**googleAutocompleteTasksReady**](SerpApi.md#googleAutocompleteTasksReady) | **GET**  /v3/serp/google/autocomplete/tasks_ready  |
[**googleAutocompleteTasksFixed**](SerpApi.md#googleAutocompleteTasksFixed) | **GET**  /v3/serp/google/autocomplete/tasks_fixed  |
[**googleAutocompleteTaskGetAdvanced**](SerpApi.md#googleAutocompleteTaskGetAdvanced) | **GET**  /v3/serp/google/autocomplete/task_get/advanced/{id}  |
[**googleAutocompleteLiveAdvanced**](SerpApi.md#googleAutocompleteLiveAdvanced) | **POST**  /v3/serp/google/autocomplete/live/advanced  |
[**googleDatasetSearchTaskPost**](SerpApi.md#googleDatasetSearchTaskPost) | **POST**  /v3/serp/google/dataset_search/task_post  |
[**googleDatasetSearchTasksReady**](SerpApi.md#googleDatasetSearchTasksReady) | **GET**  /v3/serp/google/dataset_search/tasks_ready  |
[**googleDatasetSearchTasksFixed**](SerpApi.md#googleDatasetSearchTasksFixed) | **GET**  /v3/serp/google/dataset_search/tasks_fixed  |
[**googleDatasetSearchTaskGetAdvanced**](SerpApi.md#googleDatasetSearchTaskGetAdvanced) | **GET**  /v3/serp/google/dataset_search/task_get/advanced/{id}  |
[**googleDatasetSearchLiveAdvanced**](SerpApi.md#googleDatasetSearchLiveAdvanced) | **POST**  /v3/serp/google/dataset_search/live/advanced  |
[**googleDatasetInfoTaskPost**](SerpApi.md#googleDatasetInfoTaskPost) | **POST**  /v3/serp/google/dataset_info/task_post  |
[**googleDatasetInfoTasksReady**](SerpApi.md#googleDatasetInfoTasksReady) | **GET**  /v3/serp/google/dataset_info/tasks_ready  |
[**googleDatasetInfoTasksFixed**](SerpApi.md#googleDatasetInfoTasksFixed) | **GET**  /v3/serp/google/dataset_info/tasks_fixed  |
[**googleDatasetInfoTaskGetAdvanced**](SerpApi.md#googleDatasetInfoTaskGetAdvanced) | **GET**  /v3/serp/google/dataset_info/task_get/advanced/{id}  |
[**googleDatasetInfoLiveAdvanced**](SerpApi.md#googleDatasetInfoLiveAdvanced) | **POST**  /v3/serp/google/dataset_info/live/advanced  |
[**serpGoogleAdsAdvertisersLocations**](SerpApi.md#serpGoogleAdsAdvertisersLocations) | **GET**  /v3/serp/google/ads_advertisers/locations  |
[**googleAdsAdvertisersTaskPost**](SerpApi.md#googleAdsAdvertisersTaskPost) | **POST**  /v3/serp/google/ads_advertisers/task_post  |
[**googleAdsAdvertisersTasksReady**](SerpApi.md#googleAdsAdvertisersTasksReady) | **GET**  /v3/serp/google/ads_advertisers/tasks_ready  |
[**googleAdsAdvertisersTaskGetAdvanced**](SerpApi.md#googleAdsAdvertisersTaskGetAdvanced) | **GET**  /v3/serp/google/ads_advertisers/task_get/advanced/{id}  |
[**serpGoogleAdsSearchLocations**](SerpApi.md#serpGoogleAdsSearchLocations) | **GET**  /v3/serp/google/ads_search/locations  |
[**googleAdsSearchTaskPost**](SerpApi.md#googleAdsSearchTaskPost) | **POST**  /v3/serp/google/ads_search/task_post  |
[**googleAdsSearchTasksReady**](SerpApi.md#googleAdsSearchTasksReady) | **GET**  /v3/serp/google/ads_search/tasks_ready  |
[**googleAdsSearchTaskGetAdvanced**](SerpApi.md#googleAdsSearchTaskGetAdvanced) | **GET**  /v3/serp/google/ads_search/task_get/advanced/{id}  |
[**serpBingLocations**](SerpApi.md#serpBingLocations) | **GET**  /v3/serp/bing/locations  |
[**serpBingLocationsCountry**](SerpApi.md#serpBingLocationsCountry) | **GET**  /v3/serp/bing/locations/{country}  |
[**serpBingLanguages**](SerpApi.md#serpBingLanguages) | **GET**  /v3/serp/bing/languages  |
[**bingOrganicTaskPost**](SerpApi.md#bingOrganicTaskPost) | **POST**  /v3/serp/bing/organic/task_post  |
[**bingOrganicTasksReady**](SerpApi.md#bingOrganicTasksReady) | **GET**  /v3/serp/bing/organic/tasks_ready  |
[**bingOrganicTasksFixed**](SerpApi.md#bingOrganicTasksFixed) | **GET**  /v3/serp/bing/organic/tasks_fixed  |
[**bingOrganicTaskGetRegular**](SerpApi.md#bingOrganicTaskGetRegular) | **GET**  /v3/serp/bing/organic/task_get/regular/{id}  |
[**bingOrganicTaskGetAdvanced**](SerpApi.md#bingOrganicTaskGetAdvanced) | **GET**  /v3/serp/bing/organic/task_get/advanced/{id}  |
[**bingOrganicTaskGetHtml**](SerpApi.md#bingOrganicTaskGetHtml) | **GET**  /v3/serp/bing/organic/task_get/html/{id}  |
[**bingOrganicLiveRegular**](SerpApi.md#bingOrganicLiveRegular) | **POST**  /v3/serp/bing/organic/live/regular  |
[**bingOrganicLiveAdvanced**](SerpApi.md#bingOrganicLiveAdvanced) | **POST**  /v3/serp/bing/organic/live/advanced  |
[**bingOrganicLiveHtml**](SerpApi.md#bingOrganicLiveHtml) | **POST**  /v3/serp/bing/organic/live/html  |
[**bingLocalPackTaskPost**](SerpApi.md#bingLocalPackTaskPost) | **POST**  /v3/serp/bing/local_pack/task_post  |
[**bingLocalPackTasksReady**](SerpApi.md#bingLocalPackTasksReady) | **GET**  /v3/serp/bing/local_pack/tasks_ready  |
[**bingLocalPackTasksFixed**](SerpApi.md#bingLocalPackTasksFixed) | **GET**  /v3/serp/bing/local_pack/tasks_fixed  |
[**bingLocalPackTaskGetRegular**](SerpApi.md#bingLocalPackTaskGetRegular) | **GET**  /v3/serp/bing/local_pack/task_get/regular/{id}  |
[**bingLocalPackTaskGetHtml**](SerpApi.md#bingLocalPackTaskGetHtml) | **GET**  /v3/serp/bing/local_pack/task_get/html/{id}  |
[**bingLocalPackLiveRegular**](SerpApi.md#bingLocalPackLiveRegular) | **POST**  /v3/serp/bing/local_pack/live/regular  |
[**bingLocalPackLiveHtml**](SerpApi.md#bingLocalPackLiveHtml) | **POST**  /v3/serp/bing/local_pack/live/html  |
[**serpYoutubeLocations**](SerpApi.md#serpYoutubeLocations) | **GET**  /v3/serp/youtube/locations  |
[**serpYoutubeLocationsCountry**](SerpApi.md#serpYoutubeLocationsCountry) | **GET**  /v3/serp/youtube/locations/{country}  |
[**serpYoutubeLanguages**](SerpApi.md#serpYoutubeLanguages) | **GET**  /v3/serp/youtube/languages  |
[**youtubeVideoInfoTaskPost**](SerpApi.md#youtubeVideoInfoTaskPost) | **POST**  /v3/serp/youtube/video_info/task_post  |
[**youtubeVideoInfoTasksReady**](SerpApi.md#youtubeVideoInfoTasksReady) | **GET**  /v3/serp/youtube/video_info/tasks_ready  |
[**youtubeVideoInfoTasksFixed**](SerpApi.md#youtubeVideoInfoTasksFixed) | **GET**  /v3/serp/youtube/video_info/tasks_fixed  |
[**youtubeVideoInfoTaskGetAdvanced**](SerpApi.md#youtubeVideoInfoTaskGetAdvanced) | **GET**  /v3/serp/youtube/video_info/task_get/advanced/{id}  |
[**youtubeVideoInfoLiveAdvanced**](SerpApi.md#youtubeVideoInfoLiveAdvanced) | **POST**  /v3/serp/youtube/video_info/live/advanced  |
[**youtubeVideoSubtitlesTaskPost**](SerpApi.md#youtubeVideoSubtitlesTaskPost) | **POST**  /v3/serp/youtube/video_subtitles/task_post  |
[**youtubeVideoSubtitlesTasksReady**](SerpApi.md#youtubeVideoSubtitlesTasksReady) | **GET**  /v3/serp/youtube/video_subtitles/tasks_ready  |
[**youtubeVideoSubtitlesTasksFixed**](SerpApi.md#youtubeVideoSubtitlesTasksFixed) | **GET**  /v3/serp/youtube/video_subtitles/tasks_fixed  |
[**youtubeVideoSubtitlesTaskGetAdvanced**](SerpApi.md#youtubeVideoSubtitlesTaskGetAdvanced) | **GET**  /v3/serp/youtube/video_subtitles/task_get/advanced/{id}  |
[**youtubeVideoSubtitlesLiveAdvanced**](SerpApi.md#youtubeVideoSubtitlesLiveAdvanced) | **POST**  /v3/serp/youtube/video_subtitles/live/advanced  |
[**youtubeVideoCommentsTaskPost**](SerpApi.md#youtubeVideoCommentsTaskPost) | **POST**  /v3/serp/youtube/video_comments/task_post  |
[**youtubeVideoCommentsTasksReady**](SerpApi.md#youtubeVideoCommentsTasksReady) | **GET**  /v3/serp/youtube/video_comments/tasks_ready  |
[**youtubeVideoCommentsTasksFixed**](SerpApi.md#youtubeVideoCommentsTasksFixed) | **GET**  /v3/serp/youtube/video_comments/tasks_fixed  |
[**youtubeVideoCommentsTaskGetAdvanced**](SerpApi.md#youtubeVideoCommentsTaskGetAdvanced) | **GET**  /v3/serp/youtube/video_comments/task_get/advanced/{id}  |
[**youtubeVideoCommentsLiveAdvanced**](SerpApi.md#youtubeVideoCommentsLiveAdvanced) | **POST**  /v3/serp/youtube/video_comments/live/advanced  |
[**serpYahooLocations**](SerpApi.md#serpYahooLocations) | **GET**  /v3/serp/yahoo/locations  |
[**serpYahooLocationsCountry**](SerpApi.md#serpYahooLocationsCountry) | **GET**  /v3/serp/yahoo/locations/{country}  |
[**serpYahooLanguages**](SerpApi.md#serpYahooLanguages) | **GET**  /v3/serp/yahoo/languages  |
[**yahooOrganicTaskPost**](SerpApi.md#yahooOrganicTaskPost) | **POST**  /v3/serp/yahoo/organic/task_post  |
[**yahooOrganicTasksReady**](SerpApi.md#yahooOrganicTasksReady) | **GET**  /v3/serp/yahoo/organic/tasks_ready  |
[**yahooOrganicTasksFixed**](SerpApi.md#yahooOrganicTasksFixed) | **GET**  /v3/serp/yahoo/organic/tasks_fixed  |
[**yahooOrganicTaskGetRegular**](SerpApi.md#yahooOrganicTaskGetRegular) | **GET**  /v3/serp/yahoo/organic/task_get/regular/{id}  |
[**yahooOrganicTaskGetAdvanced**](SerpApi.md#yahooOrganicTaskGetAdvanced) | **GET**  /v3/serp/yahoo/organic/task_get/advanced/{id}  |
[**yahooOrganicTaskGetHtml**](SerpApi.md#yahooOrganicTaskGetHtml) | **GET**  /v3/serp/yahoo/organic/task_get/html/{id}  |
[**yahooOrganicLiveRegular**](SerpApi.md#yahooOrganicLiveRegular) | **POST**  /v3/serp/yahoo/organic/live/regular  |
[**yahooOrganicLiveAdvanced**](SerpApi.md#yahooOrganicLiveAdvanced) | **POST**  /v3/serp/yahoo/organic/live/advanced  |
[**yahooOrganicLiveHtml**](SerpApi.md#yahooOrganicLiveHtml) | **POST**  /v3/serp/yahoo/organic/live/html  |
[**serpBaiduLocations**](SerpApi.md#serpBaiduLocations) | **GET**  /v3/serp/baidu/locations  |
[**serpBaiduLocationsCountry**](SerpApi.md#serpBaiduLocationsCountry) | **GET**  /v3/serp/baidu/locations/{country}  |
[**serpBaiduLanguages**](SerpApi.md#serpBaiduLanguages) | **GET**  /v3/serp/baidu/languages  |
[**baiduOrganicTaskPost**](SerpApi.md#baiduOrganicTaskPost) | **POST**  /v3/serp/baidu/organic/task_post  |
[**baiduOrganicTasksReady**](SerpApi.md#baiduOrganicTasksReady) | **GET**  /v3/serp/baidu/organic/tasks_ready  |
[**baiduOrganicTasksFixed**](SerpApi.md#baiduOrganicTasksFixed) | **GET**  /v3/serp/baidu/organic/tasks_fixed  |
[**baiduOrganicTaskGetRegular**](SerpApi.md#baiduOrganicTaskGetRegular) | **GET**  /v3/serp/baidu/organic/task_get/regular/{id}  |
[**baiduOrganicTaskGetAdvanced**](SerpApi.md#baiduOrganicTaskGetAdvanced) | **GET**  /v3/serp/baidu/organic/task_get/advanced/{id}  |
[**baiduOrganicTaskGetHtml**](SerpApi.md#baiduOrganicTaskGetHtml) | **GET**  /v3/serp/baidu/organic/task_get/html/{id}  |
[**naverOrganicTaskPost**](SerpApi.md#naverOrganicTaskPost) | **POST**  /v3/serp/naver/organic/task_post  |
[**naverOrganicTasksReady**](SerpApi.md#naverOrganicTasksReady) | **GET**  /v3/serp/naver/organic/tasks_ready  |
[**naverOrganicTasksFixed**](SerpApi.md#naverOrganicTasksFixed) | **GET**  /v3/serp/naver/organic/tasks_fixed  |
[**naverOrganicTaskGetRegular**](SerpApi.md#naverOrganicTaskGetRegular) | **GET**  /v3/serp/naver/organic/task_get/regular/{id}  |
[**naverOrganicTaskGetAdvanced**](SerpApi.md#naverOrganicTaskGetAdvanced) | **GET**  /v3/serp/naver/organic/task_get/advanced/{id}  |
[**naverOrganicTaskGetHtml**](SerpApi.md#naverOrganicTaskGetHtml) | **GET**  /v3/serp/naver/organic/task_get/html/{id}  |
[**serpSeznamLocations**](SerpApi.md#serpSeznamLocations) | **GET**  /v3/serp/seznam/locations  |
[**serpSeznamLocationsCountry**](SerpApi.md#serpSeznamLocationsCountry) | **GET**  /v3/serp/seznam/locations/{country}  |
[**serpSeznamLanguages**](SerpApi.md#serpSeznamLanguages) | **GET**  /v3/serp/seznam/languages  |
[**seznamOrganicTaskPost**](SerpApi.md#seznamOrganicTaskPost) | **POST**  /v3/serp/seznam/organic/task_post  |
[**seznamOrganicTasksReady**](SerpApi.md#seznamOrganicTasksReady) | **GET**  /v3/serp/seznam/organic/tasks_ready  |
[**seznamOrganicTasksFixed**](SerpApi.md#seznamOrganicTasksFixed) | **GET**  /v3/serp/seznam/organic/tasks_fixed  |
[**seznamOrganicTaskGetRegular**](SerpApi.md#seznamOrganicTaskGetRegular) | **GET**  /v3/serp/seznam/organic/task_get/regular/{id}  |
[**seznamOrganicTaskGetAdvanced**](SerpApi.md#seznamOrganicTaskGetAdvanced) | **GET**  /v3/serp/seznam/organic/task_get/advanced/{id}  |
[**seznamOrganicTaskGetHtml**](SerpApi.md#seznamOrganicTaskGetHtml) | **GET**  /v3/serp/seznam/organic/task_get/html/{id}  |
[**googleFinanceExploreTaskPost**](SerpApi.md#googleFinanceExploreTaskPost) | **POST**  /v3/serp/google/finance_explore/task_post  |
[**googleFinanceExploreTasksReady**](SerpApi.md#googleFinanceExploreTasksReady) | **GET**  /v3/serp/google/finance_explore/tasks_ready  |
[**googleFinanceExploreTaskGetAdvanced**](SerpApi.md#googleFinanceExploreTaskGetAdvanced) | **GET**  /v3/serp/google/finance_explore/task_get/advanced/{id}  |
[**googleFinanceExploreTaskGetHtml**](SerpApi.md#googleFinanceExploreTaskGetHtml) | **GET**  /v3/serp/google/finance_explore/task_get/html/{id}  |
[**googleFinanceExploreLiveAdvanced**](SerpApi.md#googleFinanceExploreLiveAdvanced) | **POST**  /v3/serp/google/finance_explore/live/advanced  |
[**googleFinanceExploreLiveHtml**](SerpApi.md#googleFinanceExploreLiveHtml) | **POST**  /v3/serp/google/finance_explore/live/html  |
[**googleFinanceMarketsTaskPost**](SerpApi.md#googleFinanceMarketsTaskPost) | **POST**  /v3/serp/google/finance_markets/task_post  |
[**googleFinanceMarketsTasksReady**](SerpApi.md#googleFinanceMarketsTasksReady) | **GET**  /v3/serp/google/finance_markets/tasks_ready  |
[**googleFinanceMarketsTaskGetAdvanced**](SerpApi.md#googleFinanceMarketsTaskGetAdvanced) | **GET**  /v3/serp/google/finance_markets/task_get/advanced/{id}  |
[**googleFinanceMarketsTaskGetHtml**](SerpApi.md#googleFinanceMarketsTaskGetHtml) | **GET**  /v3/serp/google/finance_markets/task_get/html/{id}  |
[**googleFinanceMarketsLiveAdvanced**](SerpApi.md#googleFinanceMarketsLiveAdvanced) | **POST**  /v3/serp/google/finance_markets/live/advanced  |
[**googleFinanceMarketsLiveHtml**](SerpApi.md#googleFinanceMarketsLiveHtml) | **POST**  /v3/serp/google/finance_markets/live/html  |
[**googleFinanceQuoteTaskPost**](SerpApi.md#googleFinanceQuoteTaskPost) | **POST**  /v3/serp/google/finance_quote/task_post  |
[**googleFinanceQuoteTasksReady**](SerpApi.md#googleFinanceQuoteTasksReady) | **GET**  /v3/serp/google/finance_quote/tasks_ready  |
[**googleFinanceQuoteTaskGetAdvanced**](SerpApi.md#googleFinanceQuoteTaskGetAdvanced) | **GET**  /v3/serp/google/finance_quote/task_get/advanced/{id}  |
[**googleFinanceQuoteTaskGetHtml**](SerpApi.md#googleFinanceQuoteTaskGetHtml) | **GET**  /v3/serp/google/finance_quote/task_get/html/{id}  |
[**googleFinanceQuoteLiveAdvanced**](SerpApi.md#googleFinanceQuoteLiveAdvanced) | **POST**  /v3/serp/google/finance_quote/live/advanced  |
[**googleFinanceQuoteLiveHtml**](SerpApi.md#googleFinanceQuoteLiveHtml) | **POST**  /v3/serp/google/finance_quote/live/html  |
[**googleFinanceTickerSearchTaskPost**](SerpApi.md#googleFinanceTickerSearchTaskPost) | **POST**  /v3/serp/google/finance_ticker_search/task_post  |
[**googleFinanceTickerSearchTasksReady**](SerpApi.md#googleFinanceTickerSearchTasksReady) | **GET**  /v3/serp/google/finance_ticker_search/tasks_ready  |
[**googleFinanceTickerSearchTaskGetAdvanced**](SerpApi.md#googleFinanceTickerSearchTaskGetAdvanced) | **GET**  /v3/serp/google/finance_ticker_search/task_get/advanced/{id}  |
[**googleFinanceTickerSearchLiveAdvanced**](SerpApi.md#googleFinanceTickerSearchLiveAdvanced) | **POST**  /v3/serp/google/finance_ticker_search/live/advanced  |

<a id="serpIdList"></a>
# **serpIdList**
> SerpIdListResponseInfo serpIdList()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_id_list_request_info import List[Optional[SerpIdListRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_id_list([SerpIdListRequestInfo(
                datetime_from="2025-07-14 10:23:34 +00:00",
                datetime_to="2025-09-14 10:23:34 +00:00",
                limit=100,
                offset=0,
                sort="desc",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpIdListRequestInfo]]&gt;**](List[Optional[SerpIdListRequestInfo]].md)|  | [optional] |



### Return type

[**SerpIdListResponseInfo**](SerpIdListResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpErrors"></a>
# **serpErrors**
> SerpErrorsResponseInfo serpErrors()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_errors_request_info import List[Optional[SerpErrorsRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_errors([SerpErrorsRequestInfo(
                limit=10,
                offset=0,
                filtered_function="pingback_url",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpErrorsRequestInfo]]&gt;**](List[Optional[SerpErrorsRequestInfo]].md)|  | [optional] |



### Return type

[**SerpErrorsResponseInfo**](SerpErrorsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="screenshot"></a>
# **screenshot**
> SerpScreenshotResponseInfo screenshot()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_screenshot_request_info import List[Optional[SerpScreenshotRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.screenshot([SerpScreenshotRequestInfo(
                task_id="06211235-0696-0139-1000-36727fbd3c90",
                browser_screen_scale_factor=0.5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpScreenshotRequestInfo]]&gt;**](List[Optional[SerpScreenshotRequestInfo]].md)|  | [optional] |



### Return type

[**SerpScreenshotResponseInfo**](SerpScreenshotResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiSummary"></a>
# **aiSummary**
> SerpAiSummaryResponseInfo aiSummary()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_ai_summary_request_info import List[Optional[SerpAiSummaryRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.ai_summary([SerpAiSummaryRequestInfo(
                task_id="07031739-1535-0139-0000-9d1e639a5b7d",
                prompt="explain what DataForSEO is",
                fetch_content=True,
                include_links=True,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpAiSummaryRequestInfo]]&gt;**](List[Optional[SerpAiSummaryRequestInfo]].md)|  | [optional] |



### Return type

[**SerpAiSummaryResponseInfo**](SerpAiSummaryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpGoogleLocations"></a>
# **serpGoogleLocations**
> SerpGoogleLocationsResponseInfo serpGoogleLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_google_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleLocationsResponseInfo**](SerpGoogleLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpGoogleLocationsCountry"></a>
# **serpGoogleLocationsCountry**
> SerpGoogleLocationsCountryResponseInfo serpGoogleLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        country = "us"
        response = serp_api.serp_google_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleLocationsCountryResponseInfo**](SerpGoogleLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpGoogleLanguages"></a>
# **serpGoogleLanguages**
> SerpGoogleLanguagesResponseInfo serpGoogleLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_google_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleLanguagesResponseInfo**](SerpGoogleLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleOrganicTaskPost"></a>
# **googleOrganicTaskPost**
> SerpGoogleOrganicTaskPostResponseInfo googleOrganicTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_organic_task_post_request_info import List[Optional[SerpGoogleOrganicTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_organic_task_post([SerpGoogleOrganicTaskPostRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleOrganicTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleOrganicTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleOrganicTaskPostResponseInfo**](SerpGoogleOrganicTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleOrganicTasksReady"></a>
# **googleOrganicTasksReady**
> SerpGoogleOrganicTasksReadyResponseInfo googleOrganicTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_organic_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleOrganicTasksReadyResponseInfo**](SerpGoogleOrganicTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="tasksReady"></a>
# **tasksReady**
> SerpTasksReadyResponseInfo tasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpTasksReadyResponseInfo**](SerpTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleOrganicTasksFixed"></a>
# **googleOrganicTasksFixed**
> SerpGoogleOrganicTasksFixedResponseInfo googleOrganicTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_organic_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleOrganicTasksFixedResponseInfo**](SerpGoogleOrganicTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleOrganicTaskGetRegular"></a>
# **googleOrganicTaskGetRegular**
> SerpGoogleOrganicTaskGetRegularResponseInfo googleOrganicTaskGetRegular()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_organic_task_get_regular(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleOrganicTaskGetRegularResponseInfo**](SerpGoogleOrganicTaskGetRegularResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleOrganicTaskGetAdvanced"></a>
# **googleOrganicTaskGetAdvanced**
> SerpGoogleOrganicTaskGetAdvancedResponseInfo googleOrganicTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_organic_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleOrganicTaskGetAdvancedResponseInfo**](SerpGoogleOrganicTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleOrganicTaskGetHtml"></a>
# **googleOrganicTaskGetHtml**
> SerpGoogleOrganicTaskGetHtmlResponseInfo googleOrganicTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_organic_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleOrganicTaskGetHtmlResponseInfo**](SerpGoogleOrganicTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleOrganicLiveRegular"></a>
# **googleOrganicLiveRegular**
> SerpGoogleOrganicLiveRegularResponseInfo googleOrganicLiveRegular()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_organic_live_regular_request_info import List[Optional[SerpGoogleOrganicLiveRegularRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_organic_live_regular([SerpGoogleOrganicLiveRegularRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleOrganicLiveRegularRequestInfo]]&gt;**](List[Optional[SerpGoogleOrganicLiveRegularRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleOrganicLiveRegularResponseInfo**](SerpGoogleOrganicLiveRegularResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleOrganicLiveAdvanced"></a>
# **googleOrganicLiveAdvanced**
> SerpGoogleOrganicLiveAdvancedResponseInfo googleOrganicLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_organic_live_advanced_request_info import List[Optional[SerpGoogleOrganicLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_organic_live_advanced([SerpGoogleOrganicLiveAdvancedRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
                calculate_rectangles=True,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleOrganicLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleOrganicLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleOrganicLiveAdvancedResponseInfo**](SerpGoogleOrganicLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleOrganicLiveHtml"></a>
# **googleOrganicLiveHtml**
> SerpGoogleOrganicLiveHtmlResponseInfo googleOrganicLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_organic_live_html_request_info import List[Optional[SerpGoogleOrganicLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_organic_live_html([SerpGoogleOrganicLiveHtmlRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleOrganicLiveHtmlRequestInfo]]&gt;**](List[Optional[SerpGoogleOrganicLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleOrganicLiveHtmlResponseInfo**](SerpGoogleOrganicLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpGoogleAiModeLanguages"></a>
# **serpGoogleAiModeLanguages**
> SerpGoogleAiModeLanguagesResponseInfo serpGoogleAiModeLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_google_ai_mode_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAiModeLanguagesResponseInfo**](SerpGoogleAiModeLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAiModeTaskPost"></a>
# **googleAiModeTaskPost**
> SerpGoogleAiModeTaskPostResponseInfo googleAiModeTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_ai_mode_task_post_request_info import List[Optional[SerpGoogleAiModeTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_ai_mode_task_post([SerpGoogleAiModeTaskPostRequestInfo(
                keyword="what is google ai mode",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleAiModeTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleAiModeTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleAiModeTaskPostResponseInfo**](SerpGoogleAiModeTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAiModeTasksReady"></a>
# **googleAiModeTasksReady**
> SerpGoogleAiModeTasksReadyResponseInfo googleAiModeTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_ai_mode_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAiModeTasksReadyResponseInfo**](SerpGoogleAiModeTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAiModeTasksFixed"></a>
# **googleAiModeTasksFixed**
> SerpGoogleAiModeTasksFixedResponseInfo googleAiModeTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_ai_mode_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAiModeTasksFixedResponseInfo**](SerpGoogleAiModeTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAiModeTaskGetAdvanced"></a>
# **googleAiModeTaskGetAdvanced**
> SerpGoogleAiModeTaskGetAdvancedResponseInfo googleAiModeTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_ai_mode_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAiModeTaskGetAdvancedResponseInfo**](SerpGoogleAiModeTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAiModeTaskGetHtml"></a>
# **googleAiModeTaskGetHtml**
> SerpGoogleAiModeTaskGetHtmlResponseInfo googleAiModeTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_ai_mode_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAiModeTaskGetHtmlResponseInfo**](SerpGoogleAiModeTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAiModeLiveAdvanced"></a>
# **googleAiModeLiveAdvanced**
> SerpGoogleAiModeLiveAdvancedResponseInfo googleAiModeLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_ai_mode_live_advanced_request_info import List[Optional[SerpGoogleAiModeLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_ai_mode_live_advanced([SerpGoogleAiModeLiveAdvancedRequestInfo(
                keyword="what is google ai mode",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleAiModeLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleAiModeLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleAiModeLiveAdvancedResponseInfo**](SerpGoogleAiModeLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAiModeLiveHtml"></a>
# **googleAiModeLiveHtml**
> SerpGoogleAiModeLiveHtmlResponseInfo googleAiModeLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_ai_mode_live_html_request_info import List[Optional[SerpGoogleAiModeLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_ai_mode_live_html([SerpGoogleAiModeLiveHtmlRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleAiModeLiveHtmlRequestInfo]]&gt;**](List[Optional[SerpGoogleAiModeLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleAiModeLiveHtmlResponseInfo**](SerpGoogleAiModeLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMapsTaskPost"></a>
# **googleMapsTaskPost**
> SerpGoogleMapsTaskPostResponseInfo googleMapsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_maps_task_post_request_info import List[Optional[SerpGoogleMapsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_maps_task_post([SerpGoogleMapsTaskPostRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleMapsTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleMapsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleMapsTaskPostResponseInfo**](SerpGoogleMapsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMapsTasksReady"></a>
# **googleMapsTasksReady**
> SerpGoogleMapsTasksReadyResponseInfo googleMapsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_maps_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleMapsTasksReadyResponseInfo**](SerpGoogleMapsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMapsTasksFixed"></a>
# **googleMapsTasksFixed**
> SerpGoogleMapsTasksFixedResponseInfo googleMapsTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_maps_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleMapsTasksFixedResponseInfo**](SerpGoogleMapsTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMapsTaskGetAdvanced"></a>
# **googleMapsTaskGetAdvanced**
> SerpGoogleMapsTaskGetAdvancedResponseInfo googleMapsTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_maps_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleMapsTaskGetAdvancedResponseInfo**](SerpGoogleMapsTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMapsLiveAdvanced"></a>
# **googleMapsLiveAdvanced**
> SerpGoogleMapsLiveAdvancedResponseInfo googleMapsLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_maps_live_advanced_request_info import List[Optional[SerpGoogleMapsLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_maps_live_advanced([SerpGoogleMapsLiveAdvancedRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleMapsLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleMapsLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleMapsLiveAdvancedResponseInfo**](SerpGoogleMapsLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleLocalFinderTaskPost"></a>
# **googleLocalFinderTaskPost**
> SerpGoogleLocalFinderTaskPostResponseInfo googleLocalFinderTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_local_finder_task_post_request_info import List[Optional[SerpGoogleLocalFinderTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_local_finder_task_post([SerpGoogleLocalFinderTaskPostRequestInfo(
                keyword="local nail services",
                location_code=2840,
                language_code="en",
                min_rating=4.5,
                time_filter="monday",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleLocalFinderTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleLocalFinderTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleLocalFinderTaskPostResponseInfo**](SerpGoogleLocalFinderTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleLocalFinderTasksReady"></a>
# **googleLocalFinderTasksReady**
> SerpGoogleLocalFinderTasksReadyResponseInfo googleLocalFinderTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_local_finder_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleLocalFinderTasksReadyResponseInfo**](SerpGoogleLocalFinderTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleLocalFinderTasksFixed"></a>
# **googleLocalFinderTasksFixed**
> SerpGoogleLocalFinderTasksFixedResponseInfo googleLocalFinderTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_local_finder_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleLocalFinderTasksFixedResponseInfo**](SerpGoogleLocalFinderTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleLocalFinderTaskGetAdvanced"></a>
# **googleLocalFinderTaskGetAdvanced**
> SerpGoogleLocalFinderTaskGetAdvancedResponseInfo googleLocalFinderTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_local_finder_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleLocalFinderTaskGetAdvancedResponseInfo**](SerpGoogleLocalFinderTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleLocalFinderTaskGetHtml"></a>
# **googleLocalFinderTaskGetHtml**
> SerpGoogleLocalFinderTaskGetHtmlResponseInfo googleLocalFinderTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_local_finder_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleLocalFinderTaskGetHtmlResponseInfo**](SerpGoogleLocalFinderTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleLocalFinderLiveAdvanced"></a>
# **googleLocalFinderLiveAdvanced**
> SerpGoogleLocalFinderLiveAdvancedResponseInfo googleLocalFinderLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_local_finder_live_advanced_request_info import List[Optional[SerpGoogleLocalFinderLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_local_finder_live_advanced([SerpGoogleLocalFinderLiveAdvancedRequestInfo(
                keyword="local nail services",
                location_code=2840,
                language_code="en",
                min_rating=4.5,
                time_filter="monday",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleLocalFinderLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleLocalFinderLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleLocalFinderLiveAdvancedResponseInfo**](SerpGoogleLocalFinderLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleLocalFinderLiveHtml"></a>
# **googleLocalFinderLiveHtml**
> SerpGoogleLocalFinderLiveHtmlResponseInfo googleLocalFinderLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_local_finder_live_html_request_info import List[Optional[SerpGoogleLocalFinderLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_local_finder_live_html([SerpGoogleLocalFinderLiveHtmlRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleLocalFinderLiveHtmlRequestInfo]]&gt;**](List[Optional[SerpGoogleLocalFinderLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleLocalFinderLiveHtmlResponseInfo**](SerpGoogleLocalFinderLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleNewsTaskPost"></a>
# **googleNewsTaskPost**
> SerpGoogleNewsTaskPostResponseInfo googleNewsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_news_task_post_request_info import List[Optional[SerpGoogleNewsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_news_task_post([SerpGoogleNewsTaskPostRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleNewsTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleNewsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleNewsTaskPostResponseInfo**](SerpGoogleNewsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleNewsTasksReady"></a>
# **googleNewsTasksReady**
> SerpGoogleNewsTasksReadyResponseInfo googleNewsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_news_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleNewsTasksReadyResponseInfo**](SerpGoogleNewsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleNewsTasksFixed"></a>
# **googleNewsTasksFixed**
> SerpGoogleNewsTasksFixedResponseInfo googleNewsTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_news_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleNewsTasksFixedResponseInfo**](SerpGoogleNewsTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleNewsTaskGetAdvanced"></a>
# **googleNewsTaskGetAdvanced**
> SerpGoogleNewsTaskGetAdvancedResponseInfo googleNewsTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_news_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleNewsTaskGetAdvancedResponseInfo**](SerpGoogleNewsTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleNewsTaskGetHtml"></a>
# **googleNewsTaskGetHtml**
> SerpGoogleNewsTaskGetHtmlResponseInfo googleNewsTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_news_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleNewsTaskGetHtmlResponseInfo**](SerpGoogleNewsTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleNewsLiveAdvanced"></a>
# **googleNewsLiveAdvanced**
> SerpGoogleNewsLiveAdvancedResponseInfo googleNewsLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_news_live_advanced_request_info import List[Optional[SerpGoogleNewsLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_news_live_advanced([SerpGoogleNewsLiveAdvancedRequestInfo(
                keyword="android",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleNewsLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleNewsLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleNewsLiveAdvancedResponseInfo**](SerpGoogleNewsLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleNewsLiveHtml"></a>
# **googleNewsLiveHtml**
> SerpGoogleNewsLiveHtmlResponseInfo googleNewsLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_news_live_html_request_info import List[Optional[SerpGoogleNewsLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_news_live_html([SerpGoogleNewsLiveHtmlRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleNewsLiveHtmlRequestInfo]]&gt;**](List[Optional[SerpGoogleNewsLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleNewsLiveHtmlResponseInfo**](SerpGoogleNewsLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleEventsTaskPost"></a>
# **googleEventsTaskPost**
> SerpGoogleEventsTaskPostResponseInfo googleEventsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_events_task_post_request_info import List[Optional[SerpGoogleEventsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_events_task_post([SerpGoogleEventsTaskPostRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleEventsTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleEventsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleEventsTaskPostResponseInfo**](SerpGoogleEventsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleEventsTasksReady"></a>
# **googleEventsTasksReady**
> SerpGoogleEventsTasksReadyResponseInfo googleEventsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_events_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleEventsTasksReadyResponseInfo**](SerpGoogleEventsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleEventsTasksFixed"></a>
# **googleEventsTasksFixed**
> SerpGoogleEventsTasksFixedResponseInfo googleEventsTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_events_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleEventsTasksFixedResponseInfo**](SerpGoogleEventsTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleEventsTaskGetAdvanced"></a>
# **googleEventsTaskGetAdvanced**
> SerpGoogleEventsTaskGetAdvancedResponseInfo googleEventsTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_events_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleEventsTaskGetAdvancedResponseInfo**](SerpGoogleEventsTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleEventsLiveAdvanced"></a>
# **googleEventsLiveAdvanced**
> SerpGoogleEventsLiveAdvancedResponseInfo googleEventsLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_events_live_advanced_request_info import List[Optional[SerpGoogleEventsLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_events_live_advanced([SerpGoogleEventsLiveAdvancedRequestInfo(
                keyword="concerts",
                location_name="Los Angeles,California,United States",
                date_range="today",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleEventsLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleEventsLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleEventsLiveAdvancedResponseInfo**](SerpGoogleEventsLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleImagesTaskPost"></a>
# **googleImagesTaskPost**
> SerpGoogleImagesTaskPostResponseInfo googleImagesTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_images_task_post_request_info import List[Optional[SerpGoogleImagesTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_images_task_post([SerpGoogleImagesTaskPostRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleImagesTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleImagesTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleImagesTaskPostResponseInfo**](SerpGoogleImagesTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleImagesTasksReady"></a>
# **googleImagesTasksReady**
> SerpGoogleImagesTasksReadyResponseInfo googleImagesTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_images_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleImagesTasksReadyResponseInfo**](SerpGoogleImagesTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleImagesTasksFixed"></a>
# **googleImagesTasksFixed**
> SerpGoogleImagesTasksFixedResponseInfo googleImagesTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_images_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleImagesTasksFixedResponseInfo**](SerpGoogleImagesTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleImagesTaskGetAdvanced"></a>
# **googleImagesTaskGetAdvanced**
> SerpGoogleImagesTaskGetAdvancedResponseInfo googleImagesTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_images_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleImagesTaskGetAdvancedResponseInfo**](SerpGoogleImagesTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleImagesTaskGetHtml"></a>
# **googleImagesTaskGetHtml**
> SerpGoogleImagesTaskGetHtmlResponseInfo googleImagesTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_images_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleImagesTaskGetHtmlResponseInfo**](SerpGoogleImagesTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleImagesLiveAdvanced"></a>
# **googleImagesLiveAdvanced**
> SerpGoogleImagesLiveAdvancedResponseInfo googleImagesLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_images_live_advanced_request_info import List[Optional[SerpGoogleImagesLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_images_live_advanced([SerpGoogleImagesLiveAdvancedRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleImagesLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleImagesLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleImagesLiveAdvancedResponseInfo**](SerpGoogleImagesLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleImagesLiveHtml"></a>
# **googleImagesLiveHtml**
> SerpGoogleImagesLiveHtmlResponseInfo googleImagesLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_images_live_html_request_info import List[Optional[SerpGoogleImagesLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_images_live_html([SerpGoogleImagesLiveHtmlRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleImagesLiveHtmlRequestInfo]]&gt;**](List[Optional[SerpGoogleImagesLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleImagesLiveHtmlResponseInfo**](SerpGoogleImagesLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleSearchByImageTaskPost"></a>
# **googleSearchByImageTaskPost**
> SerpGoogleSearchByImageTaskPostResponseInfo googleSearchByImageTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_search_by_image_task_post_request_info import List[Optional[SerpGoogleSearchByImageTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_search_by_image_task_post([SerpGoogleSearchByImageTaskPostRequestInfo(
                image_url="https://dataforseo.com/wp-content/uploads/2016/11/data_for_seo_light_429.png",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleSearchByImageTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleSearchByImageTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleSearchByImageTaskPostResponseInfo**](SerpGoogleSearchByImageTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleSearchByImageTasksReady"></a>
# **googleSearchByImageTasksReady**
> SerpGoogleSearchByImageTasksReadyResponseInfo googleSearchByImageTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_search_by_image_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleSearchByImageTasksReadyResponseInfo**](SerpGoogleSearchByImageTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleSearchByImageTasksFixed"></a>
# **googleSearchByImageTasksFixed**
> SerpGoogleSearchByImageTasksFixedResponseInfo googleSearchByImageTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_search_by_image_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleSearchByImageTasksFixedResponseInfo**](SerpGoogleSearchByImageTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleSearchByImageTaskGetAdvanced"></a>
# **googleSearchByImageTaskGetAdvanced**
> SerpGoogleSearchByImageTaskGetAdvancedResponseInfo googleSearchByImageTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_search_by_image_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleSearchByImageTaskGetAdvancedResponseInfo**](SerpGoogleSearchByImageTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleJobsTaskPost"></a>
# **googleJobsTaskPost**
> SerpGoogleJobsTaskPostResponseInfo googleJobsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_jobs_task_post_request_info import List[Optional[SerpGoogleJobsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_jobs_task_post([SerpGoogleJobsTaskPostRequestInfo(
                keyword=".net developer",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleJobsTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleJobsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleJobsTaskPostResponseInfo**](SerpGoogleJobsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleJobsTasksReady"></a>
# **googleJobsTasksReady**
> SerpGoogleJobsTasksReadyResponseInfo googleJobsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_jobs_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleJobsTasksReadyResponseInfo**](SerpGoogleJobsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleJobsTasksFixed"></a>
# **googleJobsTasksFixed**
> SerpGoogleJobsTasksFixedResponseInfo googleJobsTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_jobs_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleJobsTasksFixedResponseInfo**](SerpGoogleJobsTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleJobsTaskGetAdvanced"></a>
# **googleJobsTaskGetAdvanced**
> SerpGoogleJobsTaskGetAdvancedResponseInfo googleJobsTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_jobs_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleJobsTaskGetAdvancedResponseInfo**](SerpGoogleJobsTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleJobsTaskGetHtml"></a>
# **googleJobsTaskGetHtml**
> SerpGoogleJobsTaskGetHtmlResponseInfo googleJobsTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_jobs_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleJobsTaskGetHtmlResponseInfo**](SerpGoogleJobsTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAutocompleteTaskPost"></a>
# **googleAutocompleteTaskPost**
> SerpGoogleAutocompleteTaskPostResponseInfo googleAutocompleteTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_autocomplete_task_post_request_info import List[Optional[SerpGoogleAutocompleteTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_autocomplete_task_post([SerpGoogleAutocompleteTaskPostRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
                cursor_pointer=6,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleAutocompleteTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleAutocompleteTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleAutocompleteTaskPostResponseInfo**](SerpGoogleAutocompleteTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAutocompleteTasksReady"></a>
# **googleAutocompleteTasksReady**
> SerpGoogleAutocompleteTasksReadyResponseInfo googleAutocompleteTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_autocomplete_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAutocompleteTasksReadyResponseInfo**](SerpGoogleAutocompleteTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAutocompleteTasksFixed"></a>
# **googleAutocompleteTasksFixed**
> SerpGoogleAutocompleteTasksFixedResponseInfo googleAutocompleteTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_autocomplete_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAutocompleteTasksFixedResponseInfo**](SerpGoogleAutocompleteTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAutocompleteTaskGetAdvanced"></a>
# **googleAutocompleteTaskGetAdvanced**
> SerpGoogleAutocompleteTaskGetAdvancedResponseInfo googleAutocompleteTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_autocomplete_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAutocompleteTaskGetAdvancedResponseInfo**](SerpGoogleAutocompleteTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAutocompleteLiveAdvanced"></a>
# **googleAutocompleteLiveAdvanced**
> SerpGoogleAutocompleteLiveAdvancedResponseInfo googleAutocompleteLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_autocomplete_live_advanced_request_info import List[Optional[SerpGoogleAutocompleteLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_autocomplete_live_advanced([SerpGoogleAutocompleteLiveAdvancedRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
                client="gws-wiz-serp",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleAutocompleteLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleAutocompleteLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleAutocompleteLiveAdvancedResponseInfo**](SerpGoogleAutocompleteLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDatasetSearchTaskPost"></a>
# **googleDatasetSearchTaskPost**
> SerpGoogleDatasetSearchTaskPostResponseInfo googleDatasetSearchTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_dataset_search_task_post_request_info import List[Optional[SerpGoogleDatasetSearchTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_dataset_search_task_post([SerpGoogleDatasetSearchTaskPostRequestInfo(
                keyword="water quality",
                last_updated="1m",
                file_formats=[
                    "archive",
                    "image",
                    ],
                usage_rights="noncommercial",
                is_free=True,
                topics=[
                    "natural_sciences",
                    "geo",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleDatasetSearchTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleDatasetSearchTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleDatasetSearchTaskPostResponseInfo**](SerpGoogleDatasetSearchTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDatasetSearchTasksReady"></a>
# **googleDatasetSearchTasksReady**
> SerpGoogleDatasetSearchTasksReadyResponseInfo googleDatasetSearchTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_dataset_search_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleDatasetSearchTasksReadyResponseInfo**](SerpGoogleDatasetSearchTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDatasetSearchTasksFixed"></a>
# **googleDatasetSearchTasksFixed**
> SerpGoogleDatasetSearchTasksFixedResponseInfo googleDatasetSearchTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_dataset_search_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleDatasetSearchTasksFixedResponseInfo**](SerpGoogleDatasetSearchTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDatasetSearchTaskGetAdvanced"></a>
# **googleDatasetSearchTaskGetAdvanced**
> SerpGoogleDatasetSearchTaskGetAdvancedResponseInfo googleDatasetSearchTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_dataset_search_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleDatasetSearchTaskGetAdvancedResponseInfo**](SerpGoogleDatasetSearchTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDatasetSearchLiveAdvanced"></a>
# **googleDatasetSearchLiveAdvanced**
> SerpGoogleDatasetSearchLiveAdvancedResponseInfo googleDatasetSearchLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_dataset_search_live_advanced_request_info import List[Optional[SerpGoogleDatasetSearchLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_dataset_search_live_advanced([SerpGoogleDatasetSearchLiveAdvancedRequestInfo(
                keyword="water quality",
                last_updated="1m",
                file_formats=[
                    "archive",
                    "image",
                    ],
                usage_rights="noncommercial",
                is_free=True,
                topics=[
                    "natural_sciences",
                    "geo",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleDatasetSearchLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleDatasetSearchLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleDatasetSearchLiveAdvancedResponseInfo**](SerpGoogleDatasetSearchLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDatasetInfoTaskPost"></a>
# **googleDatasetInfoTaskPost**
> SerpGoogleDatasetInfoTaskPostResponseInfo googleDatasetInfoTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_dataset_info_task_post_request_info import List[Optional[SerpGoogleDatasetInfoTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_dataset_info_task_post([SerpGoogleDatasetInfoTaskPostRequestInfo(
                dataset_id="L2cvMTFqbl85ZHN6MQ==",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleDatasetInfoTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleDatasetInfoTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleDatasetInfoTaskPostResponseInfo**](SerpGoogleDatasetInfoTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDatasetInfoTasksReady"></a>
# **googleDatasetInfoTasksReady**
> SerpGoogleDatasetInfoTasksReadyResponseInfo googleDatasetInfoTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_dataset_info_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleDatasetInfoTasksReadyResponseInfo**](SerpGoogleDatasetInfoTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDatasetInfoTasksFixed"></a>
# **googleDatasetInfoTasksFixed**
> SerpGoogleDatasetInfoTasksFixedResponseInfo googleDatasetInfoTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_dataset_info_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleDatasetInfoTasksFixedResponseInfo**](SerpGoogleDatasetInfoTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDatasetInfoTaskGetAdvanced"></a>
# **googleDatasetInfoTaskGetAdvanced**
> SerpGoogleDatasetInfoTaskGetAdvancedResponseInfo googleDatasetInfoTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_dataset_info_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleDatasetInfoTaskGetAdvancedResponseInfo**](SerpGoogleDatasetInfoTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDatasetInfoLiveAdvanced"></a>
# **googleDatasetInfoLiveAdvanced**
> SerpGoogleDatasetInfoLiveAdvancedResponseInfo googleDatasetInfoLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_dataset_info_live_advanced_request_info import List[Optional[SerpGoogleDatasetInfoLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_dataset_info_live_advanced([SerpGoogleDatasetInfoLiveAdvancedRequestInfo(
                dataset_id="L2cvMTFqbl85ZHN6MQ==",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleDatasetInfoLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleDatasetInfoLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleDatasetInfoLiveAdvancedResponseInfo**](SerpGoogleDatasetInfoLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpGoogleAdsAdvertisersLocations"></a>
# **serpGoogleAdsAdvertisersLocations**
> SerpGoogleAdsAdvertisersLocationsResponseInfo serpGoogleAdsAdvertisersLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_google_ads_advertisers_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAdsAdvertisersLocationsResponseInfo**](SerpGoogleAdsAdvertisersLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsAdvertisersTaskPost"></a>
# **googleAdsAdvertisersTaskPost**
> SerpGoogleAdsAdvertisersTaskPostResponseInfo googleAdsAdvertisersTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_ads_advertisers_task_post_request_info import List[Optional[SerpGoogleAdsAdvertisersTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_ads_advertisers_task_post([SerpGoogleAdsAdvertisersTaskPostRequestInfo(
                keyword="apple",
                location_code=2840,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleAdsAdvertisersTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleAdsAdvertisersTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleAdsAdvertisersTaskPostResponseInfo**](SerpGoogleAdsAdvertisersTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsAdvertisersTasksReady"></a>
# **googleAdsAdvertisersTasksReady**
> SerpGoogleAdsAdvertisersTasksReadyResponseInfo googleAdsAdvertisersTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_ads_advertisers_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAdsAdvertisersTasksReadyResponseInfo**](SerpGoogleAdsAdvertisersTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsAdvertisersTaskGetAdvanced"></a>
# **googleAdsAdvertisersTaskGetAdvanced**
> SerpGoogleAdsAdvertisersTaskGetAdvancedResponseInfo googleAdsAdvertisersTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_ads_advertisers_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAdsAdvertisersTaskGetAdvancedResponseInfo**](SerpGoogleAdsAdvertisersTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpGoogleAdsSearchLocations"></a>
# **serpGoogleAdsSearchLocations**
> SerpGoogleAdsSearchLocationsResponseInfo serpGoogleAdsSearchLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_google_ads_search_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAdsSearchLocationsResponseInfo**](SerpGoogleAdsSearchLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsSearchTaskPost"></a>
# **googleAdsSearchTaskPost**
> SerpGoogleAdsSearchTaskPostResponseInfo googleAdsSearchTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_ads_search_task_post_request_info import List[Optional[SerpGoogleAdsSearchTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_ads_search_task_post([SerpGoogleAdsSearchTaskPostRequestInfo(
                advertiser_ids=[
                    "AR13752565271262920705",
                    "AR02439908557932462081",
                    ],
                location_code=2840,
                platform="google_search",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleAdsSearchTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleAdsSearchTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleAdsSearchTaskPostResponseInfo**](SerpGoogleAdsSearchTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsSearchTasksReady"></a>
# **googleAdsSearchTasksReady**
> SerpGoogleAdsSearchTasksReadyResponseInfo googleAdsSearchTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_ads_search_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAdsSearchTasksReadyResponseInfo**](SerpGoogleAdsSearchTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsSearchTaskGetAdvanced"></a>
# **googleAdsSearchTaskGetAdvanced**
> SerpGoogleAdsSearchTaskGetAdvancedResponseInfo googleAdsSearchTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_ads_search_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleAdsSearchTaskGetAdvancedResponseInfo**](SerpGoogleAdsSearchTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpBingLocations"></a>
# **serpBingLocations**
> SerpBingLocationsResponseInfo serpBingLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_bing_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingLocationsResponseInfo**](SerpBingLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpBingLocationsCountry"></a>
# **serpBingLocationsCountry**
> SerpBingLocationsCountryResponseInfo serpBingLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        country = "us"
        response = serp_api.serp_bing_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingLocationsCountryResponseInfo**](SerpBingLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpBingLanguages"></a>
# **serpBingLanguages**
> SerpBingLanguagesResponseInfo serpBingLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_bing_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingLanguagesResponseInfo**](SerpBingLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingOrganicTaskPost"></a>
# **bingOrganicTaskPost**
> SerpBingOrganicTaskPostResponseInfo bingOrganicTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_bing_organic_task_post_request_info import List[Optional[SerpBingOrganicTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.bing_organic_task_post([SerpBingOrganicTaskPostRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpBingOrganicTaskPostRequestInfo]]&gt;**](List[Optional[SerpBingOrganicTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpBingOrganicTaskPostResponseInfo**](SerpBingOrganicTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingOrganicTasksReady"></a>
# **bingOrganicTasksReady**
> SerpBingOrganicTasksReadyResponseInfo bingOrganicTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.bing_organic_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingOrganicTasksReadyResponseInfo**](SerpBingOrganicTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingOrganicTasksFixed"></a>
# **bingOrganicTasksFixed**
> SerpBingOrganicTasksFixedResponseInfo bingOrganicTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.bing_organic_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingOrganicTasksFixedResponseInfo**](SerpBingOrganicTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingOrganicTaskGetRegular"></a>
# **bingOrganicTaskGetRegular**
> SerpBingOrganicTaskGetRegularResponseInfo bingOrganicTaskGetRegular()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.bing_organic_task_get_regular(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingOrganicTaskGetRegularResponseInfo**](SerpBingOrganicTaskGetRegularResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingOrganicTaskGetAdvanced"></a>
# **bingOrganicTaskGetAdvanced**
> SerpBingOrganicTaskGetAdvancedResponseInfo bingOrganicTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.bing_organic_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingOrganicTaskGetAdvancedResponseInfo**](SerpBingOrganicTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingOrganicTaskGetHtml"></a>
# **bingOrganicTaskGetHtml**
> SerpBingOrganicTaskGetHtmlResponseInfo bingOrganicTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.bing_organic_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingOrganicTaskGetHtmlResponseInfo**](SerpBingOrganicTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingOrganicLiveRegular"></a>
# **bingOrganicLiveRegular**
> SerpBingOrganicLiveRegularResponseInfo bingOrganicLiveRegular()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_bing_organic_live_regular_request_info import List[Optional[SerpBingOrganicLiveRegularRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.bing_organic_live_regular([SerpBingOrganicLiveRegularRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpBingOrganicLiveRegularRequestInfo]]&gt;**](List[Optional[SerpBingOrganicLiveRegularRequestInfo]].md)|  | [optional] |



### Return type

[**SerpBingOrganicLiveRegularResponseInfo**](SerpBingOrganicLiveRegularResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingOrganicLiveAdvanced"></a>
# **bingOrganicLiveAdvanced**
> SerpBingOrganicLiveAdvancedResponseInfo bingOrganicLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_bing_organic_live_advanced_request_info import List[Optional[SerpBingOrganicLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.bing_organic_live_advanced([SerpBingOrganicLiveAdvancedRequestInfo(
                keyword="flight ticket new york san francisco",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpBingOrganicLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpBingOrganicLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpBingOrganicLiveAdvancedResponseInfo**](SerpBingOrganicLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingOrganicLiveHtml"></a>
# **bingOrganicLiveHtml**
> SerpBingOrganicLiveHtmlResponseInfo bingOrganicLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_bing_organic_live_html_request_info import List[Optional[SerpBingOrganicLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.bing_organic_live_html([SerpBingOrganicLiveHtmlRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpBingOrganicLiveHtmlRequestInfo]]&gt;**](List[Optional[SerpBingOrganicLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**SerpBingOrganicLiveHtmlResponseInfo**](SerpBingOrganicLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingLocalPackTaskPost"></a>
# **bingLocalPackTaskPost**
> SerpBingLocalPackTaskPostResponseInfo bingLocalPackTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_bing_local_pack_task_post_request_info import List[Optional[SerpBingLocalPackTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.bing_local_pack_task_post([SerpBingLocalPackTaskPostRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpBingLocalPackTaskPostRequestInfo]]&gt;**](List[Optional[SerpBingLocalPackTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpBingLocalPackTaskPostResponseInfo**](SerpBingLocalPackTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingLocalPackTasksReady"></a>
# **bingLocalPackTasksReady**
> SerpBingLocalPackTasksReadyResponseInfo bingLocalPackTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.bing_local_pack_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingLocalPackTasksReadyResponseInfo**](SerpBingLocalPackTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingLocalPackTasksFixed"></a>
# **bingLocalPackTasksFixed**
> SerpBingLocalPackTasksFixedResponseInfo bingLocalPackTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.bing_local_pack_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingLocalPackTasksFixedResponseInfo**](SerpBingLocalPackTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingLocalPackTaskGetRegular"></a>
# **bingLocalPackTaskGetRegular**
> SerpBingLocalPackTaskGetRegularResponseInfo bingLocalPackTaskGetRegular()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.bing_local_pack_task_get_regular(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingLocalPackTaskGetRegularResponseInfo**](SerpBingLocalPackTaskGetRegularResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingLocalPackTaskGetHtml"></a>
# **bingLocalPackTaskGetHtml**
> SerpBingLocalPackTaskGetHtmlResponseInfo bingLocalPackTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.bing_local_pack_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBingLocalPackTaskGetHtmlResponseInfo**](SerpBingLocalPackTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingLocalPackLiveRegular"></a>
# **bingLocalPackLiveRegular**
> SerpBingLocalPackLiveRegularResponseInfo bingLocalPackLiveRegular()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_bing_local_pack_live_regular_request_info import List[Optional[SerpBingLocalPackLiveRegularRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.bing_local_pack_live_regular([SerpBingLocalPackLiveRegularRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpBingLocalPackLiveRegularRequestInfo]]&gt;**](List[Optional[SerpBingLocalPackLiveRegularRequestInfo]].md)|  | [optional] |



### Return type

[**SerpBingLocalPackLiveRegularResponseInfo**](SerpBingLocalPackLiveRegularResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingLocalPackLiveHtml"></a>
# **bingLocalPackLiveHtml**
> SerpBingLocalPackLiveHtmlResponseInfo bingLocalPackLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_bing_local_pack_live_html_request_info import List[Optional[SerpBingLocalPackLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.bing_local_pack_live_html([SerpBingLocalPackLiveHtmlRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpBingLocalPackLiveHtmlRequestInfo]]&gt;**](List[Optional[SerpBingLocalPackLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**SerpBingLocalPackLiveHtmlResponseInfo**](SerpBingLocalPackLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpYoutubeLocations"></a>
# **serpYoutubeLocations**
> SerpYoutubeLocationsResponseInfo serpYoutubeLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_youtube_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeLocationsResponseInfo**](SerpYoutubeLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpYoutubeLocationsCountry"></a>
# **serpYoutubeLocationsCountry**
> SerpYoutubeLocationsCountryResponseInfo serpYoutubeLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        country = "us"
        response = serp_api.serp_youtube_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeLocationsCountryResponseInfo**](SerpYoutubeLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpYoutubeLanguages"></a>
# **serpYoutubeLanguages**
> SerpYoutubeLanguagesResponseInfo serpYoutubeLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_youtube_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeLanguagesResponseInfo**](SerpYoutubeLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoInfoTaskPost"></a>
# **youtubeVideoInfoTaskPost**
> SerpYoutubeVideoInfoTaskPostResponseInfo youtubeVideoInfoTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_youtube_video_info_task_post_request_info import List[Optional[SerpYoutubeVideoInfoTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_info_task_post([SerpYoutubeVideoInfoTaskPostRequestInfo(
                video_id="vQXvyV0zIP4",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpYoutubeVideoInfoTaskPostRequestInfo]]&gt;**](List[Optional[SerpYoutubeVideoInfoTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpYoutubeVideoInfoTaskPostResponseInfo**](SerpYoutubeVideoInfoTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoInfoTasksReady"></a>
# **youtubeVideoInfoTasksReady**
> SerpYoutubeVideoInfoTasksReadyResponseInfo youtubeVideoInfoTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_info_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeVideoInfoTasksReadyResponseInfo**](SerpYoutubeVideoInfoTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoInfoTasksFixed"></a>
# **youtubeVideoInfoTasksFixed**
> SerpYoutubeVideoInfoTasksFixedResponseInfo youtubeVideoInfoTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_info_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeVideoInfoTasksFixedResponseInfo**](SerpYoutubeVideoInfoTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoInfoTaskGetAdvanced"></a>
# **youtubeVideoInfoTaskGetAdvanced**
> SerpYoutubeVideoInfoTaskGetAdvancedResponseInfo youtubeVideoInfoTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.youtube_video_info_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeVideoInfoTaskGetAdvancedResponseInfo**](SerpYoutubeVideoInfoTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoInfoLiveAdvanced"></a>
# **youtubeVideoInfoLiveAdvanced**
> SerpYoutubeVideoInfoLiveAdvancedResponseInfo youtubeVideoInfoLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_youtube_video_info_live_advanced_request_info import List[Optional[SerpYoutubeVideoInfoLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_info_live_advanced([SerpYoutubeVideoInfoLiveAdvancedRequestInfo(
                video_id="vQXvyV0zIP4",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpYoutubeVideoInfoLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpYoutubeVideoInfoLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpYoutubeVideoInfoLiveAdvancedResponseInfo**](SerpYoutubeVideoInfoLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoSubtitlesTaskPost"></a>
# **youtubeVideoSubtitlesTaskPost**
> SerpYoutubeVideoSubtitlesTaskPostResponseInfo youtubeVideoSubtitlesTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_youtube_video_subtitles_task_post_request_info import List[Optional[SerpYoutubeVideoSubtitlesTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_subtitles_task_post([SerpYoutubeVideoSubtitlesTaskPostRequestInfo(
                video_id="Y8Wu4rSNJms",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpYoutubeVideoSubtitlesTaskPostRequestInfo]]&gt;**](List[Optional[SerpYoutubeVideoSubtitlesTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpYoutubeVideoSubtitlesTaskPostResponseInfo**](SerpYoutubeVideoSubtitlesTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoSubtitlesTasksReady"></a>
# **youtubeVideoSubtitlesTasksReady**
> SerpYoutubeVideoSubtitlesTasksReadyResponseInfo youtubeVideoSubtitlesTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_subtitles_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeVideoSubtitlesTasksReadyResponseInfo**](SerpYoutubeVideoSubtitlesTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoSubtitlesTasksFixed"></a>
# **youtubeVideoSubtitlesTasksFixed**
> SerpYoutubeVideoSubtitlesTasksFixedResponseInfo youtubeVideoSubtitlesTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_subtitles_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeVideoSubtitlesTasksFixedResponseInfo**](SerpYoutubeVideoSubtitlesTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoSubtitlesTaskGetAdvanced"></a>
# **youtubeVideoSubtitlesTaskGetAdvanced**
> SerpYoutubeVideoSubtitlesTaskGetAdvancedResponseInfo youtubeVideoSubtitlesTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.youtube_video_subtitles_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeVideoSubtitlesTaskGetAdvancedResponseInfo**](SerpYoutubeVideoSubtitlesTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoSubtitlesLiveAdvanced"></a>
# **youtubeVideoSubtitlesLiveAdvanced**
> SerpYoutubeVideoSubtitlesLiveAdvancedResponseInfo youtubeVideoSubtitlesLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_youtube_video_subtitles_live_advanced_request_info import List[Optional[SerpYoutubeVideoSubtitlesLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_subtitles_live_advanced([SerpYoutubeVideoSubtitlesLiveAdvancedRequestInfo(
                video_id="Y8Wu4rSNJms",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpYoutubeVideoSubtitlesLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpYoutubeVideoSubtitlesLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpYoutubeVideoSubtitlesLiveAdvancedResponseInfo**](SerpYoutubeVideoSubtitlesLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoCommentsTaskPost"></a>
# **youtubeVideoCommentsTaskPost**
> SerpYoutubeVideoCommentsTaskPostResponseInfo youtubeVideoCommentsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_youtube_video_comments_task_post_request_info import List[Optional[SerpYoutubeVideoCommentsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_comments_task_post([SerpYoutubeVideoCommentsTaskPostRequestInfo(
                video_id="vQXvyV0zIP4",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpYoutubeVideoCommentsTaskPostRequestInfo]]&gt;**](List[Optional[SerpYoutubeVideoCommentsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpYoutubeVideoCommentsTaskPostResponseInfo**](SerpYoutubeVideoCommentsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoCommentsTasksReady"></a>
# **youtubeVideoCommentsTasksReady**
> SerpYoutubeVideoCommentsTasksReadyResponseInfo youtubeVideoCommentsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_comments_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeVideoCommentsTasksReadyResponseInfo**](SerpYoutubeVideoCommentsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoCommentsTasksFixed"></a>
# **youtubeVideoCommentsTasksFixed**
> SerpYoutubeVideoCommentsTasksFixedResponseInfo youtubeVideoCommentsTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_comments_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeVideoCommentsTasksFixedResponseInfo**](SerpYoutubeVideoCommentsTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoCommentsTaskGetAdvanced"></a>
# **youtubeVideoCommentsTaskGetAdvanced**
> SerpYoutubeVideoCommentsTaskGetAdvancedResponseInfo youtubeVideoCommentsTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.youtube_video_comments_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYoutubeVideoCommentsTaskGetAdvancedResponseInfo**](SerpYoutubeVideoCommentsTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="youtubeVideoCommentsLiveAdvanced"></a>
# **youtubeVideoCommentsLiveAdvanced**
> SerpYoutubeVideoCommentsLiveAdvancedResponseInfo youtubeVideoCommentsLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_youtube_video_comments_live_advanced_request_info import List[Optional[SerpYoutubeVideoCommentsLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.youtube_video_comments_live_advanced([SerpYoutubeVideoCommentsLiveAdvancedRequestInfo(
                video_id="vQXvyV0zIP4",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpYoutubeVideoCommentsLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpYoutubeVideoCommentsLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpYoutubeVideoCommentsLiveAdvancedResponseInfo**](SerpYoutubeVideoCommentsLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpYahooLocations"></a>
# **serpYahooLocations**
> SerpYahooLocationsResponseInfo serpYahooLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_yahoo_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYahooLocationsResponseInfo**](SerpYahooLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpYahooLocationsCountry"></a>
# **serpYahooLocationsCountry**
> SerpYahooLocationsCountryResponseInfo serpYahooLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        country = "us"
        response = serp_api.serp_yahoo_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYahooLocationsCountryResponseInfo**](SerpYahooLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpYahooLanguages"></a>
# **serpYahooLanguages**
> SerpYahooLanguagesResponseInfo serpYahooLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_yahoo_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYahooLanguagesResponseInfo**](SerpYahooLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="yahooOrganicTaskPost"></a>
# **yahooOrganicTaskPost**
> SerpYahooOrganicTaskPostResponseInfo yahooOrganicTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_yahoo_organic_task_post_request_info import List[Optional[SerpYahooOrganicTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.yahoo_organic_task_post([SerpYahooOrganicTaskPostRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpYahooOrganicTaskPostRequestInfo]]&gt;**](List[Optional[SerpYahooOrganicTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpYahooOrganicTaskPostResponseInfo**](SerpYahooOrganicTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="yahooOrganicTasksReady"></a>
# **yahooOrganicTasksReady**
> SerpYahooOrganicTasksReadyResponseInfo yahooOrganicTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.yahoo_organic_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYahooOrganicTasksReadyResponseInfo**](SerpYahooOrganicTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="yahooOrganicTasksFixed"></a>
# **yahooOrganicTasksFixed**
> SerpYahooOrganicTasksFixedResponseInfo yahooOrganicTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.yahoo_organic_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYahooOrganicTasksFixedResponseInfo**](SerpYahooOrganicTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="yahooOrganicTaskGetRegular"></a>
# **yahooOrganicTaskGetRegular**
> SerpYahooOrganicTaskGetRegularResponseInfo yahooOrganicTaskGetRegular()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.yahoo_organic_task_get_regular(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYahooOrganicTaskGetRegularResponseInfo**](SerpYahooOrganicTaskGetRegularResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="yahooOrganicTaskGetAdvanced"></a>
# **yahooOrganicTaskGetAdvanced**
> SerpYahooOrganicTaskGetAdvancedResponseInfo yahooOrganicTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.yahoo_organic_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYahooOrganicTaskGetAdvancedResponseInfo**](SerpYahooOrganicTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="yahooOrganicTaskGetHtml"></a>
# **yahooOrganicTaskGetHtml**
> SerpYahooOrganicTaskGetHtmlResponseInfo yahooOrganicTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.yahoo_organic_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpYahooOrganicTaskGetHtmlResponseInfo**](SerpYahooOrganicTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="yahooOrganicLiveRegular"></a>
# **yahooOrganicLiveRegular**
> SerpYahooOrganicLiveRegularResponseInfo yahooOrganicLiveRegular()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_yahoo_organic_live_regular_request_info import List[Optional[SerpYahooOrganicLiveRegularRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.yahoo_organic_live_regular([SerpYahooOrganicLiveRegularRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpYahooOrganicLiveRegularRequestInfo]]&gt;**](List[Optional[SerpYahooOrganicLiveRegularRequestInfo]].md)|  | [optional] |



### Return type

[**SerpYahooOrganicLiveRegularResponseInfo**](SerpYahooOrganicLiveRegularResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="yahooOrganicLiveAdvanced"></a>
# **yahooOrganicLiveAdvanced**
> SerpYahooOrganicLiveAdvancedResponseInfo yahooOrganicLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_yahoo_organic_live_advanced_request_info import List[Optional[SerpYahooOrganicLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.yahoo_organic_live_advanced([SerpYahooOrganicLiveAdvancedRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpYahooOrganicLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpYahooOrganicLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpYahooOrganicLiveAdvancedResponseInfo**](SerpYahooOrganicLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="yahooOrganicLiveHtml"></a>
# **yahooOrganicLiveHtml**
> SerpYahooOrganicLiveHtmlResponseInfo yahooOrganicLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_yahoo_organic_live_html_request_info import List[Optional[SerpYahooOrganicLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.yahoo_organic_live_html([SerpYahooOrganicLiveHtmlRequestInfo(
                keyword="albert einstein",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpYahooOrganicLiveHtmlRequestInfo]]&gt;**](List[Optional[SerpYahooOrganicLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**SerpYahooOrganicLiveHtmlResponseInfo**](SerpYahooOrganicLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpBaiduLocations"></a>
# **serpBaiduLocations**
> SerpBaiduLocationsResponseInfo serpBaiduLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_baidu_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBaiduLocationsResponseInfo**](SerpBaiduLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpBaiduLocationsCountry"></a>
# **serpBaiduLocationsCountry**
> SerpBaiduLocationsCountryResponseInfo serpBaiduLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        country = "us"
        response = serp_api.serp_baidu_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBaiduLocationsCountryResponseInfo**](SerpBaiduLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpBaiduLanguages"></a>
# **serpBaiduLanguages**
> SerpBaiduLanguagesResponseInfo serpBaiduLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_baidu_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBaiduLanguagesResponseInfo**](SerpBaiduLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="baiduOrganicTaskPost"></a>
# **baiduOrganicTaskPost**
> SerpBaiduOrganicTaskPostResponseInfo baiduOrganicTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_baidu_organic_task_post_request_info import List[Optional[SerpBaiduOrganicTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.baidu_organic_task_post([SerpBaiduOrganicTaskPostRequestInfo(
                keyword="best iphone ever",
                priority=2,
                location_code=2156,
                tag="some_string_123",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpBaiduOrganicTaskPostRequestInfo]]&gt;**](List[Optional[SerpBaiduOrganicTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpBaiduOrganicTaskPostResponseInfo**](SerpBaiduOrganicTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="baiduOrganicTasksReady"></a>
# **baiduOrganicTasksReady**
> SerpBaiduOrganicTasksReadyResponseInfo baiduOrganicTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.baidu_organic_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBaiduOrganicTasksReadyResponseInfo**](SerpBaiduOrganicTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="baiduOrganicTasksFixed"></a>
# **baiduOrganicTasksFixed**
> SerpBaiduOrganicTasksFixedResponseInfo baiduOrganicTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.baidu_organic_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBaiduOrganicTasksFixedResponseInfo**](SerpBaiduOrganicTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="baiduOrganicTaskGetRegular"></a>
# **baiduOrganicTaskGetRegular**
> SerpBaiduOrganicTaskGetRegularResponseInfo baiduOrganicTaskGetRegular()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.baidu_organic_task_get_regular(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBaiduOrganicTaskGetRegularResponseInfo**](SerpBaiduOrganicTaskGetRegularResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="baiduOrganicTaskGetAdvanced"></a>
# **baiduOrganicTaskGetAdvanced**
> SerpBaiduOrganicTaskGetAdvancedResponseInfo baiduOrganicTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.baidu_organic_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBaiduOrganicTaskGetAdvancedResponseInfo**](SerpBaiduOrganicTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="baiduOrganicTaskGetHtml"></a>
# **baiduOrganicTaskGetHtml**
> SerpBaiduOrganicTaskGetHtmlResponseInfo baiduOrganicTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.baidu_organic_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpBaiduOrganicTaskGetHtmlResponseInfo**](SerpBaiduOrganicTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="naverOrganicTaskPost"></a>
# **naverOrganicTaskPost**
> SerpNaverOrganicTaskPostResponseInfo naverOrganicTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_naver_organic_task_post_request_info import List[Optional[SerpNaverOrganicTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.naver_organic_task_post([SerpNaverOrganicTaskPostRequestInfo(
                keyword="albert einstein",
                device="desktop",
                tag="some_string_123",
                postback_url="https://your-server.com/postbackscript.php",
                postback_data="regular",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpNaverOrganicTaskPostRequestInfo]]&gt;**](List[Optional[SerpNaverOrganicTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpNaverOrganicTaskPostResponseInfo**](SerpNaverOrganicTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="naverOrganicTasksReady"></a>
# **naverOrganicTasksReady**
> SerpNaverOrganicTasksReadyResponseInfo naverOrganicTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.naver_organic_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpNaverOrganicTasksReadyResponseInfo**](SerpNaverOrganicTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="naverOrganicTasksFixed"></a>
# **naverOrganicTasksFixed**
> SerpNaverOrganicTasksFixedResponseInfo naverOrganicTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.naver_organic_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpNaverOrganicTasksFixedResponseInfo**](SerpNaverOrganicTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="naverOrganicTaskGetRegular"></a>
# **naverOrganicTaskGetRegular**
> SerpNaverOrganicTaskGetRegularResponseInfo naverOrganicTaskGetRegular()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.naver_organic_task_get_regular(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpNaverOrganicTaskGetRegularResponseInfo**](SerpNaverOrganicTaskGetRegularResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="naverOrganicTaskGetAdvanced"></a>
# **naverOrganicTaskGetAdvanced**
> SerpNaverOrganicTaskGetAdvancedResponseInfo naverOrganicTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.naver_organic_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpNaverOrganicTaskGetAdvancedResponseInfo**](SerpNaverOrganicTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="naverOrganicTaskGetHtml"></a>
# **naverOrganicTaskGetHtml**
> SerpNaverOrganicTaskGetHtmlResponseInfo naverOrganicTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.naver_organic_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpNaverOrganicTaskGetHtmlResponseInfo**](SerpNaverOrganicTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpSeznamLocations"></a>
# **serpSeznamLocations**
> SerpSeznamLocationsResponseInfo serpSeznamLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_seznam_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpSeznamLocationsResponseInfo**](SerpSeznamLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpSeznamLocationsCountry"></a>
# **serpSeznamLocationsCountry**
> SerpSeznamLocationsCountryResponseInfo serpSeznamLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        country = "us"
        response = serp_api.serp_seznam_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpSeznamLocationsCountryResponseInfo**](SerpSeznamLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="serpSeznamLanguages"></a>
# **serpSeznamLanguages**
> SerpSeznamLanguagesResponseInfo serpSeznamLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.serp_seznam_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpSeznamLanguagesResponseInfo**](SerpSeznamLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="seznamOrganicTaskPost"></a>
# **seznamOrganicTaskPost**
> SerpSeznamOrganicTaskPostResponseInfo seznamOrganicTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_seznam_organic_task_post_request_info import List[Optional[SerpSeznamOrganicTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.seznam_organic_task_post([SerpSeznamOrganicTaskPostRequestInfo(
                keyword="albert einstein",
                location_code=2203,
                language_code="cs",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpSeznamOrganicTaskPostRequestInfo]]&gt;**](List[Optional[SerpSeznamOrganicTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpSeznamOrganicTaskPostResponseInfo**](SerpSeznamOrganicTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="seznamOrganicTasksReady"></a>
# **seznamOrganicTasksReady**
> SerpSeznamOrganicTasksReadyResponseInfo seznamOrganicTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.seznam_organic_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpSeznamOrganicTasksReadyResponseInfo**](SerpSeznamOrganicTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="seznamOrganicTasksFixed"></a>
# **seznamOrganicTasksFixed**
> SerpSeznamOrganicTasksFixedResponseInfo seznamOrganicTasksFixed()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.seznam_organic_tasks_fixed()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpSeznamOrganicTasksFixedResponseInfo**](SerpSeznamOrganicTasksFixedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="seznamOrganicTaskGetRegular"></a>
# **seznamOrganicTaskGetRegular**
> SerpSeznamOrganicTaskGetRegularResponseInfo seznamOrganicTaskGetRegular()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.seznam_organic_task_get_regular(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpSeznamOrganicTaskGetRegularResponseInfo**](SerpSeznamOrganicTaskGetRegularResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="seznamOrganicTaskGetAdvanced"></a>
# **seznamOrganicTaskGetAdvanced**
> SerpSeznamOrganicTaskGetAdvancedResponseInfo seznamOrganicTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.seznam_organic_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpSeznamOrganicTaskGetAdvancedResponseInfo**](SerpSeznamOrganicTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="seznamOrganicTaskGetHtml"></a>
# **seznamOrganicTaskGetHtml**
> SerpSeznamOrganicTaskGetHtmlResponseInfo seznamOrganicTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.seznam_organic_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpSeznamOrganicTaskGetHtmlResponseInfo**](SerpSeznamOrganicTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceExploreTaskPost"></a>
# **googleFinanceExploreTaskPost**
> SerpGoogleFinanceExploreTaskPostResponseInfo googleFinanceExploreTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_finance_explore_task_post_request_info import List[Optional[SerpGoogleFinanceExploreTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_explore_task_post([SerpGoogleFinanceExploreTaskPostRequestInfo(
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleFinanceExploreTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleFinanceExploreTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleFinanceExploreTaskPostResponseInfo**](SerpGoogleFinanceExploreTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceExploreTasksReady"></a>
# **googleFinanceExploreTasksReady**
> SerpGoogleFinanceExploreTasksReadyResponseInfo googleFinanceExploreTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_explore_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleFinanceExploreTasksReadyResponseInfo**](SerpGoogleFinanceExploreTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceExploreTaskGetAdvanced"></a>
# **googleFinanceExploreTaskGetAdvanced**
> SerpGoogleFinanceExploreTaskGetAdvancedResponseInfo googleFinanceExploreTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_finance_explore_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleFinanceExploreTaskGetAdvancedResponseInfo**](SerpGoogleFinanceExploreTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceExploreTaskGetHtml"></a>
# **googleFinanceExploreTaskGetHtml**
> SerpGoogleFinanceExploreTaskGetHtmlResponseInfo googleFinanceExploreTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_finance_explore_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleFinanceExploreTaskGetHtmlResponseInfo**](SerpGoogleFinanceExploreTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceExploreLiveAdvanced"></a>
# **googleFinanceExploreLiveAdvanced**
> SerpGoogleFinanceExploreLiveAdvancedResponseInfo googleFinanceExploreLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_finance_explore_live_advanced_request_info import List[Optional[SerpGoogleFinanceExploreLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_explore_live_advanced([SerpGoogleFinanceExploreLiveAdvancedRequestInfo(
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleFinanceExploreLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleFinanceExploreLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleFinanceExploreLiveAdvancedResponseInfo**](SerpGoogleFinanceExploreLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceExploreLiveHtml"></a>
# **googleFinanceExploreLiveHtml**
> SerpGoogleFinanceExploreLiveHtmlResponseInfo googleFinanceExploreLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_finance_explore_live_html_request_info import List[Optional[SerpGoogleFinanceExploreLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_explore_live_html([SerpGoogleFinanceExploreLiveHtmlRequestInfo(
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleFinanceExploreLiveHtmlRequestInfo]]&gt;**](List[Optional[SerpGoogleFinanceExploreLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleFinanceExploreLiveHtmlResponseInfo**](SerpGoogleFinanceExploreLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceMarketsTaskPost"></a>
# **googleFinanceMarketsTaskPost**
> SerpGoogleFinanceMarketsTaskPostResponseInfo googleFinanceMarketsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_finance_markets_task_post_request_info import List[Optional[SerpGoogleFinanceMarketsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_markets_task_post([SerpGoogleFinanceMarketsTaskPostRequestInfo(
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleFinanceMarketsTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleFinanceMarketsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleFinanceMarketsTaskPostResponseInfo**](SerpGoogleFinanceMarketsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceMarketsTasksReady"></a>
# **googleFinanceMarketsTasksReady**
> SerpGoogleFinanceMarketsTasksReadyResponseInfo googleFinanceMarketsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_markets_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleFinanceMarketsTasksReadyResponseInfo**](SerpGoogleFinanceMarketsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceMarketsTaskGetAdvanced"></a>
# **googleFinanceMarketsTaskGetAdvanced**
> SerpGoogleFinanceMarketsTaskGetAdvancedResponseInfo googleFinanceMarketsTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_finance_markets_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleFinanceMarketsTaskGetAdvancedResponseInfo**](SerpGoogleFinanceMarketsTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceMarketsTaskGetHtml"></a>
# **googleFinanceMarketsTaskGetHtml**
> SerpGoogleFinanceMarketsTaskGetHtmlResponseInfo googleFinanceMarketsTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_finance_markets_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleFinanceMarketsTaskGetHtmlResponseInfo**](SerpGoogleFinanceMarketsTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceMarketsLiveAdvanced"></a>
# **googleFinanceMarketsLiveAdvanced**
> SerpGoogleFinanceMarketsLiveAdvancedResponseInfo googleFinanceMarketsLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_finance_markets_live_advanced_request_info import List[Optional[SerpGoogleFinanceMarketsLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_markets_live_advanced([SerpGoogleFinanceMarketsLiveAdvancedRequestInfo(
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleFinanceMarketsLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleFinanceMarketsLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleFinanceMarketsLiveAdvancedResponseInfo**](SerpGoogleFinanceMarketsLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceMarketsLiveHtml"></a>
# **googleFinanceMarketsLiveHtml**
> SerpGoogleFinanceMarketsLiveHtmlResponseInfo googleFinanceMarketsLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_finance_markets_live_html_request_info import List[Optional[SerpGoogleFinanceMarketsLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_markets_live_html([SerpGoogleFinanceMarketsLiveHtmlRequestInfo(
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleFinanceMarketsLiveHtmlRequestInfo]]&gt;**](List[Optional[SerpGoogleFinanceMarketsLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleFinanceMarketsLiveHtmlResponseInfo**](SerpGoogleFinanceMarketsLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceQuoteTaskPost"></a>
# **googleFinanceQuoteTaskPost**
> SerpGoogleFinanceQuoteTaskPostResponseInfo googleFinanceQuoteTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_finance_quote_task_post_request_info import List[Optional[SerpGoogleFinanceQuoteTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_quote_task_post([SerpGoogleFinanceQuoteTaskPostRequestInfo(
                keyword=".DJI:INDEXDJX",
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleFinanceQuoteTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleFinanceQuoteTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleFinanceQuoteTaskPostResponseInfo**](SerpGoogleFinanceQuoteTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceQuoteTasksReady"></a>
# **googleFinanceQuoteTasksReady**
> SerpGoogleFinanceQuoteTasksReadyResponseInfo googleFinanceQuoteTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_quote_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleFinanceQuoteTasksReadyResponseInfo**](SerpGoogleFinanceQuoteTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceQuoteTaskGetAdvanced"></a>
# **googleFinanceQuoteTaskGetAdvanced**
> SerpGoogleFinanceQuoteTaskGetAdvancedResponseInfo googleFinanceQuoteTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_finance_quote_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleFinanceQuoteTaskGetAdvancedResponseInfo**](SerpGoogleFinanceQuoteTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceQuoteTaskGetHtml"></a>
# **googleFinanceQuoteTaskGetHtml**
> SerpGoogleFinanceQuoteTaskGetHtmlResponseInfo googleFinanceQuoteTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_finance_quote_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleFinanceQuoteTaskGetHtmlResponseInfo**](SerpGoogleFinanceQuoteTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceQuoteLiveAdvanced"></a>
# **googleFinanceQuoteLiveAdvanced**
> SerpGoogleFinanceQuoteLiveAdvancedResponseInfo googleFinanceQuoteLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_finance_quote_live_advanced_request_info import List[Optional[SerpGoogleFinanceQuoteLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_quote_live_advanced([SerpGoogleFinanceQuoteLiveAdvancedRequestInfo(
                keyword="CLW00:NYMEX",
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleFinanceQuoteLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleFinanceQuoteLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleFinanceQuoteLiveAdvancedResponseInfo**](SerpGoogleFinanceQuoteLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceQuoteLiveHtml"></a>
# **googleFinanceQuoteLiveHtml**
> SerpGoogleFinanceQuoteLiveHtmlResponseInfo googleFinanceQuoteLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_finance_quote_live_html_request_info import List[Optional[SerpGoogleFinanceQuoteLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_quote_live_html([SerpGoogleFinanceQuoteLiveHtmlRequestInfo(
                keyword="NASDAQ-100",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleFinanceQuoteLiveHtmlRequestInfo]]&gt;**](List[Optional[SerpGoogleFinanceQuoteLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleFinanceQuoteLiveHtmlResponseInfo**](SerpGoogleFinanceQuoteLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceTickerSearchTaskPost"></a>
# **googleFinanceTickerSearchTaskPost**
> SerpGoogleFinanceTickerSearchTaskPostResponseInfo googleFinanceTickerSearchTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_finance_ticker_search_task_post_request_info import List[Optional[SerpGoogleFinanceTickerSearchTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_ticker_search_task_post([SerpGoogleFinanceTickerSearchTaskPostRequestInfo(
                keyword="DJ",
                location_code=2840,
                language_name="English",
                priority=2,
                category="all",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleFinanceTickerSearchTaskPostRequestInfo]]&gt;**](List[Optional[SerpGoogleFinanceTickerSearchTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleFinanceTickerSearchTaskPostResponseInfo**](SerpGoogleFinanceTickerSearchTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceTickerSearchTasksReady"></a>
# **googleFinanceTickerSearchTasksReady**
> SerpGoogleFinanceTickerSearchTasksReadyResponseInfo googleFinanceTickerSearchTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_ticker_search_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleFinanceTickerSearchTasksReadyResponseInfo**](SerpGoogleFinanceTickerSearchTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceTickerSearchTaskGetAdvanced"></a>
# **googleFinanceTickerSearchTaskGetAdvanced**
> SerpGoogleFinanceTickerSearchTaskGetAdvancedResponseInfo googleFinanceTickerSearchTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = serp_api.google_finance_ticker_search_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**SerpGoogleFinanceTickerSearchTaskGetAdvancedResponseInfo**](SerpGoogleFinanceTickerSearchTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleFinanceTickerSearchLiveAdvanced"></a>
# **googleFinanceTickerSearchLiveAdvanced**
> SerpGoogleFinanceTickerSearchLiveAdvancedResponseInfo googleFinanceTickerSearchLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_serp_google_finance_ticker_search_live_advanced_request_info import List[Optional[SerpGoogleFinanceTickerSearchLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        serp_api = SerpApi(api_client)

        response = serp_api.google_finance_ticker_search_live_advanced([SerpGoogleFinanceTickerSearchLiveAdvancedRequestInfo(
                keyword="DJ",
                location_code=2840,
                language_name="English",
                category="all",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[SerpGoogleFinanceTickerSearchLiveAdvancedRequestInfo]]&gt;**](List[Optional[SerpGoogleFinanceTickerSearchLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**SerpGoogleFinanceTickerSearchLiveAdvancedResponseInfo**](SerpGoogleFinanceTickerSearchLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |