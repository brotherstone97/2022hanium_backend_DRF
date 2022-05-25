from pymongo import MongoClient

# MongoClient Connection Object
conn = MongoClient(host='127.0.0.1', port=27017)

# Connected DB
db = conn.get_database('drug_information')
# Collection
col_drugs = db.get_collection('drugs')

#전체를 조회하는 함수
def read_all():
    result = []
    items = col_drugs.find()
    for item in items:
        result.append(item)
    return result

#특정 키워드가 포함된 필드를 조회
def read_by_title(title):
    print(col_drugs.find(title))

read_all()