try:
    import androidhelper
except ImportError:
    print("\033[91;1mMódulo: \033[92;1mandroidhelper\033[m \033[91;1mnão encontrado\033[m")
    print("Por favor, instale este módulo")
    sys.exit()
try:
    import os
except ImportError:
    print("\033[91;1mMódulo: \033[92;1mos\033[m \033[91;1mnão encontrado\033[m")
    print("Por favor, instale este módulo")
    sys.exit()
try:
    from datetime import datetime
except ImportError:
    print("\033[91;1mMódulo: \033[92;1mdatetime\033[m \033[91;1mnão encontrado\033[m")
    print("Por favor, instale este módulo")