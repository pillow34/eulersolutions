# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import eulerfuncs as ef
import math


def compute():
    ans = sum(int(digit) for digit in str((2**1000)))
    return (ans)


if __name__ == "__main__":
    print(compute())
