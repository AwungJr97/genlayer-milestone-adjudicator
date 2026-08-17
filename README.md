# GenLayer Milestone Adjudicator

A GenLayer Intelligent Contract for decentralized milestone verification.

## Overview

This project evaluates submitted evidence against predefined milestone requirements
using GenLayer's consensus-based AI adjudication.

The contract produces an `APPROVED` or `REJECTED` decision and is designed for:

- Bounties
- Grants
- Freelance work
- Performance-based agreements
- Decentralized project milestones

## Concept

A requester defines a milestone requirement and a contributor submits evidence.
The Intelligent Contract asks GenLayer's validators to independently evaluate
whether the evidence sufficiently demonstrates completion.

This turns milestone approval into a transparent, reusable on-chain adjudication
primitive rather than relying on a single centralized reviewer.

## Contract

`contracts/MilestoneAdjudicator.py`

The contract stores the milestone requirement, submitted evidence, and final decision.

## Decision logic

The adjudicator approves only when the submitted evidence clearly supports the
specified requirement. Otherwise it rejects the milestone.

Possible outcomes:

- `APPROVED`
- `REJECTED`
- `PENDING` before adjudication

## Example use case

Requirement:

"Implement a responsive landing page with wallet connection."

Evidence:

- GitHub repository
- Screenshot
- Demonstration of wallet connection

The Intelligent Contract evaluates the evidence and records the resulting decision.

## Why GenLayer

Milestone verification often requires interpreting evidence rather than comparing
simple numeric values. GenLayer's Intelligent Contracts and consensus-based
adjudication make this type of subjective verification suitable for decentralized
review.

## License

MIT
