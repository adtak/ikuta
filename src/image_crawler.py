from icrawler.builtin import BingImageCrawler


class ImageCrawler(object):
    def __init__(self) -> None:
        self.crawler = BingImageCrawler(storage={"root_dir": "result"})

    def run(self, keyword: str, max_num: str) -> None:
        filters = dict(
            type="photo",
            size="medium",
            license="creativecommons",
            layout="tall")

        self.crawler.crawl(keyword=keyword, filters=filters, max_num=max_num)


if __name__ == "__main__":
    ImageCrawler().run("painting", 1)
