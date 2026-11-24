"""Vacuum excuse: the robot vacuum explains why the sock survived.

A robot vacuum patrols the floor, detects objects, and classifies each one
before deciding whether to clean around it or swallow it. This program
replays the vacuum's patrol log for one cleaning run and writes the excuse
it gives for the single object it refused to touch, as one line of text.

Run: python3 main.py
Output: /output/entry.txt (UTF-8, one line, 1-140 characters)
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140

# What the vacuum's camera saw, in the order it saw it. Each entry is
# (object name, where it was found).
PATROL_LOG = [
    ("dust bunny", "under the sofa"),
    ("sock", "middle of the living room"),
    ("charging cable", "beside the desk"),
]

# The vacuum's classifier: object name -> what the vacuum thinks it is.
# Anything it cannot place with confidence is treated as furniture.
CLASSIFICATIONS = {
    "dust bunny": "dirt",
    "sock": "pet",
    "charging cable": "snake",
}


def classify(object_name):
    """Return what the vacuum believes an object is."""
    return CLASSIFICATIONS.get(object_name, "furniture")


def excuse_for(object_name):
    """Build the vacuum's excuse for refusing to clean an object.

    The vacuum only apologises for objects it classified as a pet: those
    are the ones it befriended instead of cleaning.
    """
    label = classify(object_name)
    if label != "pet":
        return None
    return "I detected a {0}, classified it as a {1}, and now we are friends.".format(
        object_name, label
    )


def build_excuse():
    """Find the first pet in the patrol log and return its excuse."""
    for object_name, _location in PATROL_LOG:
        excuse = excuse_for(object_name)
        if excuse is not None:
            return excuse
    raise ValueError("no pet found in the patrol log")


def write_entry(text):
    """Write the excuse to OUTPUT_PATH as UTF-8, mode 0644.

    The /output directory is created when missing but never chmodded.
    The file holds exactly the excuse bytes: no trailing newline.
    """
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    return OUTPUT_PATH


def main():
    excuse = build_excuse()
    path = write_entry(excuse)
    print(excuse)
    print("%s: %d characters" % (path, len(excuse)))


if __name__ == "__main__":
    main()
