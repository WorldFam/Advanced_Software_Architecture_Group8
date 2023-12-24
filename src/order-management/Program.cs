using System;
using MongoDB.Driver;
using Logs.model;
using DotNetEnv;

class Program
{
    static void Main()
    {
        DotNetEnv.Env.Load();

        string connectionString = Environment.GetEnvironmentVariable("ATLAS_URI");
        // MongoDB client
        MongoClient client = new MongoClient(connectionString);
        // Accessing a database
        IMongoDatabase database = client.GetDatabase(Environment.GetEnvironmentVariable("DB_NAME"));
        // Accessing a collection
        IMongoCollection<Log> collection = database.GetCollection<Log>("logs");
        // Now you can perform CRUD operations on the collection
        Console.WriteLine("Connected to MongoDB!");
        // Don't forget to close the connection when done
        // client.DropDatabase(Environment.GetEnvironmentVariable("DB_NAME")); 
    }

}