const BASE_URL = 'http://localhost:8090';

export const fetchData = async () => {
    const response = await fetch(`${BASE_URL}/api/order`);
    const data = await response.json();
    return data;
};

export const postData = async (newForecast) => {
    const response = await fetch(`${BASE_URL}/api/order`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newForecast),
    });

    if (!response.ok) {
        throw new Error(`Failed to add order: ${response.status}`);
    }
};
