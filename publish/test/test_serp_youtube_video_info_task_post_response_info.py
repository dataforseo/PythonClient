# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.serp_youtube_video_info_task_post_response_info import SerpYoutubeVideoInfoTaskPostResponseInfo

class TestSerpYoutubeVideoInfoTaskPostResponseInfo(unittest.TestCase):
    """SerpYoutubeVideoInfoTaskPostResponseInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SerpYoutubeVideoInfoTaskPostResponseInfo:
        """Test SerpYoutubeVideoInfoTaskPostResponseInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SerpYoutubeVideoInfoTaskPostResponseInfo`
        """
        model = SerpYoutubeVideoInfoTaskPostResponseInfo()
        if include_optional:
            return SerpYoutubeVideoInfoTaskPostResponseInfo(
                version = '',
                status_code = 56,
                status_message = '',
                time = '',
                cost = 1.337,
                tasks_count = 56,
                tasks_error = 56,
                tasks = [
                    dataforseo_client.models.serp_youtube_video_info_task_post_task_info.SerpYoutubeVideoInfoTaskPostTaskInfo()
                    ]
            )
        else:
            return SerpYoutubeVideoInfoTaskPostResponseInfo(
        )
        """

    def testSerpYoutubeVideoInfoTaskPostResponseInfo(self):
        """Test SerpYoutubeVideoInfoTaskPostResponseInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()