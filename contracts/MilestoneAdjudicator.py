from genlayer import *
from genlayer.gl import *


class MilestoneAdjudicator(gl.Contract):
    """Consensus-based milestone evidence adjudication."""

    requirement: str
    evidence: str
    decision: str

    def __init__(self, requirement: str = "", evidence: str = ""):
        self.requirement = requirement
        self.evidence = evidence
        self.decision = "PENDING"

    @gl.public.write
    def set_case(self, requirement: str, evidence: str):
        if not requirement.strip() or not evidence.strip():
            raise ValueError("Requirement and evidence are required")
        self.requirement = requirement.strip()
        self.evidence = evidence.strip()
        self.decision = "PENDING"

    @gl.public.write
    def adjudicate(self):
        prompt = f"""
You are a neutral milestone adjudicator.

Milestone requirement:
{self.requirement}

Submitted evidence:
{self.evidence}

Determine whether the submitted evidence clearly demonstrates that the milestone
requirement has been satisfied.

Return exactly one of:
APPROVED
REJECTED

Approve only when the evidence provides sufficient support for the requirement.
"""
        result = gl.eq_principle.prompt_non_comparative(prompt)
        self.decision = result.strip().upper()

    @gl.public.view
    def get_decision(self) -> str:
        return self.decision
