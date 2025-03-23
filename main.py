from argparse import ArgumentParser
from business_logic import base_requests


# -----
parser = ArgumentParser(
    "Trading robot simulator",
)
subparsers = parser.add_subparsers(help="Choose console or web interface")
console_parser = subparsers.add_parser(
    "cli",
    help = "console interface"
)
web_parser = subparsers.add_parser(
    "web",
    help = "web interface"
)

web_parser.add_argument(
    "runserver",
    choices=("runserver",),
)

console_parser.add_argument(
    "actives",
    nargs='?',
    choices=("actives",),
    help="get all available actives"
)
console_parser.add_argument(
    "--active",
    type=str,
    choices=base_requests.available_actives,
    help="get price(in USD) of pointed active"
)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.actives:
        print(base_requests.get_available_actives())
    elif args.active:
        print(base_requests.get_price_of_active(args.active))
    base_requests._()
