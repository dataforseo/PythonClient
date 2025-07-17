from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.link_element import LinkElement
from dataforseo_client.models.licenses_element import LicensesElement
from dataforseo_client.models.formats_element import FormatsElement
from dataforseo_client.models.authors_element import AuthorsElement
from dataforseo_client.models.period_covered import PeriodCovered
from dataforseo_client.models.dataset_description import DatasetDescription



class Dataset(BaseModel):
    """
    Dataset
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    dataset_id: Optional[StrictStr] = Field(default=None, description="ID of the dataset")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    image_url: Optional[StrictStr] = Field(default=None, description="URL of the image. the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available)")
    scholarly_citations_count: Optional[StrictInt] = Field(default=None, description="count of articles that refer to the dataset")
    scholarly_articles_url: Optional[StrictStr] = Field(default=None, description="url of scholarly articles. link to the list of scholarly articles on Google Scholar. example: https://scholar.google.com/scholar?q=%2210.6084%20m9%20figshare%207427933%20v1%22")
    unique_identifier: Optional[StrictStr] = Field(default=None, description="digital identifier of an object. unique digital identifier of the dataset. example: https://doi.org/10.5061/dryad.hmgqnk9m3")
    related_article: Optional[StrictStr] = Field(default=None, description="link to related article. link to the published article that is related to the dataset")
    links: Optional[List[Optional[LinkElement]]] = Field(default=None, description="sitelinks. the links shown below some of Google Dataset’s search results. if there are none, equals null")
    dataset_providers: Optional[List[Optional[LicensesElement]]] = Field(default=None, description="the list of institutions that provided the dataset")
    formats: Optional[List[Optional[FormatsElement]]] = Field(default=None, description="the list of file formats of the dataset")
    authors: Optional[List[Optional[AuthorsElement]]] = Field(default=None, description="the list of authors of the dataset")
    licenses: Optional[List[Optional[LicensesElement]]] = Field(default=None, description="the list of licenses issued to the dataset")
    updated_date: Optional[StrictStr] = Field(default=None, description="date and time when the result was last updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2022-11-27 02:00:00 +00:00")
    area_covered: Optional[List[Optional[StrictStr]]] = Field(default=None, description="the list of areas covered in the dataset. for example: Africa, Global")
    period_covered: Optional[PeriodCovered] = Field(default=None, description="period covered in the dataset")
    dataset_description: Optional[DatasetDescription] = Field(default=None, description="description of the dataset")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "dataset_id", 
        "title", 
        "image_url", 
        "scholarly_citations_count", 
        "scholarly_articles_url", 
        "unique_identifier", 
        "related_article", 
        "links", 
        "dataset_providers", 
        "formats", 
        "authors", 
        "licenses", 
        "updated_date", 
        "area_covered", 
        "period_covered", 
        "dataset_description", 
        ]

    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([
        ])

        _dict = {}

        _dict['type'] = self.type
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['dataset_id'] = self.dataset_id
        _dict['title'] = self.title
        _dict['image_url'] = self.image_url
        _dict['scholarly_citations_count'] = self.scholarly_citations_count
        _dict['scholarly_articles_url'] = self.scholarly_articles_url
        _dict['unique_identifier'] = self.unique_identifier
        _dict['related_article'] = self.related_article
        links_items = []
        if self.links:
            for _item in self.links:
                if _item:
                    links_items.append(_item.to_dict())
            _dict['links'] = links_items
        dataset_providers_items = []
        if self.dataset_providers:
            for _item in self.dataset_providers:
                if _item:
                    dataset_providers_items.append(_item.to_dict())
            _dict['dataset_providers'] = dataset_providers_items
        formats_items = []
        if self.formats:
            for _item in self.formats:
                if _item:
                    formats_items.append(_item.to_dict())
            _dict['formats'] = formats_items
        authors_items = []
        if self.authors:
            for _item in self.authors:
                if _item:
                    authors_items.append(_item.to_dict())
            _dict['authors'] = authors_items
        licenses_items = []
        if self.licenses:
            for _item in self.licenses:
                if _item:
                    licenses_items.append(_item.to_dict())
            _dict['licenses'] = licenses_items
        _dict['updated_date'] = self.updated_date
        _dict['area_covered'] = self.area_covered
        _dict['period_covered'] = self.period_covered.to_dict() if self.period_covered else None
        _dict['dataset_description'] = self.dataset_description.to_dict() if self.dataset_description else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "dataset_id": obj.get("dataset_id"),
            "title": obj.get("title"),
            "image_url": obj.get("image_url"),
            "scholarly_citations_count": obj.get("scholarly_citations_count"),
            "scholarly_articles_url": obj.get("scholarly_articles_url"),
            "unique_identifier": obj.get("unique_identifier"),
            "related_article": obj.get("related_article"),
            "links": [LinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "dataset_providers": [LicensesElement.from_dict(_item) for _item in obj["dataset_providers"]] if obj.get("dataset_providers") is not None else None,
            "formats": [FormatsElement.from_dict(_item) for _item in obj["formats"]] if obj.get("formats") is not None else None,
            "authors": [AuthorsElement.from_dict(_item) for _item in obj["authors"]] if obj.get("authors") is not None else None,
            "licenses": [LicensesElement.from_dict(_item) for _item in obj["licenses"]] if obj.get("licenses") is not None else None,
            "updated_date": obj.get("updated_date"),
            "area_covered": obj.get("area_covered"),
            "period_covered": PeriodCovered.from_dict(obj["period_covered"]) if obj.get("period_covered") is not None else None,
            "dataset_description": DatasetDescription.from_dict(obj["dataset_description"]) if obj.get("dataset_description") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj