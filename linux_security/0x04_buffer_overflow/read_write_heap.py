#!/usr/bin/python3

import sys

def read_write_heap():
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    pid = sys.argv[1]
    search_str = sys.argv[2]
    replace_str = sys.argv[3]

    if len(replace_str) > len(search_str):
        sys.exit(1)

    try:
        maps_path = "/proc/{}/maps".format(pid)
        mem_path = "/proc/{}/mem".format(pid)
        
        heap_start = None
        heap_end = None

        with open(maps_path, 'r') as maps_file:
            for line in maps_file:
                if "[heap]" in line:
                    parts = line.split()
                    addr_range = parts[0].split('-')
                    heap_start = int(addr_range[0], 16)
                    heap_end = int(addr_range[1], 16)
                    break

        if heap_start is None:
            sys.exit(1)

        print("[*] Found heap at: {} - {}".format(hex(heap_start), hex(heap_end)))

        with open(mem_path, 'rb+') as mem_file:
            mem_file.seek(heap_start)
            heap_data = mem_file.read(heap_end - heap_start)

            try:
                index = heap_data.index(bytes(search_str, "ascii"))
            except ValueError:
                sys.exit(1)

            print("[*] Found '{}' at offset {}".format(search_str, hex(index)))

            mem_file.seek(heap_start + index)
            mem_file.write(bytes(replace_str, "ascii"))
            
            print("[*] Successfully replaced with '{}'".format(replace_str))

    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    read_write_heap()
