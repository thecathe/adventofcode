import os

for i in range(0, 25):
    day_dir = f"day{i+1:02d}"

    if not os.path.exists(day_dir):
        os.mkdir(day_dir)
    else:
        print(f"skipped: {day_dir} already exists")

    input_path = os.path.join(day_dir, "input")
    if not os.path.exists(input_path):
        input_file = open(input_path, "w")
        input_file.close()
    else:
        print(f"\tskipped: {input_path} already exists")

    day_path = os.path.join(day_dir, "run.py")
    if not os.path.exists(day_path):
        day_file = open(day_path, "w")
        day_file.write(f"\n# https://adventofcode.com/2022/day/{i}")
        day_file.close()
    else:
        print(f"\tskipped: {day_path} already exists")

print("done.")
