This is a basic description of the interactions with the REST API server.
The easiest way to run it is `docker run -p 8000:8000 <image-name>`.
To make sure it runs try `curl localhost:8000/jam`

| Endpoint      | Method | Notes | Examples |
| ----------- | ----------- | --- | --- |
| /db/\<action>      | POST       | action is either "load" or "save"| localhost:8000/db/save |
| /jam   | GET |  | localhost:8000/jam |
| /jam/\<flavour>   | GET |  | localhost:8000/jam/blueberry | 
| /jam/\<flavour>   | PATCH | Must have query parameter action (i.e. ?action=) <br> with value "eat" or "buy" | localhost:8000/jam/blueberry?action=eat | 

