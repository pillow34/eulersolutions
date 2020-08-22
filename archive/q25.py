# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import eulerfuncs as ef
import math


def compute():
    ans = [1]
    y = 1
    x = 1
    while int(math.log10(max(ans))) + 1 < 1000:
        x, y = y, x + y
        ans.append(x)
    return len(ans)


if __name__ == "__main__":
    print(compute())
