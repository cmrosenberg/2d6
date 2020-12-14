#!/usr/bin/env python3
import twodeesix
import random


def roll_twod6():

    return random.choice([1, 2, 3, 4, 5, 6]) + random.choice([1, 2, 3, 4, 5, 6])


def simulate(
    target_num,
    modifier=0,
    reroll=False,
    dispell=False,
    dispell_reroll=False,
    dispell_modifier=0,
):

    # assume "may reroll" interpretation

    roll = roll_twod6() + modifier

    if roll < target_num:
        if reroll:
            roll = roll_twod6() + modifier
            if roll < target_num:
                return False
        else:
            return False

    if dispell:
        dispell_roll = roll_twod6() + dispell_modifier
        if dispell_roll > roll:
            return False
        elif dispell_reroll:
            dispell_roll = roll_twod6() + dispell_modifier
            if dispell_roll > roll:
                return False

    return True


def test_correspondence(
    target_num,
    modifier=0,
    reroll=False,
    dispell=False,
    dispell_reroll=False,
    dispell_modifier=0,
    N=100000,
    eps=0.001,
):
    direct_result = twodeesix.main(
        target=target_num, modifier=modifier, reroll=reroll, dispell=dispell
    )

    successes = 0
    for i in range(N):
        success = simulate(
            target_num=target_num, modifier=modifier, reroll=reroll, dispell=dispell
        )
        if success:
            successes += 1

    correspondence = (direct_result - (successes / N)) < eps

    if not correspondence:
        print("exact: ", float(direct_result), "simulated:", (successes / N))

    return correspondence


def simulate_all(N=30000, eps=0.02, debug=True):

    for target_num in range(4, 13):
        for modifier in [-4, -3, -2, -1, 1, 2, 3, 4]:
            for reroll in [True, False]:
                for dispell in [True, False]:
                    corresponding = test_correspondence(
                        target_num=target_num,
                        modifier=modifier,
                        reroll=reroll,
                        dispell=dispell,
                        N=N,
                        eps=eps,
                    )
                    if not corresponding:
                        if debug:
                            print(
                                "FAILING: target num",
                                target_num,
                                "modifier",
                                modifier,
                                "reroll",
                                reroll,
                                "dispell",
                                dispell,
                            )
                        return False

    if debug:
        print("All simulations succeeded.")
    return True


if __name__ == "__main__":

    simulate_all()
