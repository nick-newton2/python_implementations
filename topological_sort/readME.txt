Uses a topological sort to find the passcode

passcode mechanism: instead of entering the whole passcode
the user must enter in three random numbers from the original door code. For instance, if the passcode was 2468135, the user may be asked to enter in the 2nd, 4th, and 5th numbers: 481. This shorter sequence (2nd, 4th, 5th) changes each time, so just watching the someone enter in the door code will not guarantee entry to the snooper. Moreover, it helps prevent divulging the complete passcode.

Given a series of successful entries where each entry is a three digit sequence, crack the passcode.

Example Input:
352
154
542
315
152

Example Output:
31542
