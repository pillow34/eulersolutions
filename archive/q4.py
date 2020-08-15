# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import eulerfuncs as ef


def compute():
    ans = []
    y = [i for i in range(101, 999)]
    ans = [a*b for a, b in ef.product(y, y)]
    ans.sort(reverse=True)
    for i in range(len(ans)):
        if str(ans[i]) == str(ans[i])[::-1]:
            return ans[i]


if __name__ == "__main__":
    print(compute())
