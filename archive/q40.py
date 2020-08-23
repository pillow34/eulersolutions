# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import eulerfuncs as ef
import math
import timeit


def compute():
    ans = ''.join(str(digit) for digit in range(1, 1000000))
    return int(ans[1-1]) * int(ans[10-1]) * int(ans[100-1]) * int(ans[1000-1]) * int(ans[10000-1]) * int(ans[100000-1]) * int(ans[1000000-1])


if __name__ == "__main__":
    # %timeit print(compute())
    print(compute())
