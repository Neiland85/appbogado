import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from appbogado.legal_processing import leer_texto_legal, procesar_texto_legal

