#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description = "A script to extract the panel configuration XML from a Lumia's DSDT file")
parser.add_argument("inputfile", type=argparse.FileType("r"), help="Decompiled DSDT file from a Lumia device")
parser.add_argument("outputfile", type=argparse.FileType("w"), help="Output XML panel configuration file")

args = parser.parse_args()

input_list = args.inputfile.readlines()

starting_line_contains = "Name (PCFG,"
starting_line_offset = 1

ending_line = "                })\n"
ending_line_offset = 0

input_list_slice_start = input_list[input_list.index([line for line in input_list if starting_line_contains in line][0]) + starting_line_offset :]
input_list_slice_end = input_list_slice_start[: input_list_slice_start.index(ending_line) + ending_line_offset]


xml_hex_list = "".join([line[32:80] for line in input_list_slice_end]).split(", ")
xml_data = "".join(chr(int(i, 16)) for i in xml_hex_list)

args.outputfile.writelines(xml_data)
