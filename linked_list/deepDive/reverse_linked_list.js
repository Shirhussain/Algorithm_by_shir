/*

Here's the trick. Imagine I ask you:
> "Hey, reverse this list: 1 → 2 → 3 → 4"
You say: "That's hard. Let me ask my friend to reverse the smaller part first."
So you hand 2 → 3 → 4 to your friend. Your friend says the same thing and hands 3 → 4 to their friend. That friend hands 4 to the next person.
That last person says: "There's only one item. It's already reversed! Here, take it back." That's the base case.
Now everyone starts passing results back and doing one small fix each.

*/
function reverse(head) {
  // BASE CASE: if empty or just one node, it's already reversed
  if (!head || !head.next) return head;

  // ASK FRIEND: "hey, reverse everything after me"
  const newHead = reverse(head.next);

  // MY ONE SMALL FIX: make the node after me point BACK to me
  head.next.next = head;

  // CLEAN UP: I'm now the last node, so I point to null
  head.next = null;

  // PASS UP: the new head (always node 4) goes all the way back
  return newHead;
}

/*

Each person in the chain says: "I can't reverse the whole thing,
but if someone reverses everything after me, I just need to make
my neighbor point back to me." That's it. That's the entire algorithm

*/
