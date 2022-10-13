### Bridge crossing problem

#### Problem

A group of four travelers comes to a bridge at night. The bridge can hold the weight of at most only two of the travelers at a time, and it can not be crossed without using a flashlight.
The travelers have one flashlight among them. Each traveler walks at a different speed: The first can cross the bridge in 1 minute, the second in 2 minutes, the third in 5 minutes and the fourth takes 10 minutes to cross the bridge. If two travelers cross together, they walk at the speed of the slower traveler.
What is the least amount of time in which all the travelers can cross from one side of the bridge to the other?

#### Solution

|          Move           | Time |
| :---------------------: | :--: |
| 1 & 2 cross with torch  |  2   |
|   1 return with torch   |
| 5 & 10 cross with torch |  10  |
|   2 return with torch   |
| 1 & 2 cross with torch  |  2   |
|                         |  17  |
