import argparse
# arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--File", default="default", type=str, help="...")
parser.add_argument("-s", "--Save", help="...", action="store_true")
args = parser.parse_args()
