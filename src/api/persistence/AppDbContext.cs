using api.models;
using Microsoft.EntityFrameworkCore;

namespace api.persistence;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    public DbSet<NumberEntity> Numbers { get; set; }
}
