##Spador

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n + 1):
            fizz, buzz = True, True
            if i % 3:
                fizz = False
            if i % 5:
                buzz = False

            if fizz and buzz:
                answer.append("FizzBuzz")
            elif fizz:
                answer.append("Fizz")
            elif buzz:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer


    # can also use divisibility rules of 3 and 5 instead of taking mod.
    # divisible by 3: if sum of digits is divisible by 3
    # divisible by 5: if the least significant digit is 0 or 5
