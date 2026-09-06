class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []
        for token in tokens:
            if token.isalnum():
                q.append(token)
                print(q)
            else:
                print(q)
                second_num = int(q.pop())
                first_num = int(q.pop())
                if token == '+':
                    cur_res = first_num+second_num
                elif token == '-':
                    cur_res = first_num-second_num
                elif token == '*':
                    cur_res = first_num*second_num
                else: 
                    cur_res = first_num/second_num
                
                q.append(cur_res)
        return q.pop()