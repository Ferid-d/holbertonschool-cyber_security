#!/usr/bin/python3
"""
Locates and replaces a string in the heap of a running process.
Usage: read_write_heap.py pid search_string replace_string
"""

import sys

def print_usage_and_exit():
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)

def read_write_heap():
    # Argument validation
    if len(sys.argv) != 4:
        print_usage_and_exit()

    pid = sys.argv[1]
    search_str = sys.argv[2]
    replace_str = sys.argv[3]

    if len(replace_str) > len(search_str):
        # We generally avoid writing more bytes than the original 
        # to prevent corrupting adjacent memory (buffer overflow).
        print("Error: replace_string cannot be longer than search_string")
        sys.exit(1)

    try:
        # 1. Find the heap range in /proc/[pid]/maps
        maps_path = f"/proc/{pid}/maps"
        mem_path = f"/proc/{pid}/mem"
        
        heap_start = None
        heap_end = None

        with open(maps_path, 'r') as maps_file:
            for line in maps_file:
                if "[heap]" in line:
                    # Line format: 555e646e0000-555e64701000 rw-p 00000000 00:00 0 [heap]
                    parts = line.split()
                    addr_range = parts[0].split('-')
                    heap_start = int(addr_range[0], 16)
                    heap_end = int(addr_range[1], 16)
                    break

        if heap_start is None:
            print(f"Error: Could not find heap for process {pid}")
            sys.exit(1)

        print(f"[*] Found heap at: {hex(heap_start)} - {hex(heap_end)}")

        # 2. Open the process memory
        # 'rb+' allows reading and writing in binary mode
        with open(mem_path, 'rb+') as mem_file:
            # 3. Seek to the start of the heap and read it
            mem_file.seek(heap_start)
            heap_data = mem_file.read(heap_end - heap_start)

            # 4. Find the string
            try:
                index = heap_data.index(bytes(search_str, "ascii"))
            except ValueError:
                print(f"Error: String '{search_str}' not found in heap.")
                sys.exit(1)

            print(f"[*] Found '{search_str}' at offset {hex(index)}")

            # 5. Replace the string
            # Move the file pointer to the specific offset of the string
            mem_file.seek(heap_start + index)
            mem_file.write(bytes(replace_str + '\0', "ascii")) # Null terminate to be safe
            
            print(f"[*] Successfully replaced with '{replace_str}'")

    except PermissionError:
        print("Error: Permission denied. Try running with sudo.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    read_write_heap()
