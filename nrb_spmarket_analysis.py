

"""
Nairobi Supermarket Transaction Analysis
----------------------------------------
This script generates trend analysis for
synthetic daily transaction history of a Nairobi
supermarket over a period of 18 months.

Creates and saves a chart showing
monthly transaction totals.
Usage:
    python nrb_spmarket_analysis.py

Config:
    Adjust the baseline, seasonal patterns, and noise
    parameters to simulate different transaction scenarios.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dates = pd.date_range("2025-04-01", "2026-09-30", freq="D")

baseline = 1000


month_factors = {1: 0.9, 2: 0.8, 3: 1.0,
     4: 1.1, 5: 1.0, 6: 1.2, 7: 1.1,
       8: 1.2, 9: 0.9, 10: 1.2, 11: 1.3, 12: 1.4}

seasonal_pattern = dates.month.map(month_factors).to_numpy()

weekly_pattern = np.where(dates.weekday < 5, 1.2, 1.0)

growth_trend = 1 + 0.0005 * np.arange(len(dates))

nrg = np.random.default_rng(seed=42)
noise = nrg.normal(1, 0.05, len(dates))

transactions = (baseline * seasonal_pattern * weekly_pattern * growth_trend * noise).round().astype(int)

daily = pd.DataFrame({"transactions": transactions}, index=dates)
daily.index.name = "Date"

print(daily.head(5))
print("------------------------------------------")

daily["growth"] = daily["transactions"].pct_change() * 100

daily["rolling_30d"] = daily["transactions"].rolling(30).mean()

print("\n----------Rolling Averages-------------\n")
print(daily[["transactions", "rolling_30d"]].round(1))


monthly = daily["transactions"].resample("ME").sum()
mid_month = monthly.index - pd.Timedelta(days=15)
print("\n---------------Monthly Totals-------------\n")
print(monthly)
print("------------------------------------------")
print(daily.tail())


fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.bar(mid_month, monthly.values, width=20, color="#1F4E79", label="Monthly total transactions")
ax1.set_xlabel("Month")
ax1.set_xticks(mid_month)
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
fig.autofmt_xdate()
ax1.set_ylabel("Transactions per Month")
ax1.set_title("Monthly Transaction Totals")
ax2 = ax1.twinx()
ax2.plot(daily.index, daily["rolling_30d"], color="#FF6B6B", linewidth=2.5, label="30-Day Rolling Average")
ax2.set_ylabel("Average Daily Transactions")
ax1.set_title("Monthly Transaction Totals with 30-Day Rolling Average", fontsize=12)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="lower right")

plt.tight_layout()
plt.savefig("nrb_final.png", dpi=150)
print("Chart saved: nrb_final.png")
