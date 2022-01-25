class ProductOfNumbers:

    def __init__(self):
        self.mult = [1]

    def add(self, num: int) -> None:
        if num > 0:
            self.mult.append(self.mult[-1] * num)
        else:
            self.mult = [1]

    def getProduct(self, k: int) -> int:
        n = len(self.mult)-1
        if k < n:
            return 0
        if k == n:
            return self.mult[-1]
        return self.mult[n] // self.mult[n-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

def process(insts, vals):
    prod = ProductOfNumbers()
    res = []
    input = []
    getK = []
    for i, inst in enumerate(insts):
        print(prod.mult)
        if inst == 'add':
            prod.add(vals[i][0])
            input.append(vals[i][0])
        elif inst == 'getProduct':
            getK.append(vals[i][0])
            res.append(prod.getProduct(vals[i][0]))
    print('Input', input)
    print('kth', getK)
    print(prod.mult)
    return prod, res


prod, res = process(
    ["add", "add", "add", "add", "add",
        "getProduct", "getProduct", "getProduct", "add", "getProduct"],
    [[3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]
)

print(prod.getProduct(5))

print(res)
