# 7z a -mx9 -tzip -r dataset.zip ./images
from pathlib import Path
import shutil
from tqdm import tqdm


def get_new_name(old_name: str) -> str:
    aux: str = old_name.split(".")
    new_name: str = f"{aux[0]}_mask.{aux[1]}"
    return new_name


mask_p = Path("./masks/0").glob("*")

for msk in tqdm(mask_p):
    new_name = get_new_name(msk.name)
    shutil.copy(msk, f"./images/{new_name}")
