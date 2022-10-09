# function to get data and indicators specific to strategy
# function to run backtest and get positions
import json

class Lbmom:
    def __init__(self, instruments_config, historical_df, simulation_start, vol_target):
        self.pairs = [(182, 249), (134, 188), (148, 266), (118, 150), (58, 149), (131, 180), (202, 272), (40, 123), (114, 119), (146, 151), (128, 279), (183, 209), (157, 230), (64, 286), (206, 281), (69, 193), (163, 280), (207, 256), (72, 154), (146, 250), (266, 281)]
        self.historical_df = historical_df
        self.simulation_start = simulation_start
        self.vol_target = vol_target
        with open(instruments_config) as f:
            self.instruments_config = json.load(f)
        self.sysname = "LBMOM"

    def extend_historicals(self, instruments, historical_data):
        # we need data for the LBMOM strategy
        # we want moving averages which proxies to momentum factor
        # we also want a univariate statistical factor as an indicator of regime- ADX used for momentum regime indicator
        for inst in instruments:
            pass

    def run_simulation(self, historical_data):
        pass

    def get_subsys_pos(self):
        pass