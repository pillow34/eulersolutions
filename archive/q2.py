# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def compute():
    ans = 0
    x, y = 0, 1
    while y < 4000000:
        x, y = y, x + y
        if y % 2 == 0:
            ans = ans + y

    return ans


if __name__ == "__main__":
    print(compute())
