class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        total = n * 2
        j = 0

        reservedSeats.sort()

        while j < len(reservedSeats):

            curr_row = reservedSeats[j][0]

            isfl = False   # seats 2,3,4,5
            ismid = False  # seats 4,5,6,7
            isfr = False   # seats 6,7,8,9

            while j < len(reservedSeats) and reservedSeats[j][0] == curr_row:

                seat = reservedSeats[j][1]

                if seat in [2, 3, 4, 5]:
                    isfl = True

                if seat in [4, 5, 6, 7]:
                    ismid = True

                if seat in [6, 7, 8, 9]:
                    isfr = True

                j += 1
            if not isfl and not isfr:
                continue
            elif not isfl or not isfr:
                total -= 1
            elif not ismid:
                total -= 1
            else:
                total -= 2

        return total