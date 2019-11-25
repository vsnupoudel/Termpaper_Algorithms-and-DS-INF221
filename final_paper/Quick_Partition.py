def quick_comparison_and_swap(input_list
                              , start, end):
    pivot_last = input_list[end]
    l_id = start - 1

    for c_id in range(start, end):
        if input_list[c_id] <= pivot_last:
            l_id += 1
            input_list[l_id], input_list[c_id] =\
                input_list[c_id], input_list[l_id]

    input_list[end], input_list[l_id + 1] =\
        input_list[l_id + 1], input_list[end]

    return l_id + 1