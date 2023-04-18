# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json

class TareascrapingPipeline:
    def process_item(self, item, spider):
        # Convert item to dictionary
        item_dict = dict(item)

        # Process and store data
        with open('output.json', 'a') as f:
            f.write(json.dumps(item_dict) + '\n')
        return item
