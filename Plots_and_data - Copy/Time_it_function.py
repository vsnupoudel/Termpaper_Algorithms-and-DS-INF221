import numpy as np
import timeit
import copy


def timing_function(number_of_data_points
                    , sort_type,
                    randomization_type
                    , seed_number=12235):
    np.random.seed(seed_number)
    test_data = np.random.random(
        number_of_data_points, )
    test_data = list(test_data)

    if randomization_type == 'reverse':
        test_data = sorted(test_data, reverse=True)
    elif randomization_type == 'sorted':
        test_data = sorted(test_data)

    clock = timeit.Timer(stmt='sort_func (copy(data))',
                         globals={'sort_func': sort_type,
                                  'data': test_data,
                                  'copy': copy.copy})
    n_ar, t_ar = clock.autorange()
    t = clock.repeat(repeat=7, number=n_ar)
    return t
