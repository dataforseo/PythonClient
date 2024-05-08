# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.business_data_google_questions_and_answers_item import BusinessDataGoogleQuestionsAndAnswersItem
from dataforseo_client.models.items_without_answers import ItemsWithoutAnswers
from typing import Optional, Set
from typing_extensions import Self

class BusinessDataGoogleQuestionsAndAnswersTaskGetResultInfo(BaseModel):
    """
    BusinessDataGoogleQuestionsAndAnswersTaskGetResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword received in a POST array keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) this field will contain the cid parameter if you specified it in the keyword field when setting a task; example: cid:2946633002421908862 learn more about the parameter in this help center article")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain as specified in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id unique id of a local establishment; learn more about the identifier in this help center article")
    feature_id: Optional[StrictStr] = Field(default=None, description="unique identifier of the SERP feature")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="item types types of search engine results encountered in the items array; possible item types: google_business_question_item")
    items_without_answers: Optional[List[ItemsWithoutAnswers]] = Field(default=None, description="array of google business question items without answers")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of items in the items array")
    items: Optional[List[BusinessDataGoogleQuestionsAndAnswersItem]] = Field(default=None, description="array of items within google_business_question_item contains answers to the google business questions; the maximum number of answers returned for each question: 5 possible item types google_business_answer_element")
    __properties: ClassVar[List[str]] = ["keyword", "se_domain", "location_code", "language_code", "check_url", "datetime", "cid", "feature_id", "item_types", "items_without_answers", "items_count", "items"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BusinessDataGoogleQuestionsAndAnswersTaskGetResultInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in items_without_answers (list)
        _items = []
        if self.items_without_answers:
            for _item in self.items_without_answers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items_without_answers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # set to None if keyword (nullable) is None
        # and model_fields_set contains the field
        if self.keyword is None and "keyword" in self.model_fields_set:
            _dict['keyword'] = None

        # set to None if se_domain (nullable) is None
        # and model_fields_set contains the field
        if self.se_domain is None and "se_domain" in self.model_fields_set:
            _dict['se_domain'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if check_url (nullable) is None
        # and model_fields_set contains the field
        if self.check_url is None and "check_url" in self.model_fields_set:
            _dict['check_url'] = None

        # set to None if datetime (nullable) is None
        # and model_fields_set contains the field
        if self.datetime is None and "datetime" in self.model_fields_set:
            _dict['datetime'] = None

        # set to None if cid (nullable) is None
        # and model_fields_set contains the field
        if self.cid is None and "cid" in self.model_fields_set:
            _dict['cid'] = None

        # set to None if feature_id (nullable) is None
        # and model_fields_set contains the field
        if self.feature_id is None and "feature_id" in self.model_fields_set:
            _dict['feature_id'] = None

        # set to None if item_types (nullable) is None
        # and model_fields_set contains the field
        if self.item_types is None and "item_types" in self.model_fields_set:
            _dict['item_types'] = None

        # set to None if items_without_answers (nullable) is None
        # and model_fields_set contains the field
        if self.items_without_answers is None and "items_without_answers" in self.model_fields_set:
            _dict['items_without_answers'] = None

        # set to None if items_count (nullable) is None
        # and model_fields_set contains the field
        if self.items_count is None and "items_count" in self.model_fields_set:
            _dict['items_count'] = None

        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BusinessDataGoogleQuestionsAndAnswersTaskGetResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "se_domain": obj.get("se_domain"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "cid": obj.get("cid"),
            "feature_id": obj.get("feature_id"),
            "item_types": obj.get("item_types"),
            "items_without_answers": [ItemsWithoutAnswers.from_dict(_item) for _item in obj["items_without_answers"]] if obj.get("items_without_answers") is not None else None,
            "items_count": obj.get("items_count"),
            "items": [BusinessDataGoogleQuestionsAndAnswersItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None
        })
        return _obj


