# Creates number files with sizes of X in terms of kilobytes


def write_file_with_kb_size(size):
    filename = str(int(size/1000))+'_kB_chunk.txt'
    with open(filename, "wb") as f:
        f.write(b'0' * size) # in kilobytes

sizes_to_make = [5000, 50000, 500000, 5000000]
for size in sizes_to_make:
    write_file_with_kb_size(size)
