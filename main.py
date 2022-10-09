import quantlib.data_utils as du
import quantlib.general_utils as gu
import json

"""
df, instruments = du.get_sp500_df()
df = du.extend_dataframe(traded=instruments, df=df)
gu.save_file("./Data/data.obj", (df, instruments))
"""

df, instruments = gu.load_file("./Data/data.obj")
print(df, instruments)

with open("./subsystems/LBMOM/config.json", "w") as f:
    json.dump({"instruments": instruments}, f, indent=4)