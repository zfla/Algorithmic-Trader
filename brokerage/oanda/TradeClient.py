# interacts with the Oanda client to make, update, read, or delete orders
import json
import oandapyV20
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.positions as positions
import oandapyV20.endpoints.instruments as instruments

class TradeClient():
    def __init__(self, auth_config):
        self.id = auth_config["oan_acc_id"]
        self.token = auth_config["oan_token"]
        self.env = auth_config["oan_env"]
        self.client = oandapyV20.API(access_token=self.token, environment=self.env)

    """
    we want
    1. capital
    2. pos
    3. to submit orders
    4. get ohlcv data
    """

   # wrapper functions 

    def get_account_details(self):
        try:
            return self.client.request(accounts.AccountDetails(self.id))['account']
        except Exception as err:
            print(err)
    
    def get_account_summary(self):
        try:
            return self.client.request(accounts.AccountSummary(self.id))["account"]
        except Exception as err:
            print(err)

    def get_account_capital(self):
        try:
            return float(self.get_account_summary()["NAV"])
        except Exception as err:
            pass

    def get_account_positions(self):
        position_data = self.get_account_details()["positions"]
        positions = {}
        for entry in position_data:
            instrument = entry['instrument']
            long_pos = int(entry["long"]["units"])
            short_pos = int(entry["short"]["units"])
            net_pos = long_pos + short_pos
            if net_pos != 0:
                positions[instrument] = net_pos
        return positions

    def get_account_instruments(self):
        try:
            r = self.client.request(accounts.AccountInstruments(accountID=self.id))["instruments"]
            instruments = {}
            currencies, cfds, metals = [],[],[]
            for inst in r:
                inst_name = inst["name"]
                inst_type = inst["type"]
                instruments["inst_name"] = {
                    "type" : inst_type,
                    "tag" : inst["tags"][0]["name "]
                }
                if inst_type == "CFD":
                    cfds.append(inst_name)

                elif inst_type == "CURRENCY":
                    currencies.append(inst_name)

                elif inst_type == "METAL":
                    metals.append(inst_name)
                
                else:
                    print("unknown type", inst_name)
                    exit()
            return instruments, currencies, cfds, metals
        except Exception as err:
            pass

    def get_account_trades(self):
        try:
            trade_data = self.client.request(trades.OpenTrades(accountID=self.id))
            return trade_data
        except Exception as err:
            pass
    
    def get_account_orders(self):
        pass

    def get_ohlcv(self, instrument, count, granularity):
        pass

    def market_order(self, inst, order_config={}):
        pass


