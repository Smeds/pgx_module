from get_target_variants import GDF
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Rewrite bed to chr:start-end list. Removing wt targets or adding padding"
    )
    parser.add_argument("--input_gdf", type=str)
    parser.add_argument("--target_bed", type=str)
    parser.add_argument("--output_file", type=str)

    args = parser.parse_args(sys.argv[1:])

    input_gdf = args.input_gdf
    target_bed = args.target_bed
    output_file = args.output_file

    c_gdf = GDF(input_gdf)
    c_gdf.rsid_per_position(target_bed)
    c_gdf.write_proccessed_gdf(output_file)


if __name__ == '__main__':
    main()