# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.trustpilot_review_search_business_data_serp_element_item import TrustpilotReviewSearchBusinessDataSerpElementItem

class TestTrustpilotReviewSearchBusinessDataSerpElementItem(unittest.TestCase):
    """TrustpilotReviewSearchBusinessDataSerpElementItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrustpilotReviewSearchBusinessDataSerpElementItem:
        """Test TrustpilotReviewSearchBusinessDataSerpElementItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrustpilotReviewSearchBusinessDataSerpElementItem`
        """
        model = TrustpilotReviewSearchBusinessDataSerpElementItem()
        if include_optional:
            return TrustpilotReviewSearchBusinessDataSerpElementItem(
                rank_group = 56,
                rank_absolute = 56,
                position = '',
                url = '',
                rating = dataforseo_client.models.rating_info.RatingInfo(
                    rating_type = '', 
                    value = 1.337, 
                    votes_count = 56, 
                    rating_max = 56, ),
                verified = True,
                language = '',
                timestamp = '',
                title = '',
                review_text = '',
                review_images = [
                    ''
                    ],
                user_profile = dataforseo_client.models.business_data_user_profile_info.BusinessDataUserProfileInfo(
                    name = '', 
                    url = '', 
                    image_url = '', 
                    location = '', 
                    reviews_count = 56, ),
                responses = [
                    dataforseo_client.models.review_response_item_info.ReviewResponseItemInfo(
                        title = '', 
                        text = '', 
                        timestamp = '', )
                    ]
            )
        else:
            return TrustpilotReviewSearchBusinessDataSerpElementItem(
        )
        """

    def testTrustpilotReviewSearchBusinessDataSerpElementItem(self):
        """Test TrustpilotReviewSearchBusinessDataSerpElementItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
