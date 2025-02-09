import argparse
import jsondiff
import ujson
import warnings
import sys
import cProfile

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("first")
    parser.add_argument("second")
    parser.add_argument("-p", "--patch", action="store_true", default=False)
    parser.add_argument("-s", "--syntax", action="store", type=str, default="compact")
    parser.add_argument("-i", "--indent", action="store", type=int, default=None)

    args = parser.parse_args()

    cProfile.run('main_wrap(args)')

def main_wrap(args):
    with open(args.first, "r") as f:
        with open(args.second, "r") as g:
            jf = ujson.load(f)
            jg = ujson.load(g)
            if args.patch:
                x = jsondiff.patch(
                    jf,
                    jg,
                    marshal=True,
                    syntax=args.syntax
                )
            else:
                x = jsondiff.diff(
                    jf,
                    jg,
                    marshal=True,
                    syntax=args.syntax
                )

            ujson.dump(x, sys.stdout, indent=args.indent)

def main_deprecated():
    warnings.warn("jsondiff is deprecated. Use jdiff instead.", DeprecationWarning)
    main()

if __name__ == '__main__':
    cProfile.run('main()')
