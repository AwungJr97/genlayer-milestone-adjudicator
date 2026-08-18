import { readFileSync } from "fs";
import path from "path";
import { TransactionStatus } from "genlayer-js/types";

export default async function main(client) {
  const filePath = path.resolve(process.cwd(), "contracts/MilestoneAdjudicator.py");
  const contractCode = new Uint8Array(readFileSync(filePath));

  await client.initializeConsensusSmartContract();

  const txHash = await client.deployContract({
    code: contractCode,
    args: [
      "Complete the requested milestone",
      "Initial evidence submitted for review"
    ]
  });

  const receipt = await client.waitForTransactionReceipt({
    hash: txHash,
    retries: 200
  });

  if (receipt.statusName !== TransactionStatus.ACCEPTED && receipt.statusName !== TransactionStatus.FINALIZED) {
    throw new Error(`Deployment failed: ${JSON.stringify(receipt)}`);
  }

  console.log("MilestoneAdjudicator deployed", receipt);
  return receipt;
}
