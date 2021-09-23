from pathlib import Path
# from POST_AUTOMATION.BACKEND.Main import Final_NationBuilder_run
from POST_AUTOMATION.BACKEND.Main import Final_NationBuilder_run
path = Path(__file__).parent.resolve()
print(path)
Final_NationBuilder_run(path)