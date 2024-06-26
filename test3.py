import numpy as np
import vectorbt as vbt

# symbols = ["BTC-USD", "ETH-USD"]
# price = vbt.YFData.download(symbols, missing_index='drop').get('Close')

# n = np.random.randint(10, 101, size=1000).tolist()
# pf = vbt.Portfolio.from_random_signals(price, n=n, init_cash=100, seed=42)

# mean_expectancy = pf.trades.expectancy().groupby(['randnx_n', 'symbol']).mean()
# fig = mean_expectancy.unstack().vbt.scatterplot(xaxis_title='randnx_n', yaxis_title='mean_expectancy')
# fig.show()

symbols = ["BTC-USD", "ETH-USD", "LTC-USD"]
price = vbt.YFData.download(symbols, missing_index='drop').get('Close')

windows = np.arange(2, 101)
fast_ma, slow_ma = vbt.MA.run_combs(price, window=windows, r=2, short_names=['fast', 'slow'])
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

pf_kwargs = dict(size=np.inf, fees=0.001, freq='1D')
pf = vbt.Portfolio.from_signals(price, entries, exits, **pf_kwargs)

# fig = pf.total_return().vbt.heatmap(
#     x_level='fast_window', y_level='slow_window', slider_level='symbol', symmetric=True,
#     trace_kwargs=dict(colorbar=dict(title='Total return', tickformat='%')))
# fig.show()

print(pf[(10, 20, 'ETH-USD')].stats())

pf[(10, 20, 'ETH-USD')].plot().show()
# import matplotlib.pyplot as plt
# plt.show()