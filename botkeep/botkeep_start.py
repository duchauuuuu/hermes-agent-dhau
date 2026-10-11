import os
import sys
from pathlib import Path

from dotenv import load_dotenv

app_dir = Path(__file__).resolve().parent
repo_dir = app_dir.parent

# Đọc .env do Botkeep quản lý tại thư mục gốc.
load_dotenv(repo_dir / ".env")

# Lưu cấu hình, bộ nhớ và phiên trò chuyện.
state_dir = app_dir / "hermes-data"
state_dir.mkdir(parents=True, exist_ok=True)
os.environ["HERMES_HOME"] = str(state_dir)

# Dùng Hermes đã cài từ requirements.txt.
# Tránh nhập nhầm mã nguồn phiên bản mới trong repo.
sys.path[:] = [
    entry
    for entry in sys.path
    if Path(entry or os.getcwd()).resolve() != repo_dir
]
os.chdir(app_dir)

from hermes_cli.main import main

if __name__ == "__main__":
    sys.argv = ["hermes", "gateway", "run"]
    main()
