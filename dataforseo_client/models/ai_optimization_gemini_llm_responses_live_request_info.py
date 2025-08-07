from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.llm_message_chain_item import LlmMessageChainItem



class AiOptimizationGeminiLlmResponsesLiveRequestInfo(BaseModel):
    """
    AiOptimizationGeminiLlmResponsesLiveRequestInfo
    """ # noqa: E501
    user_prompt: Optional[StrictStr] = Field(default=None, description="prompt for the AI model. required field. the question or task you want to send to the AI model;. you can specify up to 500 characters in the user_prompt field")
    model_name: Optional[StrictStr] = Field(default=None, description="name of the AI model. required field. model_nameconsists of the actual model name and version name;. if the basic model name is specified, its latest version will be set by default;. for example, if gemini-1.5-pro is specified, the gemini-1.5-pro-002 will be set as model_name automatically;. you can receive the list of available LLM models by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/gemini/llm_responses/models")
    max_output_tokens: Optional[StrictInt] = Field(default=None, description="maximum number of tokens in the AI response. optional field. minimum value: 1. maximum value: 2048. default value: 2048. Note: when web_search is set to true, the output token count may exceed the specified max_output_tokens limit")
    temperature: Optional[StrictFloat] = Field(default=None, description="randomness of the AI response. optional field. higher values make output more diverse. lower values make output more focused. minimum value: 0. maximum value: 2. default value: 1.3")
    top_p: Optional[StrictFloat] = Field(default=None, description="diversity of the AI response. optional field. controls diversity of the response by limiting token selection. minimum value: 0. maximum value: 1. default value: 0.9")
    web_search: Optional[StrictBool] = Field(default=None, description="enable web search for current information. optional field. when enabled, the AI model can access and cite current web information;. Note: refer to the Models endpoint for a list of models that support web_search;. default value: false;. The cost of the parameter can be calculated on the Pricing page")
    system_message: Optional[StrictStr] = Field(default=None, description="instructions for the AI behavior. optional field. defines the AI’s role, tone, or specific behavior. you can specify up to 500 characters in the system_message field")
    message_chain: Optional[List[Optional[LlmMessageChainItem]]] = Field(default=None, description="conversation history. optional field. array of message objects representing previous conversation turns;. each object must contain:. role string with either user or ai role;. message string with message content (max 500 characters);. you can specify maximum of 10 message objects in the array;. Note: for Perplexity models, messages must strictly alternate between user and AI roles (user → ai);. example:. 'message_chain': [{'role':'user','message':'Hello, what’s up?'},{'role':'ai','message':'Hello! I’m doing well, thank you. How can I assist you today?'}]")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "user_prompt", 
        "model_name", 
        "max_output_tokens", 
        "temperature", 
        "top_p", 
        "web_search", 
        "system_message", 
        "message_chain", 
        "tag", 
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

        _dict['user_prompt'] = self.user_prompt
        _dict['model_name'] = self.model_name
        _dict['max_output_tokens'] = self.max_output_tokens
        _dict['temperature'] = self.temperature
        _dict['top_p'] = self.top_p
        _dict['web_search'] = self.web_search
        _dict['system_message'] = self.system_message
        message_chain_items = []
        if self.message_chain:
            for _item in self.message_chain:
                if _item:
                    message_chain_items.append(_item.to_dict())
            _dict['message_chain'] = message_chain_items
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "user_prompt": obj.get("user_prompt"),
            "model_name": obj.get("model_name"),
            "max_output_tokens": obj.get("max_output_tokens"),
            "temperature": obj.get("temperature"),
            "top_p": obj.get("top_p"),
            "web_search": obj.get("web_search"),
            "system_message": obj.get("system_message"),
            "message_chain": [LlmMessageChainItem.from_dict(_item) for _item in obj["message_chain"]] if obj.get("message_chain") is not None else None,
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj