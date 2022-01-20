import logging
from modules.spiders import EventSpider, ProgramSpider
from modules import CONST
from scrapyscript import Job, Processor
from yaspin import yaspin

logging.getLogger("scrapy").propagate = False

if __name__ == '__main__':
    urls = ["https://www.lucernefestival.ch/en/program/summer-festival-22",
            "https://www.lucernefestival.ch/en/program/mendelssohn-festival-22"]

    with yaspin(text="Crawling events!", color="yellow") as spinner:
        processor = Processor(settings=None)
        job = Job(EventSpider, url=urls[1])
        events = processor.run(job)

        if len(events) > 0:
            spinner.ok(f'✅ Successful! Crawled {len(events)} events!')
        else:
            spinner.fail("💥 Failed! Program exits!")
            exit()

    for i, event in enumerate(events):
        with yaspin(text=f'Crawling a program from an event {i + 1}/{len(events)}!', color="yellow") as spinner:
            link = event[CONST.LINK]
            job = Job(ProgramSpider, url=link)
            try:
                event[CONST.PROGRAM] = processor.run(job)[0]
                if len(event[CONST.PROGRAM][CONST.ARTISTS]) > 0 and len(event[CONST.PROGRAM][CONST.SONGS]) > 0:
                    spinner.ok(f'✅ Successful! Crawled {len(event[CONST.PROGRAM][CONST.SONGS])} songs!')
            except:
                spinner.fail(f'💥 Failed! Event ID: {i}!')
