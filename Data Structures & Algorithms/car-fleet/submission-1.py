class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse = True)
        times = [(target-pos)/spe for pos,spe in cars]
        print(f"times{times}")
        stack = []
        for time in times:
            if len(stack) == 0:
                stack.append(time)
            elif time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)


            








        