#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    pid = sys.argv[1]
    search_string = sys.argv[2].encode('ascii')
    replace_string = sys.argv[3].encode('ascii')

    with open(f"/proc/{pid}/maps", 'r') as maps_file:
        for line in maps_file:
            if "[heap]" in line:
                address_range = line.split(' ')[0]
                start_hex, end_hex = address_range.split('-')
                heap_start = int(start_hex, 16)
                heap_end = int(end_hex, 16)
                break

    with open(f"/proc/{pid}/mem", 'r+b') as mem_file:
        mem_file.seek(heap_start)
        heap_data = mem_file.read(heap_end - heap_start)

        offset = heap_data.find(search_string)
        if offset == -1:
            print("Error: String not found in heap.")
            sys.exit(1)

        mem_file.seek(heap_start + offset)

        padded_replace = replace_string.ljust(len(search_string), b'\x00')
        mem_file.write(padded_replace)


if __name__ == "__main__":
    main()
