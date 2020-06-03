# Serialize and Desrialize Objects

- `JsonSerializer` provides static methods that
  - Directly serialize an object to json string
  - Desrialize json string to an object
  - The serializer only handle's the object's public **properties**
- `JsonSerializerOptions` customzie the serialization and deserialization
  process
  - `PropertyNamingConvention`: transformation to apply to object's properties
  - `WriteIndented`: include indentation during serialization

# Custom Converters

```cs
struct Foo
{
  [JsonConverter(typeof(Converter))]
  public int Value;
}
```

- `Converter` needs to derive from `JsonConverter<T>`
