
for i in range(1, 25)
    day_dir = "day$(lpad(i,2,'0'))"

    if !(isdir(day_dir))
        mkdir(day_dir)
    end

    touch("$(day_dir)/input")

    file_path = "$(day_dir)/run.jl"
    touch(file_path)

    open(file_path, "w") do file
        write(file, "\n# https://adventofcode.com/2023/day/$(i)")
    end

end

print("done.")