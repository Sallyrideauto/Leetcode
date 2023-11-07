'''
The program follows these steps:
1. Calculate the times list which is the time taken for each monster to reach the city.
2. Sort the list times so that we can process the monsters in the order they would reach the city.
3. Initialize count to track the number of monsters eliminated.
4. Initialize currentTime to 0 since the game starts with the weapon charged.
5. Iterate through the times list:
    • If the time for a monster to reach the city is greater than the current time, 
      you can eliminate the monster, increment the count, and update the current time.
	• If the time is less than or equal to the current time, a monster has reached the city, and the game is over.
6. Return the total count of monsters eliminated before any of them can reach the city
'''

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Calculate the time it will take for each monster to reach the city
        times = [dist[i] / speed[i] for i in range(len(dist))]
        
        # Sort the monsters by their time to reach the city
        times.sort()
        
        # The count of monsters eliminated
        count = 0
        
        # The current time
        currentTime = 0
        
        # Go through the times list and eliminate monsters
        for t in times:
            # If the monster's time is greater than the curent time,
            # you can eliminate this monster.
            if t > currentTime:
                count += 1
                currentTime += 1
            else:
                # If a monster reaches the city before or when the weapon is ready,
                # the game is over, so break the loop.
                break
                
        # Return the total count of monsters eliminated
        return count