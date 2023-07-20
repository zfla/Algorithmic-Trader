import quantlib.data_utils as du
import quantlib.general_utils as gu
import json
from subsystems.LBMOM.subsys import Lbmom
from dateutil.relativedelta import relativedelta

from brokerage.oanda.oanda import Oanda

"""
df, instruments = du.get_sp500_df()
df = du.extend_dataframe(traded=instruments, df=df)
gu.save_file("./Data/data.obj", (df, instruments))
"""

with open("config/auth_config.json", "r") as f:
    auth_config = json.load(f)

df, instruments = gu.load_file("./Data/data.obj")
#print(df, instruments)
sim_start = df.index[-1] - relativedelta(years=5)
VOL_TARGET = 0.20

trade_client = Oanda(auth_config=auth_config).get_trade_client()
summary = trade_client.get_account_summary()
capital = trade_client.get_account_capital()
details = trade_client.get_account_instruments()
print(details)
exit()

strat = Lbmom(instruments_config="./subsystems/LBMOM/config.json", historical_df=df, simulation_start=sim_start, vol_target=VOL_TARGET)
strat.get_subsys_pos()




