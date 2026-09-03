class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)% groupSize!=0:
            return False
        g_num = int(len(hand)/groupSize)
        card_book = {}
        for h in hand:
            card_book[h] = card_book.get(h,0)+1

        for i in range(g_num):
            min_hand = min(card_book)
            card_book[min_hand]-=1
            if card_book[min_hand]<=0:
                card_book.pop(min_hand)
            print(f"min hand = {min_hand}")
            for g in range(groupSize-1):
                cur_hand = min_hand+1
                print(f"cur_hand = {cur_hand}")
                if cur_hand not in card_book:
                    return False
                card_book[cur_hand]-=1
                if card_book[cur_hand]<=0:
                    print(f"card_book[cur_hand] = {card_book[cur_hand]}")
                    card_book.pop(cur_hand)
                min_hand = cur_hand
        return True


