from src.image_crawler import ImageCrawler
from src.image_storage import ImageStorage


def main():
    ImageCrawler().run("painting", 1)
    ImageStorage().push_images()


if __name__ == "__main__":
    main()
