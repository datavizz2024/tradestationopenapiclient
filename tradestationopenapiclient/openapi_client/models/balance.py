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
from openapi_client.models.balance_detail import BalanceDetail
from openapi_client.models.currency_detail import CurrencyDetail

class Balance(BaseModel):
    """
    Contains realtime balance information for a single account.
    """
    account_id: Optional[StrictStr] = Field(None, alias="AccountID", description="TradeStation Account ID.")
    account_type: Optional[StrictStr] = Field(None, alias="AccountType", description="The type of the account. Valid values are: `Cash`, `Margin`, `Futures` and `DVP`.")
    balance_detail: Optional[BalanceDetail] = Field(None, alias="BalanceDetail")
    buying_power: Optional[StrictStr] = Field(None, alias="BuyingPower", description="Buying Power available in the account.")
    cash_balance: Optional[StrictStr] = Field(None, alias="CashBalance", description="Indicates the value of real-time cash balance.")
    commission: Optional[StrictStr] = Field(None, alias="Commission", description="The brokerage commission cost and routing fees (if applicable) for a trade based on the number of shares or contracts.")
    currency_details: Optional[conlist(CurrencyDetail)] = Field(None, alias="CurrencyDetails", description="Only applies to futures. Collection of properties that describe balance characteristics in different currencies.")
    equity: Optional[StrictStr] = Field(None, alias="Equity", description="The real-time equity of the account.")
    market_value: Optional[StrictStr] = Field(None, alias="MarketValue", description="Market value of open positions.")
    todays_profit_loss: Optional[StrictStr] = Field(None, alias="TodaysProfitLoss", description="Unrealized profit and loss, for the current trading day, of all open positions.")
    uncleared_deposit: Optional[StrictStr] = Field(None, alias="UnclearedDeposit", description="The total of uncleared checks received by Tradestation for deposit.")
    __properties = ["AccountID", "AccountType", "BalanceDetail", "BuyingPower", "CashBalance", "Commission", "CurrencyDetails", "Equity", "MarketValue", "TodaysProfitLoss", "UnclearedDeposit"]

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
    def from_json(cls, json_str: str) -> Balance:
        """Create an instance of Balance from a JSON string"""
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
    def from_dict(cls, obj: dict) -> Balance:
        """Create an instance of Balance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Balance.parse_obj(obj)

        _obj = Balance.parse_obj({
            "account_id": obj.get("AccountID"),
            "account_type": obj.get("AccountType"),
            "balance_detail": BalanceDetail.from_dict(obj.get("BalanceDetail")) if obj.get("BalanceDetail") is not None else None,
            "buying_power": obj.get("BuyingPower"),
            "cash_balance": obj.get("CashBalance"),
            "commission": obj.get("Commission"),
            "currency_details": [CurrencyDetail.from_dict(_item) for _item in obj.get("CurrencyDetails")] if obj.get("CurrencyDetails") is not None else None,
            "equity": obj.get("Equity"),
            "market_value": obj.get("MarketValue"),
            "todays_profit_loss": obj.get("TodaysProfitLoss"),
            "uncleared_deposit": obj.get("UnclearedDeposit")
        })
        return _obj


