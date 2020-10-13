from src.image_crawler import ImageCrawler
from src.image_storage import ImageStorage


def main():
    output_dir = "results"
    results = ImageCrawler(output_dir).run("painting", 3)
    ImageStorage().push_images(output_dir, results)


if __name__ == "__main__":
    main()
