const { MongoClient } = require('mongodb');

const uri = 'mongodb://localhost:27017';
const dbName = 'admin';

async function main() {
    const client = new MongoClient(uri);

    try {
        // 连接到 MongoDB 数据库
        await client.connect();
        console.log('Connected to MongoDB');

        // 获取 admin 数据库对象
        const adminDb = client.db(dbName).admin();

        console.log('Database:', adminDb.databaseName);

        // 创建管理员用户
        await adminDb.command({
            createUser: 'adminUser',
            pwd: '153719',
            roles: [{ role: 'root', db: 'admin' }]
        });
        console.log('Admin user created successfully.');

    } catch (err) {
        console.error('Error:', err.stack);
    } finally {
        // 关闭数据库连接
        await client.close();
        console.log('Disconnected from MongoDB');
    }
}

// 执行主函数
main().catch(console.error);
