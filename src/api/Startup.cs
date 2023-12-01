using MongoDB.Driver;
using api.Model;
using api.Service;

public class Startup
{
    public IConfiguration Configuration { get; }

    public Startup(IConfiguration configuration)
    {
        Configuration = configuration;
    }

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddControllers();
        services.AddScoped<OrderConsumerService>();

        // Configure MongoDB
        var mongoConnectionString = Configuration.GetConnectionString("MongoDb");
        services.AddSingleton<IMongoClient>(new MongoClient(mongoConnectionString));
        services.AddScoped<IMongoDatabase>(provider =>
        {
            var client = provider.GetService<IMongoClient>();
            return client.GetDatabase("orderDb");
        });
        services.AddScoped<IMongoCollection<Order>>(provider =>
        {
            var database = provider.GetService<IMongoDatabase>();
            return database.GetCollection<Order>("order");
        });
    }

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        if (env.IsDevelopment())
        {
            app.UseDeveloperExceptionPage();
        }

        app.UseRouting();
        app.UseEndpoints(endpoints =>
        {
            endpoints.MapControllers();
        });
    }
}
