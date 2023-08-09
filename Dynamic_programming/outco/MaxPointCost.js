// Painting problem:
// You're painting the exterior of houses in a neighborhood. Each house has a
// cost. Adjacent houses can't be painted on the same day because the paint
// needs to dry.

// Given an array costs of house painting costs, return the maximum possible
// cost while adhering to the constraint of not painting adjacent houses on the
// same day.

// Example 1:
// Input: costs = [2, 7, 9, 3, 1]
// Output: 12
// Explanation: Paint the first, third, and fifth houses for a total cost of 2 +
// 9 + 1 = 12.

// Example 2:
// Input: costs = [10, 5, 1, 20]
// Output: 30
// Explanation: Paint the first and fourth houses for a total cost of 10 + 20
// = 30.

// Example 3:
// Input: costs = [4, 1, 2, 3, 7]
// Output: 13
// Explanation: Paint the first, third, and fifth houses for a total cost of 4 +
// 2 + 7 = 13.

// Recursive relationship
// F(n) = Max ( F(n-1), F(n-2) + costs[n] )
// F(0) = costs[0],  F(1) =F(0)+ costs[1]

// more information: -->
// https://docs.google.com/document/d/1JaYYuTtXCSAuCqoZnyfIe8sHGW9iY4-_eSIffENHnKU/edit

function MaxPaintCost(costs) {
  function MaxPaintCostHelper(i) {
    if (i === 0) {
      return costs[0];
    }

    if (i === 1) {
      return Math.max(costs[0], costs[1]);
    }

    return Math.max(
      MaxPaintCostHelper(i - 1),
      MaxPaintCostHelper(i - 2) + costs[i]
    );
  }

  return MaxPaintCostHelper(costs.length - 1);
}

let costs = [4, 1, 2, 3, 7];
console.log(MaxPaintCost(costs));

costs = [10, 5, 1, 20];
console.log(MaxPaintCost(costs));
