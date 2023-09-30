using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace api.models;

[Table("numbers")]
public class NumberEntity
{
    [Key]
    [Column("id")]
    public int Id { get; set; }

    [Column("value")]
    public int value { get; set; }
}
