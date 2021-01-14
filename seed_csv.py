import csv
from faker import Faker
from random import choice, randint
import datetime
import lorem

fake = Faker()


with open('seed_data/listing.csv', mode='w') as listing_file:
    listing_writer = csv.writer(listing_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    current_time =  datetime.datetime.now()
    min = current_time.strftime("%M")
    for num in range(10):
        created_at =  current_time.strftime("%Y-%m-%d %H:"+str(int(min) + num)+":%S.%f")
        title = lorem.sentence()
        listing_user_id = num
        flagged = choice([True, False])
        listing_writer.writerow([created_at, title, listing_user_id, flagged])

with open('seed_data/comment.csv', mode='w') as comment_file:
    comment_writer = csv.writer(comment_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for num in range(10):
        listing_id = num
        user_id = num
        comment_text = fake.sentence()
        comment_writer.writerow([listing_id, user_id, comment_text])

