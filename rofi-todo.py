#!/usr/bin/env python3

import json, argparse
from rofi import Rofi

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f", "--file", help="specify path to notes notes file", required=True
)
args = parser.parse_args()

with open(args.file) as f:
    notes = json.load(f)

titles = []
def show_titles():
    for i in range(len(notes["notes"])):
        titles.append(notes["notes"][i]["name"])

r = Rofi()

while True:
    titles = []
    show_titles()

    index, key = r.select(
        "Notes",
        titles,
        key1=("Alt+d", "delete note"),
        key2=("Alt+a", "add note"),
        rofi_args=["-i", "-no-custom", "-l", "15"],
    )

    if key == 0:
        r.error(notes["notes"][index]["description"])

    elif key == 1:
        del notes["notes"][index]

        with open(args.file, "w") as f:
            json.dump(notes, f, indent=2)

        r.error("Note deleted.")

    elif key == 2:
        name = r.text_entry("Enter note name", rofi_args=["-l", "0"])

        if name:
            desc = r.text_entry("Enter node description", rofi_args=["-l", "0"])
            new_note = {"name": name, "description": desc}
            notes["notes"].append(new_note)

            with open(args.file, "w") as f:
                json.dump(notes, f, indent=2)

            r.error("Note added.")

    else:
        break
