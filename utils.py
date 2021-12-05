import collections
from bisect import bisect


def makeInterval(low, high, nIntervals):
    distance = high - low
    if distance < nIntervals:
        points = list(range(low, high + 1))
    else:
        interval = int(round(((high - low + 1) / nIntervals)))
        points = list(range(low, high, interval))
    return points


def showDistribution(data, itemLabel, amountLabel, maxBuckets=50, maxAmounts=50):
    maxFreq = int(round(max(data)))
    lenBucketInt = len(str(maxFreq))

    buckets = collections.Counter()

    for (freq, nItems) in data.items():
        buckets[int(round(freq))] += nItems

    maxAmount = max(buckets.values())
    lenAmountInt = len(str(maxAmount))
    amountPoints = makeInterval(0, maxAmount + 1, maxAmounts)

    lines = []
    labelLength = max((len(amountLabel), lenBucketInt))
    valueLength = max((len(itemLabel), maxAmounts + lenAmountInt))

    lines.append("─" * labelLength + "┬" + "─" * valueLength)
    lines.append(f"{amountLabel:<{labelLength}}│{itemLabel}")
    lines.append("─" * labelLength + "┼" + "─" * valueLength)

    for (bucket, nItems) in sorted(buckets.items(), key=lambda x: -x[0]):
        valueIndex = bisect(amountPoints, nItems)
        valueRep = "■" * valueIndex + str(nItems)
        lines.append(f"{bucket:>{labelLength}}│{valueRep}")
    lines.append("─" * labelLength + "┴" + "─" * valueLength)
    print("\n".join(lines))
