from pathlib import Path
import sys

# tests/ is expected here; adjust .parents[1] if you place this file somewhere else.
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))
