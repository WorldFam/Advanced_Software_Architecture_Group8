using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace api.Service;
public class OrderConsumerService
{
    private readonly HttpClient _httpClient;

    public OrderConsumerService()
    {
        _httpClient = new HttpClient();
    }

    public async Task<string> ConsumeOrderAsync(string jsonData)
    {
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

        var response = await _httpClient.PostAsync("http://scheduler:9090/v1/order", content);

        response.EnsureSuccessStatusCode();

        return await response.Content.ReadAsStringAsync();
    }
}
