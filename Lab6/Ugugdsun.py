"""
Эрэмбэлэгдсэн n ширхэг хайлтын түлхүүр агуулсан k жагсаалт бо￾лон түлхүүр бүрийн хайгдсан тоог агуулсан f жагсаалт өгөгджээ. Тэгвэл нийт түлхүүрийн хувьд хайлтын хамгийн бага өртгийг ол.
Жишээлбэл, n = 2, k = {5, 6}, f = {17, 25} бол хамгийн бага өртөг нь 59. Учир нь оройн утга нь 5 (5–6) бол c = 17 ∗ 1 + 25 ∗ 2 = 67 болно. 
Харин 6 бол (6–5) c = 25 ∗ 1 + 17 ∗ 2 = 59 болно.
"""
def min_search_cost(k, f):
    n = len(k)
    min_cost = float('inf')
    
    for root in k:
        cost = 0
        for i in range(n):
            level = abs(k[i] - root)
            cost += f[i] * (level + 1)
        min_cost = min(min_cost, cost)
    
    return min_cost

if __name__ == "__main__":
    k = [5, 6]
    f = [17, 25]
    result = min_search_cost(k, f)
    print(f"Minimum search cost: {result}")
