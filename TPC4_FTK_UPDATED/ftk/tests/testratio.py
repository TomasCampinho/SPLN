from ftk.ratio import calculate_ratio

def test_calculate_ratio():
    freq1 = {'word1': 500000, 'word2': 300000, 'word3': 200000}
    freq2 = {'word1': 250000, 'word2': 150000, 'word3': 100000}
    expected_ratios = {'word1': 2.0, 'word2': 2.0, 'word3': 2.0}
    
    ratios = calculate_ratio(freq1, freq2)
    print("Test calculate_ratio:")
    print("Expected:", expected_ratios)
    print("Got:", ratios)
    assert ratios == expected_ratios, f"Expected {expected_ratios}, but got {ratios}"

if __name__ == "__main__":
    test_calculate_ratio()
