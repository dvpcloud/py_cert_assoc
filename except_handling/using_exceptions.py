import sys
from cli import main
from cli.errors import ArgumentError

try:
    main()
except ArgumentError as err:
    print(f"Error: {err}")
    sys.exit(1)