# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%

def compute():
    y = [i for i in range(1, 101)]
    z = [i * i for i in range(1, 101)]
    return sum(y)**2 - sum(z)


if __name__ == "__main__":
    print(compute())
