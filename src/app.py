"""JSONL interface for the recovery gate POC."""
import json
import sys
from src.recovery import Signals, plan


def evaluate(payload: dict) -> dict:
    return {"input": payload, "decision": plan(Signals(**payload))}


def main() -> None:
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(evaluate(json.loads(line))))


if __name__ == "__main__":
    main()
