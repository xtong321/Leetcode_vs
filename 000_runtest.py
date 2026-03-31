"""
write a validation function that includes:
1) test function
2) a list of test cases and expected answers
3) compare the function output and expected output, and judge correct/fail
   output #case pass test, #case fail test
"""

# this is an examplar test function
def reverse_list(lst):
    """reverse a list"""
    if not isinstance(lst, list):
        raise TypeError("input must be a list")
    return lst[::-1]

# define test case: each element is (input, expected_output)
test_cases = [
    ([1, 2, 3], [3, 2, 1]),
    ([], []),
    (['a', 'b'], ['b', 'a']),
    ([1], [1]),
    ([True, False], [False, True])
]

# run tests
def run_tests(func, cases):
    passed = 0
    for i, (input_data, expected) in enumerate(cases, start=1):
        try:
            result = func(input_data)
            if result == expected:
                print(f"✅ test {i} pass: input={input_data}, output={result}")
                passed += 1
            else:
                print(f"❌ test {i} fail: input={input_data}, output={result}, expect={expected}")
        except Exception as e:
            print(f"⚠️ test {i} error: input={input_data}, error={e}")

    print(f"\n=> test finished: {passed}/{len(cases)} passed")

if __name__ == "__main__":
    # run_tests(reverse_list, test_cases)

    base = 1000000
    rate = 0.05
    year = 23
    print(f'==> total: {format(round(base*(1+rate)**year),',d')}')
