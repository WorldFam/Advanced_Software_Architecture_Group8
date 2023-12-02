using Microsoft.AspNetCore.Mvc;
using MongoDB.Driver;
using api.Model;
using api.Service;
using System.Text.Json;

[Route("api/[controller]")]
[ApiController]
public class OrderController : ControllerBase
{
    private readonly IMongoCollection<Order> _orderCollection;
    private readonly OrderConsumerService _orderConsumerService;

    public OrderController(IMongoCollection<Order> orderCollection, OrderConsumerService orderConsumerService)
    {
        _orderCollection = orderCollection;
        _orderConsumerService = orderConsumerService;
    }

    [HttpGet]
    public IActionResult Get()
    {
        var orders =  _orderCollection.Find(order => true).ToList();
        return Ok(orders);
    }

    [HttpPost]
    public async Task<IActionResult> Post(Order order)
    {
        try
        {
        _orderCollection.InsertOne(order);
        var jsonOrder = JsonSerializer.Serialize(order);
        Console.WriteLine(jsonOrder);

        var response = await  _orderConsumerService.ConsumeOrderAsync(jsonOrder);
        return Ok(response);
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"Error: {ex.Message}");
        }
    }
}
