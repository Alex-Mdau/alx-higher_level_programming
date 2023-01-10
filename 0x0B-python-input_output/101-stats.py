#!/usr/bin/python3
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
 """

def print_stats(size, status_code):
    """Prints accumulated metrics.
    args:
    size (int): The accumulated read file size.
    status_code (dict): the accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys
    from collections import defaultdict

    total_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line_number, line in enumerate(sys.stdin, 1):
            parts = line.split()
            if len(parts) != 6:
                print("Invalid input format on line", line_number)
            continue

            ip, _, date, request, status_code, file_size = parts
            total_size += int(file_size)
            status_codes[status_code] += 1

            if line_number % 10 == 0:
                print("Total file size:", total_size)
            for status_code in sorted(status_codes.keys()):
                print(status_code + ":", status_codes[status_code])

            except KeyboardInterrupt:
                print("Total file size:", total_size)
            for status_code in sorted(status_codes.keys()):
                print(status_code + ":", status_codes[status_code])
                sys.exit()

