# pureapiDjango
pure Django api using serializer

- Python has a built in package called json, which is used to work wih json data

- dumps(data) - this is used to convert python object into json string.
- ex:

```
import json
python_data = {'name':'sonam', 'roll':101}
json_data = json.dumps(python_data)
print(json_data)
O/P : {"name":"sonam", "roll" : 101}
```

- loads(data) -> This is use to parse json string

- Ex:
```
import json
json_data = {"name": "sonam", "roll": 101}
parsed_data = json.loads(json_data)
print(parsed_data)
O/P: {'name':'sonam', 'roll':101}
```

## Serializers:
- in drf serializers are responsible for converting complex data such as querysets and model instances to native python datatypes (called serialization)
- that can then be easily rendered into JSON, XML which is understandable by frontend

- complex data type to python native datatype (this process is called serialization)
- pytohn native datatype to Json data this is called Render into Json



## Serialization process with code
- creating query set
- stu = Student.objects.all()
- serializer = StudentSerializer(stu, many=True)
- here we get values insideserializer.data
- Now convert serialized data into json so use JSONRENDERER

- from rest_frameowkr.renderers import JSONRenderer 
- json_data = JSONRenderer().render(serializer.data)

# Serialization

- COMPLEX DATA TYPE --> (serialization) --> PYTHON NATIVE DATATYPE --> (render into json) --> JSON DATA 

# De-serialization

- JSON DATA -->(parse data)--> PYTHON NATIVE DATATYPE --> (De-Serialization)--> COMPLEX DATATYPE

# BytemIO()
```
import io
stream = io.BytemIO(json_data)

```
# JSONPARSER()

this is used to parse json data to pytohn native datatype

```
from rest_framework.parser import JSONParser
parsed_data = JSONParser().parser(stream)

```
# De serialization

- It allows parsed data to be converted back into complex types, after first validating the incoming data.

- Steps
- Creating Serializer Object
```
serializer = StudentSerializer(data = parsed_data)
```
- Validated Data 
```
serializer.is_valid()
```
- if serializer is valid then we get the results in serializer.validated_data
- if not the we get serializer.errors

# demo
