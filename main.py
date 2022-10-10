import quantlib.data_utils as du
import quantlib.general_utils as gu
import json
from subsystems.LBMOM.subsys import Lbmom
from dateutil.relativedelta import relativedelta

"""
df, instruments = du.get_sp500_df()
df = du.extend_dataframe(traded=instruments, df=df)
gu.save_file("./Data/data.obj", (df, instruments))
"""

df, instruments = gu.load_file("./Data/data.obj")
print(df, instruments)

sim_start = df.index[-1] - relativedelta(years=5)
VOL_TARGET = 0.20

strat = Lbmom(instruments_config="./subsystems/LBMOM/config.json", historical_df=df, simulation_start=sim_start, vol_target=VOL_TARGET)
strat.get_subsys_pos()