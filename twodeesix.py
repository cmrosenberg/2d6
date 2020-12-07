#!/usr/bin/env python3
import sys
from fractions import Fraction

def geq(num, modifier=0):

    successes = 0
    fails = 0
    total = 36

    for a in range(1, 6 + 1):
        for b in range(1, 6 + 1):
            if (a + b + modifier) >= num:
                successes += 1
            else:
                fails += 1

    return successes, fails, total


def possible_successes(target, modifier):

    success_freq = {}

    for a in range(1, 6 + 1):
        for b in range(1, 6 + 1):
            if (a + b + modifier) >= target:
                obtained_sum = a + b + modifier

                if obtained_sum not in success_freq:
                    success_freq[obtained_sum] = 0

                success_freq[obtained_sum] += 1

    return dict(map(lambda x: (x[0], Fraction(x[1], 36)), success_freq.items()))


def dispell_target_prob(target, dispell_mod=0):

    success, fails, total = geq(target + 1, dispell_mod)

    return Fraction(success, total)


def resolve_modifier_args(modifiers):

    boost = 0
    neg = 0

    for m in modifiers:
        if "+" in m:
            num = int(m.split("+")[1])
            boost += num
        else:
            num = int(m.split("-")[1])
            neg += num

    return boost - neg


def show_help():

    print("Hello")


def parse_args(arguments):

    if len(arguments) == 1:
        show_help()
        sys.exit(0)

    if arguments[1].lower() == "help":
        show_help()
        sys.exit(0)

    target = int(arguments[1])

    if len(arguments) == 2:
        return {"target": target, "modifier": 0, "reroll": False, "dispell": False}

    for arg in arguments[2:]:
        if (
            ("+" not in arg)
            and ("-" not in arg)
            and arg.lower() not in ["reroll", "r", "dispell", "d"]
        ):
            raise Exception("invalid argument:", arg, ". Run `2d6 help` for help")

    modifiers = list(filter(lambda a: "+" in a or "-" in a, arguments[2:]))

    modifier = 0
    if len(modifiers) > 0:
        modifier = resolve_modifier_args(modifiers)

    reroll = ("reroll" in arguments[2:]) or ("r" in arguments[2:])
    dispell = ("dispell" in arguments[2:]) or ("d" in arguments[2:])

    return {
        "target": target,
        "modifier": modifier,
        "reroll": reroll,
        "dispell": dispell,
    }


def format_nicely(success_frac):

    print(
        "{:.2f}%".format(float(success_frac * 100)),
        "(exact:",
        str(success_frac.numerator) + "/" + str(success_frac.denominator) + ")",
    )

if __name__ == "__main__":

    args = parse_args(sys.argv)

    success, fails, total = geq(args["target"], modifier=args["modifier"])
    success_frac = Fraction(success, total)
    fail_frac = Fraction(1, 1) - success_frac

    if not args["dispell"]:
        if args["reroll"]:
            success_frac = success_frac + (fail_frac * success_frac)

        format_nicely(success_frac)
        sys.exit(0)

    ps = possible_successes(args["target"], modifier=args["modifier"])

    if args["reroll"]:
        for tval, prob in ps.items():
            ps[tval] = prob + (fail_frac * prob)

    for tval, prob in ps.items():

        ps[tval] = prob * (Fraction(1, 1) - dispell_target_prob(tval))

    final_success = Fraction(0, 1)
    for tval in ps:
        final_success += ps[tval]

    format_nicely(final_success)
