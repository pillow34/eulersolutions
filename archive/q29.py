# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import eulerfuncs as ef
import math
import timeit


def compute():
    ans = []
    for a in range(2, 101):
        for b in range(2, 101):
            ans.append(math.pow(a, b))
    return len(set(ans))


if __name__ == "__main__":
    # %timeit print(compute())
    print(compute())
