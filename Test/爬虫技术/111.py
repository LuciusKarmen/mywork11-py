from pymongo import MongoClient

# 1. 连接到 MongoDB 服务器
# 假设 MongoDB 运行在本地，默认端口 27017
client = MongoClient('mongodb://localhost:2701/')

# 2. 选择或创建一个数据库
# 如果数据库 'mycompany' 不存在，MongoDB 会在你第一次插入数据时创建它
db = client['mycompany']  # 推荐使用这种字典式访问

# 或者等价写法: db = client.mycompany

# 3. 选择或创建一个集合 (相当于 SQL 中的表)
collection = db['employees']

# 4. 插入一条数据 (这一步会真正触发数据库和集合的创建)
employee = {
    "name": "张三",
    "department": "技术部",
    "position": "Python 工程师"
}

# insert_one 插入单条文档
result = collection.insert_one(employee)

print(f"✅ 文档插入成功！ID: {result.inserted_id}")

# 5. 打印数据库和集合信息

# 打印所有数据库名称
print("\n📋 所有数据库:")
print(client.list_database_names())

# 打印当前数据库中的所有集合名称
print(f"\n📂 数据库 '{db.name}' 中的集合:")
print(db.list_collection_names())

# 6. 查询并打印刚插入的数据
print(f"\n🔍 查询 'employees' 集合中的所有数据:")
for doc in collection.find():
    print(doc)

# 7. 关闭连接 (最佳实践)
client.close()