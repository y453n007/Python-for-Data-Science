import time
from datetime import datetime

seconds = time.time()
print(f"Seconds since Jan 1, 1970: {seconds} or {seconds:.2e} in scientific notation")

now = datetime.fromtimestamp(seconds)
print(now.strftime("%b %d %Y"))
