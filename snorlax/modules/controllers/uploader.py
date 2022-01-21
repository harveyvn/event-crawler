import csv
from filestack import Client
from .reader import Reader


class Uploader:
    """
    The Uploader class declares the interface that create and upload csv file.
    """
    @staticmethod
    def write_file():
        """
        Write the db to a demo.csv file.
        """
        reader = Reader()
        reader.connect()
        ids = reader.get_events()

        header = ["id", "title", "cover", "locations", "artists", "songs", "date"]

        with open("demo.csv", 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            for id in ids:
                data = [
                    id,
                    reader.get_title(id),
                    reader.get_cover(id),
                    reader.get_locations(id),
                    reader.get_artists(id),
                    reader.get_songs(id),
                    reader.get_date(id)
                ]
                writer.writerow(data)

    @staticmethod
    def upload_file():
        """
        Upload a demo.csv file and retrieve a link

        Returns:
            link (str): download link
        """
        client = Client("AP0pry0vFSFGOE5h40Lqfz")
        demo_file = client.upload(filepath="demo.csv")
        return demo_file.url

