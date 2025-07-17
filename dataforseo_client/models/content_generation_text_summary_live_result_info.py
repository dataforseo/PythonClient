from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentGenerationTextSummaryLiveResultInfo(BaseModel):
    """
    ContentGenerationTextSummaryLiveResultInfo
    """ # noqa: E501
    sentences: Optional[StrictInt] = Field(default=None, description="number of sentences found in the target text")
    paragraphs: Optional[StrictInt] = Field(default=None, description="number of paragraphs found in the target text")
    words: Optional[StrictInt] = Field(default=None, description="number of words found in the target text")
    characters_without_spaces: Optional[StrictInt] = Field(default=None, description="number of characters without spaces found in the target text")
    characters_with_spaces: Optional[StrictInt] = Field(default=None, description="number of characters with spaces found in the target text")
    words_per_sentence: Optional[StrictInt] = Field(default=None, description="average number of words per sentence in the target text")
    characters_per_word: Optional[StrictInt] = Field(default=None, description="average number of characters per word in the target text")
    vocabulary_density: Optional[StrictInt] = Field(default=None, description="vocabulary density of the target text")
    keyword_density: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="keyword density of the target text. contains most common words and their count")
    automated_readability_index: Optional[StrictInt] = Field(default=None, description="Automated Readability Index")
    coleman_liau_index: Optional[StrictInt] = Field(default=None, description="Coleman–Liau Index")
    flesch_kincaid_grade_level: Optional[StrictInt] = Field(default=None, description="Flesch–Kincaid Readability Index")
    smog_readability_index: Optional[StrictInt] = Field(default=None, description="SMOG Readability Index")
    spelling_errors: Optional[StrictInt] = Field(default=None, description="number of spelling errors found in the target text")
    grammar_errors: Optional[StrictInt] = Field(default=None, description="number of grammar errors found in the target text")
    __properties: ClassVar[List[str]] = [
        "sentences", 
        "paragraphs", 
        "words", 
        "characters_without_spaces", 
        "characters_with_spaces", 
        "words_per_sentence", 
        "characters_per_word", 
        "vocabulary_density", 
        "keyword_density", 
        "automated_readability_index", 
        "coleman_liau_index", 
        "flesch_kincaid_grade_level", 
        "smog_readability_index", 
        "spelling_errors", 
        "grammar_errors", 
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

        _dict['sentences'] = self.sentences
        _dict['paragraphs'] = self.paragraphs
        _dict['words'] = self.words
        _dict['characters_without_spaces'] = self.characters_without_spaces
        _dict['characters_with_spaces'] = self.characters_with_spaces
        _dict['words_per_sentence'] = self.words_per_sentence
        _dict['characters_per_word'] = self.characters_per_word
        _dict['vocabulary_density'] = self.vocabulary_density
        _dict['keyword_density'] = self.keyword_density
        _dict['automated_readability_index'] = self.automated_readability_index
        _dict['coleman_liau_index'] = self.coleman_liau_index
        _dict['flesch_kincaid_grade_level'] = self.flesch_kincaid_grade_level
        _dict['smog_readability_index'] = self.smog_readability_index
        _dict['spelling_errors'] = self.spelling_errors
        _dict['grammar_errors'] = self.grammar_errors
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sentences": obj.get("sentences"),
            "paragraphs": obj.get("paragraphs"),
            "words": obj.get("words"),
            "characters_without_spaces": obj.get("characters_without_spaces"),
            "characters_with_spaces": obj.get("characters_with_spaces"),
            "words_per_sentence": obj.get("words_per_sentence"),
            "characters_per_word": obj.get("characters_per_word"),
            "vocabulary_density": obj.get("vocabulary_density"),
            "keyword_density": obj.get("keyword_density"),
            "automated_readability_index": obj.get("automated_readability_index"),
            "coleman_liau_index": obj.get("coleman_liau_index"),
            "flesch_kincaid_grade_level": obj.get("flesch_kincaid_grade_level"),
            "smog_readability_index": obj.get("smog_readability_index"),
            "spelling_errors": obj.get("spelling_errors"),
            "grammar_errors": obj.get("grammar_errors"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj