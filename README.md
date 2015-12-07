# PyWeatherServer
**Fake weather service to test XML-RPC communication.**

**Usage:**
    
    python -m weatherserver [-h] [-l {DEBUG,INFO,WARNING,ERROR}] 
                            [-n NAME] [-s SERVER] [-p PORT] -d DATA
   
**Arguments:**
    
    -h  show this help message and exit
    -d DATA  file with weather data
    -l LOGLEVEL  one of *DEBUG INFO WARNING ERROR*
    -n NAME  name of the service
    -s SERVER  host to listen
    -p PORT  port to listen

**Sample `.ini` file with fake weather data is provided for convinience:**
    
    ; location config
    [config]
    port = 9000
    host = localhost
    name = Location Name
   
    ; fake weather data
    [site]
    temperature = 7.4
    humidity = 45
    windspeed = 15.5
    pressure = 1020
