class Solution:
    def divisorGame(self, n: int) -> bool:

        alice = 0
        bob = 0

        for i in range(1,n):
            if n % i == 0:
                n = n - i

            if i % 2 != 0:
                alice += 1
            else:
                bob += 1

        if alice > bob:
            return True
        return False

            


        