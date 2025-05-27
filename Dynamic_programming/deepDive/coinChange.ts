function coinChange(coins: number[], amount: number): number {
  let q: number[] = [];
  q.push(amount);
  let visited: Set<number> = new Set();
  visited.add(amount);
  let steps = 0;
  while (q.length > 0) {
    let size = q.length;
    for (let i = 0; i < size; i++) {
      let node = q.shift();
      if (node === undefined) continue;
      if (node === 0) return steps;
      for (let coin of coins) {
        let next = node - coin;
        if (!visited.has(next)) {
          visited.add(next);
          q.push(next);
        }
      }
    }
    steps++;
  }
  return -1;
}

console.log(coinChange([1, 2, 5], 11));
