def test_intentional_fail():
    # DELIBERATELY failing to demonstrate CI blocks deployment.
    # Evidence captured, now fixed.
    assert 1 == 1, "Fixed after capturing CI RED evidence"