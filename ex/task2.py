
import argparse
import sys
parser = argparse.ArgumentParser(
    description='калькулятор'
)

parser.add_argument(
    'values'
    metavar='VALUES'
    type=float
    nargs='2'
    help='входные данные'
)

parser.add_argument(
    '-a',
    '--action',
    type=float,
    action='store_true',
    help='знак'
)
parser.add_argument(
    '-v',
    '--verbose',
    action='store_true',
    help='вывести выражение'
)

if not args.action and not args.verbose:
    print(
        'Должен быть указан хотя бы один из параметров --action и --verbose',
        file=sys.stderr
    )
    sys.exit(-1)
args = parser.parse_args()
values = args.values
if args.action is '*':
    print(values[0]*values[1])
elif args.action is '-':
    print(values[0]-values[1])
elif args.action is '+':
    print(values[0]+values[1])
elif args.action is '/':
    print(values[0]/values[1])
