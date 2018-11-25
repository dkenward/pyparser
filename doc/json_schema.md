# Schema
Most objects are defined under the mylib.io.json.schema.definitions.json file. 

## Definitions.json
1. MasterObject :-1:
    - Description: `MasterObject describes a master object to which all other objects are associated to in some way.`
    - Subclasses: _None_
    - Uses: `Function`
2. Frame
    - Description: `Holds multiple rows of data. Similar to a pandas DataFrame.`
    - Subclasses: `SpecialFrame`
    - Uses: `Row`

3. SpecialFrame
    - _todo_

4. Row
    - _todo_

5. DataPoint
    - Description: <code>DataPoint has a single point in the data. Nothing more than a dtype with a timestamp and a [trigger](./triggers.md)</code>
    - Subclasses: _None_
    - Uses: _None_

6. Function:
    - Description: `Function describes a function name and a python function to be executed by the object parser/handler.`
    - Subclasses: `TriggerFunction`
    - Uses: _None_

7. TriggerFunction:
    - Description: `A TriggerFunction is a function that begins with a conditional statement and ends with a function that acts on the datapoint or frame itself.`
