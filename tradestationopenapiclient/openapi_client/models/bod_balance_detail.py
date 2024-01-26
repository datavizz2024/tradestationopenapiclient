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
from pydantic import BaseModel, Field, StrictStr

class BODBalanceDetail(BaseModel):
    """
    Contains detailed beginning of day balance information which varies according to account type.
    """
    account_balance: Optional[StrictStr] = Field(None, alias="AccountBalance", description="Only applies to equities. The amount of cash in the account at the beginning of the day.")
    cash_available_to_withdraw: Optional[StrictStr] = Field(None, alias="CashAvailableToWithdraw", description="Beginning of day value for cash available to withdraw.")
    day_trades: Optional[StrictStr] = Field(None, alias="DayTrades", description="Only applies to equities. The number of day trades placed in the account within the previous 4 trading days. A day trade refers to buying then selling or selling short then buying to cover the same security on the same trading day.")
    day_trading_marginable_buying_power: Optional[StrictStr] = Field(None, alias="DayTradingMarginableBuyingPower", description="Only applies to equities. The Intraday Buying Power with which the account started the trading day.")
    equity: Optional[StrictStr] = Field(None, alias="Equity", description="The total amount of equity with which you started the current trading day.")
    net_cash: Optional[StrictStr] = Field(None, alias="NetCash", description="The amount of cash in the account at the beginning of the day.")
    open_trade_equity: Optional[StrictStr] = Field(None, alias="OpenTradeEquity", description="Only applies to futures. Unrealized profit and loss at the beginning of the day.")
    option_buying_power: Optional[StrictStr] = Field(None, alias="OptionBuyingPower", description="Only applies to equities. Option buying power at the start of the trading day.")
    option_value: Optional[StrictStr] = Field(None, alias="OptionValue", description="Only applies to equities. Intraday liquidation value of option positions.")
    overnight_buying_power: Optional[StrictStr] = Field(None, alias="OvernightBuyingPower", description="Only applies to equities. Real-time Overnight Marginable Equities Buying Power.")
    security_on_deposit: Optional[StrictStr] = Field(None, alias="SecurityOnDeposit", description="(Futures) The value of special securities that are deposited by the customer with the clearing firm for the sole purpose of increasing purchasing power in their trading account.")
    __properties = ["AccountBalance", "CashAvailableToWithdraw", "DayTrades", "DayTradingMarginableBuyingPower", "Equity", "NetCash", "OpenTradeEquity", "OptionBuyingPower", "OptionValue", "OvernightBuyingPower", "SecurityOnDeposit"]

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
    def from_json(cls, json_str: str) -> BODBalanceDetail:
        """Create an instance of BODBalanceDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BODBalanceDetail:
        """Create an instance of BODBalanceDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BODBalanceDetail.parse_obj(obj)

        _obj = BODBalanceDetail.parse_obj({
            "account_balance": obj.get("AccountBalance"),
            "cash_available_to_withdraw": obj.get("CashAvailableToWithdraw"),
            "day_trades": obj.get("DayTrades"),
            "day_trading_marginable_buying_power": obj.get("DayTradingMarginableBuyingPower"),
            "equity": obj.get("Equity"),
            "net_cash": obj.get("NetCash"),
            "open_trade_equity": obj.get("OpenTradeEquity"),
            "option_buying_power": obj.get("OptionBuyingPower"),
            "option_value": obj.get("OptionValue"),
            "overnight_buying_power": obj.get("OvernightBuyingPower"),
            "security_on_deposit": obj.get("SecurityOnDeposit")
        })
        return _obj


