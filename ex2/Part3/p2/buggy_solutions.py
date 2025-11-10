def func2(cnt1, cnt2, cnt3, cnt4):
    total = cnt1 + cnt2 + cnt3 + cnt4

    # 1. Total length must be even
    if total % 2 != 0:
        return 0

    # 2. Compute overall imbalance
    # () adds 0, ( adds +1, ) adds -1, )( adds -1
    imbalance = cnt1 + cnt3 - cnt4

    if imbalance != 0:
        return 0

    # 3. For each dangerous )(, we need to "use" a ( from the available count
    # Each )( introduces a closing as the first bracket, so it must be wrapped
    if cnt3 > cnt1:
        return 0

    return 1