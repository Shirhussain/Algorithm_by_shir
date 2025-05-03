class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) {
            return 0;
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(0);
        Set<Integer> visited = new HashSet<>();
        visited.add(0);

        int level = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();

            // for each target amount in the queue/level
            for (int i = 0; i < size; i++) {
                // get the current target
                int cur = queue.poll();
                // if (cur == amount) {
                //     return level;
                // }

                for (int coin : coins) {
                    int next = cur + coin;
                    if (next == amount) {
                        // success!!!
                        return level + 1;
                    }

                    if (next > amount) {
                        continue;
                    }

                    if (!visited.contains(next)) {
                        queue.offer(next);
                        visited.add(next);
                    }
                    
                }
            }

            level++;
        }

        return -1;
    }
    
    public int coinChange2(int[] coins, int amount) {
        Map<Integer, Integer> map = new HashMap<>();
        return helper(coins, amount, map);
    }

    int helper(int[] coins, int amount, Map<Integer, Integer> map) {
        if (amount == 0) {
            return 0;
        }

        if (amount < 0) {
            return -1;
        }

        if (map.containsKey(amount)) {
            return map.get(amount);
        }

        // amount > 0
        int min = Integer.MAX_VALUE;
        for (int coin : coins) {
            int count = helper(coins, amount - coin, map);
            if (count >= 0) {
                min = Math.min(min, count + 1);
            }
        }

        map.put(amount, min == Integer.MAX_VALUE ? - 1 : min);
        return map.get(amount);
    }
}