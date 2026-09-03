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
        
        #这个visit不代表，已经看过这个node，而是代表这个node最短已经被找到了，可以pop出去了。
        visit = set()

        h = []
        h.append([0,k])

        while h:
            #被弹出来说明这个node已经是最小了
            cur_time,cur = heapq.heappop(h)

            if cur in visit:
                continue
            else:
                visit.add(cur)
                t = cur_time
            
            for nei,time in dic[cur]:
                if nei in visit:
                    continue
                heapq.heappush(h,[time+cur_time,nei])

        return t if len(visit)==n else -1





        



        