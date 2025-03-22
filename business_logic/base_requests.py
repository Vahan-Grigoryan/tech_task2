from dotenv import load_dotenv
import requests, os, base64, time
from cryptography.hazmat.primitives.serialization import load_pem_private_key


load_dotenv()
base_url = "https://testnet.binance.vision/"
available_actives = (
    "ETHBTC",
    "LTCBTC",
    "BNBBTC",
    "NEOBTC",
    "QTUMETH",
    "EOSETH",
    "SNTETH",
    "BNTETH",
    "GASBTC",
    "BNBETH",
    "BTCUSDT"
)
with open(os.getenv("PRIVATE_KEY_PATH"), 'rb') as f:
    private_key = load_pem_private_key(data=f.read(), password=None)


def get_available_actives():
    return available_actives


def get_price_of_active(active):
    actives = requests.get(
        f"{base_url}api/v3/ticker/price?symbol={active}",
        headers = {
            'X-MBX-APIKEY': os.getenv("API_KEY"),
        }
    )
    return actives.json()

def _():
    params = {
    }

    timestamp = int(time.time() * 1000) # UNIX timestamp in milliseconds
    params['timestamp'] = timestamp

    payload = '&'.join([f'{param}={value}' for param, value in params.items()])
    signature = base64.b64encode(private_key.sign(payload.encode('ASCII'), ))
    params['signature'] = signature

    _ = requests.get(
        f"{base_url}api/v3/account",
        headers = {
            'X-MBX-APIKEY': os.getenv("API_KEY"),
        },
        data=params,
    )
    print(_.status_code)
    print(_.json())
