# File: README.md

# Nairobi Supermarket Transaction Analysis

A Python script that generates trend analysis for synthetic daily transaction history of a Nairobi supermarket over a period of 18 months. It plots and saves a chart showing monthly transaction totals.

## What It Does

- Generates 18-months realistic transaction data
- Uses numpy to create seasonal variation
- Resamples daily transactional data to monthly totals
- Creates month-to-month growth and 30-day rolling average
- Plots chart of monthly bars alongside 30-day rolling average
- Saves the chart as PNG


## My Analysis

- From the chart, the sales are not growing continously.
- This is a seasonal peak and fall and there is no clear indication of general monthly transaction growth. 

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Run the program from the project's folder

```
python nrb_spmarket_analysis.py
```
## How It Works
Transaction analysis chart is generated alongside a 30-day rolling average, after resampling monthly totals. The chart is then saved as a PNG.
 
```python
daily["growth"] = daily["transactions"].pct_change() * 100

daily["rolling_30d"] = daily["transactions"].rolling(30).mean()

monthly = daily["transactions"].resample("ME").sum()
mid_month = monthly.index - pd.Timedelta(days=15)

ax2.plot(daily.index, daily["rolling_30d"], color="#FF6B6B", linewidth=2.5, label="30-Day Rolling Average")
```


## Sample Output

```
            transactions     growth  rolling_30d
Date                                            
2026-09-26          1134 -18.417266  1351.800000
2026-09-27          1130  -0.352734  1326.733333
2026-09-28          1363  20.619469  1321.000000
2026-09-29          1389   1.907557  1315.300000
2026-09-30          1306  -5.975522  1300.500000
```

## Stack

Python, matplotlib
