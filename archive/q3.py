# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import eulerfuncs as ef


def compute():
    y = 600851475143
    ans = ef._divs(y)
    return max(ans)


if __name__ == "__main__":
    print(compute())
