def test_contract_shape():
    source = open("contracts/MilestoneAdjudicator.py", encoding="utf-8").read()
    assert "class MilestoneAdjudicator" in source
    assert "prompt_non_comparative" in source
    assert "def set_case" in source
    assert "def adjudicate" in source
    assert "def get_decision" in source
