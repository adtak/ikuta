import argparse

from src.image_crawler import ImageCrawler
from src.image_storage import ImageStorage


def main():
    args = parse_arguments()
    output_dir = "results"
    results = ImageCrawler(output_dir).run(args.keyword, args.max)
    ImageStorage().push_images(output_dir, results)


def parse_arguments():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-k", "--keyword", required=True)
    arg_parser.add_argument("-m", "--max", required=True)
    return arg_parser.parse_args()


if __name__ == "__main__":
    main()
