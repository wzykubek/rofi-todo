#!/usr/bin/env python3

import json, argparse
from rofi import Rofi

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f", "--file", help="specify path to notes JSON file", required=True
)
args = parser.parse_args()

json = json.loads(open(args.file).read())

titles = []
for i in range(len(json["notes"])):
    titles.append(json["notes"][i]["name"])

r = Rofi()

index, key = r.select("Notes", titles, rofi_args=["-i", "-no-custom"])

if key == 0:
    r.error(json["notes"][index]["description"])
