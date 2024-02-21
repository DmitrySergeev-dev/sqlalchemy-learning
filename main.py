import sys
import os
from pathlib import Path
 
BASE_DIR = Path(os.path.realpath(__file__)).parent.parent
sys.path.append(BASE_DIR)


from src.database import test_db

test_db()
