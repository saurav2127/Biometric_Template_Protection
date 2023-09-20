import glob
from pathlib import Path


for fn in Path("folder_name").glob("*"):
    file_base_name = "-".join(fn.stem.split("-")[:-1])
    file_count = len(glob.glob1("folder_name", f"{file_base_name}*"))
    if file_count > 1 or Path(file_base_name).is_dir():
        outdir = Path("folder_name") / file_base_name
        outdir.mkdir(exist_ok=True)
        fn.rename(outdir / fn.name)