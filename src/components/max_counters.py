def max_counters(arr=[3, 4, 4, 6, 8, 1, 4, 4], n=5):
    counter = [0] * n
    max_val = 0
    counter_maxed = False

    for curr in arr:
        if curr > n:
            if not counter_maxed:
                counter = [max_val] * n
                counter_maxed = True
            print(f"curr: {curr}, counter: {counter}, max: {max_val}, counter_maxed: {counter_maxed}")
            continue

        curr -= 1
        counter[curr] += 1
        counter_maxed = False
        if counter[curr] > max_val:
            max_val = counter[curr]

        print(f"curr: {curr + 1}, counter: {counter}, max: {max_val}, counter_maxed: {counter_maxed}")

    return counter

# Test the function
max_counters()
