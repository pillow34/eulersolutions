# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import eulerfuncs as ef


def compute():
    y = [i for i in range(1, 21)]
    return ef.findLCM(y)


if __name__ == "__main__":
    print(compute())
