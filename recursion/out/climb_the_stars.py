'''
https://docs.google.com/document/d/1Uhnldz90UuZU5vDdVRAQgV49aKyR7ieafbmJTrVAH0U/edit?usp=sharing

// Given a non-negative integer n, to calculate how many distinct ways you can
// climb to the top. Your function should accept positive numbers less than 45
// and return the number of ways. We define:
// Rules of the climb stairs:
// You are climbing a staircase. Each time you can either climb 1 or 2 or 3
// steps. It takes n steps to reach the top. Your function takes n as input.

// If there are 0 stairs, return 0. For negative input, please
// return -1.
// For example, if the stairs number is 3, (n = 3), it should have 4 ways to the
// top:

// 1 + 1 + 1

// 1 + 2

// 2 + 1

// 3


'''


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return f(n-1) + f(n-2) + f(n-3)
