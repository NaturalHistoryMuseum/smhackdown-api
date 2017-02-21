
import csv
import dataset

def main():

    db = dataset.connect('postgresql://postgres:asdf@127.0.0.1:5432/smhackdown')

    likes_table = db['likes']
    likes_table.delete()

    objects_table = db['objects']
    # Delete all existing objects
    objects_table.delete()


    with open('./objects.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            obj = {
                'name': row['Object Name'],
                'institution': row['Institution'],
                'object_url': row['Permanent Object URL (item landing page)'],
                'image_url': row['Image URL'],
            }
            filtered = dict(filter(lambda item: item[1] is not '', obj.items()))
            
            if len(filtered) == len(obj):
                objects_table.insert(obj)
            

              

if __name__ == "__main__":
    main()