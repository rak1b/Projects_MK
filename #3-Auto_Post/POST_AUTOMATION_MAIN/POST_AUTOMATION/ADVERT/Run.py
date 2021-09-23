from pathlib import Path
from POST_AUTOMATION.BACKEND.Main import Final_advert_run
path = Path(__file__).parent.resolve()
Final_advert_run(path)