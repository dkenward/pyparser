# Schema
Most objects are defined under the mylib.io.json.schema.definitions.json file. 

## Definitions.json
1. MasterObject :-1:
    - Description: <code>MasterObject describes a master object to which all other objects are associated to in some way.</code>
    - Subclasses: <em>None</em>
    - Uses: <code>Function</code>
2. Frame
    - Description: <code>Holds multiple rows of data. Similar to a pandas DataFrame.</code>
    - Subclasses: <code>SpecialFrame</code>
    - Uses: <code>Row</code>
3. Row

4. Function:
    - Description: <code>Function describes a function name and a python function to be executed by the object parser/handler.</code>
    - Subclasses: <em>None</em>
    - Uses: <em>None</em>
