# this program is for finding the closest point in 2-D
import sys

def xcor(pnt):
    return pnt[0]

def ycor(pnt):
    return pnt[1]

def findDist(pnt1, pnt2):
    return ((pnt1[0] - pnt2[0]) ** 2 + (pnt1[1] - pnt2[1]) ** 2) ** 0.5

def bruteForce(pnts, n):
    minD = sys.float_info.max
    for i in range(n):
        for j in range(i+1, n):
            curD = findDist(pnts[i], pnts[j])
            if curD < minD:
                minD = curD
    return minD

def acrossDist(stp, d, n):
    minD = d
    for i in range(n):
        for j in range(i+1, n):
            if stp[j][1] - stp[i][1] > minD:
                break
            minD = findDist(stp[i], stp[j])
    return minD

def findClosest(px, py, n):
    if n <= 3:
        return bruteForce(px, n)

    mid = n // 2
    mp = px[mid][0]
    pyl, pyr = [], []
    for i in range(n):
        if py[i][0] <= mp:
            pyl.append(py[i])
        else:
            pyr.append(py[i])

    dl = findClosest(px[: mid+1], pyl, mid+1)
    dr = findClosest(px[mid+1 :], pyr, n-mid-1)

    d = min(dl, dr)
    stp = []
    for i in range(n):
        if abs(px[i][0] - mp) < d:
            stp.append(px[i])

    return min(d, acrossDist(stp, d, len(stp)))

cordXy = [(1,2),(3,7),(5,8),(7,2),(9,1)]
px = sorted(cordXy, key = xcor)
py = sorted(cordXy, key = ycor)
print(findClosest(px, py, len(cordXy)))