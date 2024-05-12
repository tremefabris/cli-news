import argparse

def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--jornal", "-j", type=str, required=True)

    return parser.parse_args()