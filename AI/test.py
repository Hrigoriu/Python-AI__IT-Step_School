import requests

def get_min_order_size(inst_id="BTC-USDT"):
    url = "https://www.okx.com/api/v5/public/instruments"
    params = {"instType": "SPOT", "instId": inst_id}
    r = requests.get(url, params=params).json()
    data = r["data"][0]
    return float(data["minSz"]), float(data["lotSz"]), float(data["tickSz"])

minSz, lotSz, tickSz = get_min_order_size("BTC-USDT")
print("Мінімальний обсяг:", minSz, "BTC")
