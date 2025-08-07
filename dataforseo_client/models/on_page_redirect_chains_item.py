from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.on_page_redirect_link_item import OnPageRedirectLinkItem



class OnPageRedirectChainsItem(BaseModel):
    """
    OnPageRedirectChainsItem
    """ # noqa: E501
    is_redirect_loop: Optional[StrictBool] = Field(default=None, description="indicates if redirects in chain start and end at the same URL. if true, the last URL from the chain redirects back to the original URL")
    chain: Optional[List[Optional[OnPageRedirectLinkItem]]] = Field(default=None, description="contains links that form a chain")
    __properties: ClassVar[List[str]] = [
        "is_redirect_loop", 
        "chain", 
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

        _dict['is_redirect_loop'] = self.is_redirect_loop
        chain_items = []
        if self.chain:
            for _item in self.chain:
                if _item:
                    chain_items.append(_item.to_dict())
            _dict['chain'] = chain_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "is_redirect_loop": obj.get("is_redirect_loop"),
            "chain": [OnPageRedirectLinkItem.from_dict(_item) for _item in obj["chain"]] if obj.get("chain") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj