import os
import sys
from pathlib import Path
from dotenv import load_dotenv

root = Path(__file__).resolve().parent
load_dotenv(root / ".env")

state = root / "hermes-data"
state.mkdir(exist_ok=True)
os.environ["HERMES_HOME"] = str(state)

from hermes_cli.main import main

if __name__ == "__main__":
    sys.argv = ["hermes", "gateway", "run"]
    main()
