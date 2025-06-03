from pathlib import Path
#from src.data.download import sha256sum
import sys
from pathlib import Path

# Adiciona o diretório /src ao PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from data.download import sha256sum

def test_sha256sum():
    test_path = Path(__file__).resolve().parents[1] / "data" / "raw" / "german_credit.csv"
    if not test_path.exists():
        assert True  # skip test if file not yet downloaded
    else:
        hash = sha256sum(test_path)
        assert len(hash) == 64
