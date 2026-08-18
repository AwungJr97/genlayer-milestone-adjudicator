# GenLayer Milestone Adjudicator

A decentralized milestone verification app built around a GenLayer Intelligent Contract.

## What it does

Users submit a milestone requirement and supporting evidence. The Intelligent Contract stores the case and asks GenLayer's nondeterministic validator process to adjudicate whether the evidence is sufficient. The result is normalized to `APPROVED` or `REJECTED` and can be read back by the frontend.

## Architecture

- `contracts/MilestoneAdjudicator.py` — GenLayer Intelligent Contract.
- `frontend/index.html` — browser UI using GenLayerJS to write the case, trigger adjudication, wait for consensus, and read the decision.
- `deploy/001_deploy.ts` — deployment workflow.
- `tests/test_milestone_adjudicator.py` — contract smoke test.

## GenLayer role

The core decision is intentionally nondeterministic: `gl.eq_principle.prompt_non_comparative(...)` lets validators evaluate the evidence while GenLayer consensus determines the accepted execution result.

## Run

Install dependencies with `npm install`, configure the GenLayer CLI/network, then run `npm run deploy`. Open `frontend/index.html` and provide the deployed contract address.

This project is intended for GenLayer Studio/Studionet experimentation and milestone-evidence workflows.
