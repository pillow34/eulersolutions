# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import eulerfuncs as ef


def compute():
    ans = []
    y = 600851475143
    k = 5
    while k >= 5 and k <= int(ef.np.sqrt(y)):
        if ef.isPrime(k) and y % k == 0:
            ans.append(k)
        k = k + 6

    return max(ans)


if __name__ == "__main__":
    print(compute())
