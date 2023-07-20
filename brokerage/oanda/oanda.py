# oanda key : a28dbdc06441ad14d72e2dd2b14f4df0-500db49525ad5bba7a0559f54da052aa
# oanda id : 101-004-26388245-001

from brokerage.oanda.TradeClient import TradeClient

class Oanda():
    def __init__(self, auth_config={}):
        self.trade_client = TradeClient(auth_config=auth_config)

    def get_service_client(self):
        pass

    def get_trade_client(self):
        return self.trade_client