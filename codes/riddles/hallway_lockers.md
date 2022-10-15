### Problem Statement

You are in a hallway with 100 lockers. You start with one pass and open the lockers, so that the opened lockers are now with their doors opened out. You begin by closing every second locker. Then you go to toggle every third locker (close every third locker and close it if it is open). You continue toggling every nth locker on pass number n. After your hundredth pass of the hallway, in which you toggle only locker number 100, how many lockers are open?

### Solution

Take a subset of the problem. Let limit to 12 lockers.
To start off we know we won't have to toggle it on any pass greater than 12. So now we only have to think of the passes that occur on 2 - 11. We can actually count these out:
On pass 2: 2,4,6,8,10,12
On pass 3: 3,6,9,12
On pass 4: 4,8,12
On pass 5: 5,10 **No toggle on this pass**.
On pass 6: 6,12
On pass 7: 7 **No toggle on this pass**

Pattern:

- All lockers are open on the first pass.
- So lockers are closed after the 2nd, 4th, 6th and so on times they are toggled. In other words, if a locker is toggled an even number of times, then it ends closed, otherwise, it ends open, You know that a locker is toggled once for every factor of the locker number, so you can say that a locker ends open only if it has an odd number of factors.
- **The task has now been reduced to finding how many numbers between 1 and 100 have an odd number of factors!**
