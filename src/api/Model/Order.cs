using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace api.Model;

public class Order
{
    [BsonId]
    [BsonRepresentation(BsonType.ObjectId)]
    public string? id { get; set; }
    
    [BsonElement("customer")]
    public string customer { get; set; }

    [BsonElement("size")]
    public string size { get; set; }

    [BsonElement("amount")]
    public string amount { get; set; }

    [BsonElement("timestamp")]
    [BsonDateTimeOptions(Kind = DateTimeKind.Utc)]
    public DateTime timestamp { get; set; } = DateTime.UtcNow;

}
