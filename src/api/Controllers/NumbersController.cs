using api.models;
using api.persistence;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace api.Controllers;

[ApiController]
[Route("[controller]")]
public class NumbersController : ControllerBase
{
    private readonly AppDbContext _context;

    public NumbersController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet("last-ten")]
    public async Task<ActionResult<IEnumerable<NumberEntity>>> GetLastTenEntries()
    {
        List<NumberEntity> lastTenEntries = await _context.Numbers.OrderByDescending(n => n.Id).Take(10).ToListAsync();
        return Ok(lastTenEntries);
    }

    [HttpGet("row-count")]
    public async Task<ActionResult<int>> GetRowCount()
    {
        int rowCount = await _context.Numbers.CountAsync();
        return Ok(rowCount);
    }
}
