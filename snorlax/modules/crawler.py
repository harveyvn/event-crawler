from scrapyscript import Processor, Job
from yaspin import yaspin
from .spiders import EventSpider, ProgramSpider
from .constant import CONST


class Crawler:
    def __init__(self, url):
        self.url = url
        self.events = []
        self.get_events()
        self.get_programs()

    def get_events(self):
        with yaspin(text="Crawling events!", color="yellow") as spinner:
            processor = Processor(settings=None)
            job = Job(EventSpider, url=self.url)
            events = processor.run(job)

            if len(events) > 0:
                spinner.ok(f'✅ Successful! Crawled {len(events)} events!')
                self.events = events
            else:
                spinner.fail("💥 Failed! Program exits!")

    def get_programs(self):
        for i, event in enumerate(self.events):
            with yaspin(text=f'Crawling a program from an event {i + 1}/{len(self.events)}!',
                        color="yellow") as spinner:
                link = event[CONST.LINK]
                job = Job(ProgramSpider, url=link)
                try:
                    processor = Processor(settings=None)
                    self.events[i][CONST.PROGRAM] = processor.run(job)[0]
                    if len(event[CONST.PROGRAM][CONST.ARTISTS]) > 0 and len(event[CONST.PROGRAM][CONST.SONGS]) > 0:
                        spinner.ok(f'✅ Successful! Crawled {len(event[CONST.PROGRAM][CONST.SONGS])} songs!')
                except:
                    spinner.fail(f'💥 Failed! Event ID: {i}!')
