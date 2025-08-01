from datetime import datetime, timedelta
from db import get_prices_for_period

def format_percent(val):
    return f"{val:+.2f}%" if val is not None else "N/A"

def calc_change(new, old):
    if old is None or old == 0:
        return None
    return 100.0 * (new - old) / old

def generate_report():
    today = datetime.utcnow().date()
    prices = get_prices_for_period(31)
    # prices = list of (date, price), most recent first

    if not prices or len(prices) < 2:
        return "Not enough data to generate a report yet."

    price_today = prices[0][1]
    date_today = prices[0][0]

    # Previous trading day
    price_yest = prices[1][1]
    date_yest = prices[1][0]
    day_chg = calc_change(price_today, price_yest)

    # 7 days ago
    if len(prices) > 7:
        price_wk = prices[7][1]
        date_wk = prices[7][0]
        week_chg = calc_change(price_today, price_wk)
    else:
        price_wk = None
        date_wk = None
        week_chg = None

    # 30 days ago
    if len(prices) > 30:
        price_mo = prices[30][1]
        date_mo = prices[30][0]
        month_chg = calc_change(price_today, price_mo)
    else:
        price_mo = None
        date_mo = None
        month_chg = None

    lines = [
        f"Silver Spot Price as of {date_today}: ${price_today:.2f}\n",
        f"Previous Trading Day ({date_yest}): ${price_yest:.2f} | Change: {format_percent(day_chg)}",
    ]
    if week_chg is not None:
        lines.append(f"1 Week Ago ({date_wk}): ${price_wk:.2f} | Change: {format_percent(week_chg)}")
    if month_chg is not None:
        lines.append(f"1 Month Ago ({date_mo}): ${price_mo:.2f} | Change: {format_percent(month_chg)}")
    return "\n".join(lines)
