import ai

def test_connect_task():
    assert ai.connect_task("please only respond with 1") == "1"
