# Serialize and Desrialize Objects

- `JsonSerializer` provides static methods that
  - Directly serialize an object to json string
  - Desrialize json string to an object
- `JsonSerializerOptions` customzie the serialization and deserialization
  process
  - `PropertyNamingConvention`: transformation to apply to object's properties
  - `WriteIndented`: include indentation during serialization
