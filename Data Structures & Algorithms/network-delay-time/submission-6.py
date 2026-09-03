class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #dic: 记录每个node，nei都是啥，然后time多久。node -- 【nei，time】的list
        #h：heap，每次弹出来min的time。(time,node).这个time表示，从node k出发到目前为止最短的time
        #min_time:一个array，index表示node，value表示min time，一开始都inf，
        #然后用dic遍历这个弹出来的node的nei，新time = 原来的time+【nei，time】里面的time，然后和min——time [nei]比较，如果大就continue，小就更新这个min time。并且加入这个h。
        #最后看min_time，如果有inf存在就返回-1说明有人到不了。否则返回max的min time
        
        dic = defaultdict(list)
        for time in times:
            start = time[0]
            end = time[1]
            dur = time[2]
            dic[start].append([end,dur])
        
        h = []
        h.append([0,k])

        min_time = [float('inf')]*(n)
        min_time[k-1]=0

        while h:
            time,cur = heapq.heappop(h)
            if time>min_time[cur-1]:
                continue
            for next_node,dur in dic[cur]:
                new_time = time+dur
                if new_time>=min_time[next_node-1]:
                    continue
                else:
                    min_time[next_node-1]=new_time
                    heapq.heappush(h,[new_time,next_node])
        res = 0
        print(min_time)
        for i in min_time:
            if i == float('inf'):
                return -1
            res = max(res,i)
        return res
        



        