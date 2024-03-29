# coding: utf-8

"""
    

    # Authentication For more information on authorization and gaining an access/refresh token, please visit: [Authentication](/docs/fundamentals/authentication/auth-overview). <SecurityDefinitions /> 

    The version of the OpenAPI document: 
    Contact: ClientServices@tradestation.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, conlist
from openapi_client.models.time_activation_rules import TimeActivationRules

class TimeActivationRulesReplace(BaseModel):
    """
    Advanced option for an order. The date portion is not used for a Time Activation rule and is returned as \"0001-01-01\".
    """
    clear_all: Optional[StrictBool] = Field(None, alias="ClearAll", description="If 'True', removes all activation rules when replacing the order and ignores any rules sent in `Rules`.")
    rules: Optional[conlist(TimeActivationRules)] = Field(None, alias="Rules")
    __properties = ["ClearAll", "Rules"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TimeActivationRulesReplace:
        """Create an instance of TimeActivationRulesReplace from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimeActivationRulesReplace:
        """Create an instance of TimeActivationRulesReplace from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimeActivationRulesReplace.parse_obj(obj)

        _obj = TimeActivationRulesReplace.parse_obj({
            "clear_all": obj.get("ClearAll"),
            "rules": [TimeActivationRules.from_dict(_item) for _item in obj.get("Rules")] if obj.get("Rules") is not None else None
        })
        return _obj


