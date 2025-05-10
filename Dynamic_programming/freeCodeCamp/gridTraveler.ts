const girdTraveler = (
  m: number,
  n: number,
  memo: { [key: string]: number } = {}
): number => {
  if (m == 1 && n == 1) return 1;
  if (m == 0 || n == 0) return 0;

  const key = `${m}, ${n}`;

  if (key in memo) return memo[key];
  memo[key] = girdTraveler(m - 1, n, memo) + girdTraveler(m, n - 1, memo);
  return memo[key];
};

console.log(girdTraveler(18, 18, {}));
