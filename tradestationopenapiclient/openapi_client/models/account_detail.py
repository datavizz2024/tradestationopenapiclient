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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt

class AccountDetail(BaseModel):
    """
    (Equities) Contains detailed information about specific accounts depending on account type.
    """
    crypto_enabled: Optional[StrictBool] = Field(None, alias="CryptoEnabled", description="Identifies whether equity account is enabled for crypto trading.")
    day_trading_qualified: Optional[StrictBool] = Field(None, alias="DayTradingQualified", description="Indicates if the account is qualified to day trade as per compliance suitability in TradeStation. An account that is not Day Trading Qualified is subject to restrictions that will not allow it to become a pattern day trader.")
    enrolled_in_reg_t_program: Optional[StrictBool] = Field(None, alias="EnrolledInRegTProgram", description="For internal use only.  Identifies whether accounts is enrolled in Reg T program.")
    is_stock_locate_eligible: Optional[StrictBool] = Field(None, alias="IsStockLocateEligible", description="True if this account is stock locate eligible; otherwise, false.")
    option_approval_level: Optional[StrictInt] = Field(None, alias="OptionApprovalLevel", description="Valid values are: `0`, `1`, `2`, `3`, `4`, and `5`. (Equities) The option approval level will determine what options strategies you will be able to employ in the account. In general terms, the levels are defined as follows: Level 0 - No options trading allowed Level 1 - Writing of Covered Calls, Buying Protective Puts Level 2 - Level 1 + Buying Calls, Buying Puts, Writing Covered Puts Level 3 - level 2+ Stock Option Spreads, Index Option Spreads, Butterfly Spreads, Condor Spreads, Iron Butterfly Spreads, Iron Condor Spreads Level 4 - Level 3 + Writing of Naked Puts (Stock Options) Level 5 - Level 4 + Writing of Naked Puts (Index Options), Writing of Naked Calls (Stock Options), Writing of Naked Calls (Index Options)")
    pattern_day_trader: Optional[StrictBool] = Field(None, alias="PatternDayTrader", description="(Equities) Indicates whether you are considered a pattern day trader. As per FINRA rules, you will be considered a pattern day trader if you trade 4 or more times in 5 business days and your day-trading activities are greater than 6 percent of your total trading activity for that same five-day period. A pattern day trader must maintain a minimum equity of $25,000 on any day that the customer day trades. If the account falls below the $25,000 requirement, the pattern day trader will not be permitted to day trade until the account is restored to the $25,000 minimum equity level.")
    requires_buying_power_warning: Optional[StrictBool] = Field(None, alias="RequiresBuyingPowerWarning", description="For internal use only. Identifies whether account is enrolled in the margin buying power warning program to receive alerts prior to placing an order which would exceed their buying power.")
    __properties = ["CryptoEnabled", "DayTradingQualified", "EnrolledInRegTProgram", "IsStockLocateEligible", "OptionApprovalLevel", "PatternDayTrader", "RequiresBuyingPowerWarning"]

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
    def from_json(cls, json_str: str) -> AccountDetail:
        """Create an instance of AccountDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountDetail:
        """Create an instance of AccountDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountDetail.parse_obj(obj)

        _obj = AccountDetail.parse_obj({
            "crypto_enabled": obj.get("CryptoEnabled"),
            "day_trading_qualified": obj.get("DayTradingQualified"),
            "enrolled_in_reg_t_program": obj.get("EnrolledInRegTProgram"),
            "is_stock_locate_eligible": obj.get("IsStockLocateEligible"),
            "option_approval_level": obj.get("OptionApprovalLevel"),
            "pattern_day_trader": obj.get("PatternDayTrader"),
            "requires_buying_power_warning": obj.get("RequiresBuyingPowerWarning")
        })
        return _obj


