using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace Logs.model
{
    public class Log
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }

        [BsonElement("programName")]
        public string ProgramName { get; set; }

        [BsonElement("message")]
        public string Message { get; set; }
    }
}

