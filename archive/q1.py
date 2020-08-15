# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def compute():
    ans = 0
    x = 0
    while x < 1000:
        if (x % 3 == 0 or x % 5 == 0):
            ans = ans + x
        x = x + 1
    return ans


if __name__ == "__main__":
    print(compute())
