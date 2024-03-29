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
from pydantic import BaseModel, Field, conlist
from openapi_client.models.account import Account


class Accounts(BaseModel):
    """
    Contains brokerage account information for the identified user.
    """

    accounts: conlist(Account)
    __properties = ["Accounts"]

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
    def from_json(cls, json_str: str) -> Accounts:
        """Create an instance of Accounts from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in accounts (list)
        _items = []
        if self.accounts:
            for _item in self.accounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict["Accounts"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Accounts:
        """Create an instance of Accounts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Accounts.parse_obj(obj)

        _obj = Accounts.parse_obj(
            {
                "accounts": [Account.from_dict(_item) for _item in obj.get("Accounts")]
                if obj.get("Accounts") is not None
                else None
            }
        )
        return _obj
