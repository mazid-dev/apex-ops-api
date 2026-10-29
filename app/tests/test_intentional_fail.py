def test_intentional_fail():
    # DELIBERATELY failing to demonstrate CI blocks deployment.
    # Evidence captured, then change 2 -> 1 and re-push.
    assert 1 == 2, "Intentional failure for CI evidence"