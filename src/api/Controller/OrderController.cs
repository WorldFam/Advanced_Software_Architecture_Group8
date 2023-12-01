using Microsoft.AspNetCore.Mvc;
using MongoDB.Driver;
using api.Model;
using api.Service;

[Route("api/[controller]")]
[ApiController]
public class OrdersController : ControllerBase
{
    private readonly IMongoCollection<Order> _orderCollection;
    private readonly OrderConsumerService _orderConsumerService;

    public OrdersController(IMongoCollection<Order> orderCollection, OrderConsumerService orderConsumerService)
    {
        _orderCollection = orderCollection;
        _orderConsumerService = orderConsumerService;
    }

    [HttpGet]
    public IActionResult Get()
    {
        var orders = _orderCollection.Find(order => true).ToList();
        return Ok(orders);
    }

    [HttpPost]
    public IActionResult Post(Order order)
    {
        try
        {
        _orderCollection.InsertOne(order);

        var jsonData = Newtonsoft.Json.JsonConvert.SerializeObject(order);
        _orderConsumerService.ConsumeOrderAsync(jsonData);

        return CreatedAtRoute(nameof(Get), new { id = order.Id }, order);

        }
        catch (Exception ex)
        {
            return StatusCode(500, $"Error: {ex.Message}");
        }
    }
}
