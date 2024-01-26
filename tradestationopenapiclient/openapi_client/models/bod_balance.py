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
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.bod_balance_detail import BODBalanceDetail
from openapi_client.models.bod_currency_detail import BODCurrencyDetail

class BODBalance(BaseModel):
    """
    Contains beginning of day balance information for a single account.
    """
    account_id: Optional[StrictStr] = Field(None, alias="AccountID", description="TradeStation Account ID.")
    account_type: Optional[StrictStr] = Field(None, alias="AccountType", description="The account type of this account.")
    balance_detail: Optional[BODBalanceDetail] = Field(None, alias="BalanceDetail")
    currency_details: Optional[conlist(BODCurrencyDetail)] = Field(None, alias="CurrencyDetails", description="Only applies to futures. Contains beginning of day currency detail information which varies according to account type.")
    __properties = ["AccountID", "AccountType", "BalanceDetail", "CurrencyDetails"]

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
    def from_json(cls, json_str: str) -> BODBalance:
        """Create an instance of BODBalance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of balance_detail
        if self.balance_detail:
            _dict['BalanceDetail'] = self.balance_detail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in currency_details (list)
        _items = []
        if self.currency_details:
            for _item in self.currency_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['CurrencyDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BODBalance:
        """Create an instance of BODBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BODBalance.parse_obj(obj)

        _obj = BODBalance.parse_obj({
            "account_id": obj.get("AccountID"),
            "account_type": obj.get("AccountType"),
            "balance_detail": BODBalanceDetail.from_dict(obj.get("BalanceDetail")) if obj.get("BalanceDetail") is not None else None,
            "currency_details": [BODCurrencyDetail.from_dict(_item) for _item in obj.get("CurrencyDetails")] if obj.get("CurrencyDetails") is not None else None
        })
        return _obj


