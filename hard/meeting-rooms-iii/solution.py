# spador

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        freeroom = [i for i in range(n)]
        busyroom = []       # (end_time, meeting_room)
        booked = [0] * n    # (to track how many times each room was booked)

        for start, end in meetings:
            while busyroom and start >= busyroom[0][0]:
                _, room = heapq.heappop(busyroom)
                heapq.heappush(freeroom, room)

            # if all the meeting room are busy
            if not freeroom:
                e, r = heapq.heappop(busyroom)
                end += e - start
                heapq.heappush(freeroom, r)

            # book a meeting room
            m = heapq.heappop(freeroom)
            heapq.heappush(busyroom, (end, m))
            booked[m] += 1

        return booked.index(max(booked))
