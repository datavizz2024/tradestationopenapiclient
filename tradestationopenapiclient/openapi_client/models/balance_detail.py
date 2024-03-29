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

class BalanceDetail(BaseModel):
    """
    Contains real-time balance information that varies according to account type.
    """
    cost_of_positions: Optional[StrictStr] = Field(None, alias="CostOfPositions", description="(Equities) The cost used to calculate today's P/L.")
    day_trade_excess: Optional[StrictStr] = Field(None, alias="DayTradeExcess", description="(Equities): (Buying Power Available - Buying Power Used) / Buying Power Multiplier. (Futures): (Cash + UnrealizedGains) - Buying Power Used.")
    day_trade_margin: Optional[StrictStr] = Field(None, alias="DayTradeMargin", description="(Futures) Money field representing the current total amount of futures day trade margin.")
    day_trade_open_order_margin: Optional[StrictStr] = Field(None, alias="DayTradeOpenOrderMargin", description="(Futures) Money field representing the current amount of money reserved for open orders.")
    day_trades: Optional[StrictStr] = Field(None, alias="DayTrades", description="(Equities) The number of day trades placed in the account within the previous 4 trading days. A day trade refers to buying then selling or selling short then buying to cover the same security on the same trading day.")
    initial_margin: Optional[StrictStr] = Field(None, alias="InitialMargin", description="(Futures) Sum (Initial Margins of all positions in the given account).")
    maintenance_margin: Optional[StrictStr] = Field(None, alias="MaintenanceMargin", description="(Futures) Indicates the value of real-time maintenance margin.")
    maintenance_rate: Optional[StrictStr] = Field(None, alias="MaintenanceRate", description="Maintenance Margin Rate.")
    margin_requirement: Optional[StrictStr] = Field(None, alias="MarginRequirement", description="(Futures) Indicates the value of real-time account margin requirement.")
    open_order_margin: Optional[StrictStr] = Field(None, alias="OpenOrderMargin", description="(Futures) The dollar amount of Open Order Margin for the given futures account.")
    option_buying_power: Optional[StrictStr] = Field(None, alias="OptionBuyingPower", description="(Equities) The intraday buying power for options.")
    options_market_value: Optional[StrictStr] = Field(None, alias="OptionsMarketValue", description="(Equities) Market value of open positions.")
    overnight_buying_power: Optional[StrictStr] = Field(None, alias="OvernightBuyingPower", description="(Equities) Overnight Buying Power (Regulation T) at the start of the trading day.")
    realized_profit_loss: Optional[StrictStr] = Field(None, alias="RealizedProfitLoss", description="Indicates the value of real-time account realized profit or loss.")
    required_margin: Optional[StrictStr] = Field(None, alias="RequiredMargin", description="(Equities) Total required margin for all held positions.")
    security_on_deposit: Optional[StrictStr] = Field(None, alias="SecurityOnDeposit", description="(Futures) The value of special securities that are deposited by the customer with the clearing firm for the sole purpose of increasing purchasing power in their trading account. This number will be reset daily by the account balances clearing file. The entire value of this field will increase purchasing power.")
    today_real_time_trade_equity: Optional[StrictStr] = Field(None, alias="TodayRealTimeTradeEquity", description="(Futures) The unrealized P/L for today. Unrealized P/L - BODOpenTradeEquity.")
    trade_equity: Optional[StrictStr] = Field(None, alias="TradeEquity", description="(Futures) The dollar amount of unrealized profit and loss for the given futures account. Same value as RealTimeUnrealizedGains.")
    unrealized_profit_loss: Optional[StrictStr] = Field(None, alias="UnrealizedProfitLoss", description="Indicates the value of real-time account unrealized profit or loss.")
    unsettled_funds: Optional[StrictStr] = Field(None, alias="UnsettledFunds", description="Unsettled Funds are funds that have been closed but not settled.")
    __properties = ["CostOfPositions", "DayTradeExcess", "DayTradeMargin", "DayTradeOpenOrderMargin", "DayTrades", "InitialMargin", "MaintenanceMargin", "MaintenanceRate", "MarginRequirement", "OpenOrderMargin", "OptionBuyingPower", "OptionsMarketValue", "OvernightBuyingPower", "RealizedProfitLoss", "RequiredMargin", "SecurityOnDeposit", "TodayRealTimeTradeEquity", "TradeEquity", "UnrealizedProfitLoss", "UnsettledFunds"]

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
    def from_json(cls, json_str: str) -> BalanceDetail:
        """Create an instance of BalanceDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BalanceDetail:
        """Create an instance of BalanceDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BalanceDetail.parse_obj(obj)

        _obj = BalanceDetail.parse_obj({
            "cost_of_positions": obj.get("CostOfPositions"),
            "day_trade_excess": obj.get("DayTradeExcess"),
            "day_trade_margin": obj.get("DayTradeMargin"),
            "day_trade_open_order_margin": obj.get("DayTradeOpenOrderMargin"),
            "day_trades": obj.get("DayTrades"),
            "initial_margin": obj.get("InitialMargin"),
            "maintenance_margin": obj.get("MaintenanceMargin"),
            "maintenance_rate": obj.get("MaintenanceRate"),
            "margin_requirement": obj.get("MarginRequirement"),
            "open_order_margin": obj.get("OpenOrderMargin"),
            "option_buying_power": obj.get("OptionBuyingPower"),
            "options_market_value": obj.get("OptionsMarketValue"),
            "overnight_buying_power": obj.get("OvernightBuyingPower"),
            "realized_profit_loss": obj.get("RealizedProfitLoss"),
            "required_margin": obj.get("RequiredMargin"),
            "security_on_deposit": obj.get("SecurityOnDeposit"),
            "today_real_time_trade_equity": obj.get("TodayRealTimeTradeEquity"),
            "trade_equity": obj.get("TradeEquity"),
            "unrealized_profit_loss": obj.get("UnrealizedProfitLoss"),
            "unsettled_funds": obj.get("UnsettledFunds")
        })
        return _obj


