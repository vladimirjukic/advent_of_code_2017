def redistributionCycles(data, isPartTwo):
    memoryBank = map(int, data.split())
    handledMemory = list()
    rounds = 0
    runs = 1
    if isPartTwo:
        runs = 2
    
    for run in range(0, runs):
        while memoryBank not in handledMemory:
            handledMemory.append(memoryBank[:])
            indexOfHighest = memoryBank.index(max(memoryBank))
            highestBlock = memoryBank[indexOfHighest]
            memoryBank[indexOfHighest] = 0
            i = 0
            while i < highestBlock:
                spread = (i + indexOfHighest + 1) % len(memoryBank)
                memoryBank[spread] += 1
                i += 1

            rounds += 1

        if isPartTwo and run == 0:
            handledMemory = list()
            rounds = 0
    
    if (isPartTwo):
        print "Redistribution rounds part two:", rounds
    else:
        print "Redistribution rounds part one:", rounds

f = open('input.txt', 'r')
content = f.read()
f.close()

redistributionCycles(content, False)
redistributionCycles(content, True)