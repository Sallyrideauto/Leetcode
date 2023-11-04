class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        """
        Function to calcultate the time when we the last and falls off the plank.
        
        Parameters:
        n(int): The length of the plank.
        left(list of int): The positions of ants moving to the left.
        right(list of int): The positions of ants moving to the right.
        
        Returns:
        int: The moment when the last ant falls off the plank.
        """
        
        # initialize the last moment to 0
        last_moment = 0
        
        # Check each ant moving to the left.
        # The time it takes for these ants to fall off is their current position
        for ant in left:
            last_moment = max(last_moment, ant)
            
        # Check each ant moving to the right.
        # The time it takes for these ants to fall off is the distance from them to the end of the plank
        for ant in right:
            last_moment = max(last_moment, n - ant)
            
        # The last moment when an ant falls is the maximum time calculated
        return last_moment