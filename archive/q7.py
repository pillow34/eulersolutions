# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import eulerfuncs as ef


def compute():
    ans = [2, 3]
    a = 5
    while len(ans) <= 10000:
        if ef.isPrime(a):
            ans.append(a)
            a += 2
            # print((ans))
        else:
            a += 2

    return max(ans)


if __name__ == "__main__":
    print(compute())
