# Sample API Endpoint
 Sample API Endpoint for IoT Sensors - This is an endpoint that takes a JSON request and transforms the data into a normalized format.

 The API accepts a JSON body request with no specific structure and returns an output request with a normalized format. Specific details / examples can be found below.

 ## Package Dependencies / Technical Description

Python Version: `Python 3.8.3` </br>
Flask Version: `Flask 1.1.2`

Refer to `setup.sh` to run app with dependencies installed. The setup script is developed to run on macOS or Linux systems.

## Example
**Input**:
```
{
 "deviceId": "sensor-1",
 "timestamp": "2020-01-02T03:45:00",
 "readingA": 212.0,
 "readingB": "high",
 "activated": "2020-01-02T03:42:55"
}
```

**Output**:

```
{
    "source": "sensor-1",
    "timestamp": 1577954700000,
    "data": {
        "readingA": {
            "string": "212.0",
            "numeric": 212.0,
            "datetime": 212000
        },
        "readingB": {
            "string": "high",
            "numeric": null,
            "datetime": null
        },
        "activated": {
            "string": "2020-01-02T03:42:55",
            "numeric": null,
            "datetime": 1577954575000
        }
    }
}
```

