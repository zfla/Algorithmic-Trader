# function to get data and indicators specific to strategy
# function to run backtest and get positions
import json
import quantlib.indicators_cal as indicators_cal
import pandas as pd

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
            historical_data["{} adx".format(inst)] = indicators_cal.adx_series(
                high=historical_data["{} high".format(inst)],
                low=historical_data["{} low".format(inst)],
                close=historical_data["{} close".format(inst)],
                n=14
            )
            for pair in self.pairs:
                # calculating the fast moving average - slow moving average
                historical_data["{} ema{}".format(inst, str(pair))] = indicators_cal.ema_series(historical_data["{} close".format(inst)], n=pair[0]) - \
                    indicators_cal.ema_series(historical_data["{} close".format(inst)], n=pair[1])
        # carries all information required for backtesting
        return historical_data

    def run_simulation(self, historical_data):
        """
        Initialise params
        """
        instruments = self.instruments_config["instruments"]

        """
        Pre-processing
        """
        historical_data = self.extend_historicals(instruments=instruments, historical_data=historical_data)
        portfolio_df = pd.DataFrame(index=historical_data[self.simulation_start:].index).reset_index()
        portfolio_df.loc[0, "capital"] = 10000
        print(portfolio_df)

        """
        Run simulation
        """

    def get_subsys_pos(self):
        self.run_simulation(historical_data=self.historical_df)
        