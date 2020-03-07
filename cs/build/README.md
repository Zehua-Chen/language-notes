# MSBuild Overview

Projects starts with a `<Project></Project>` element

```xml
<Project>
</Project>
```

All build items has to be put inside `<ItemGroup></ItemGroup>` elements;
build settings are put inside `<PropertyGroup></PropertyGroup>` elements.

Both of these elements can have conditions that allow them to be conditionally
enabled.

```xml
<Project>
  <ItemGroup>
    ...
  </ItemGroup>
</Project>
```

Settings elements can have meta data children

```xml
<Project>
  <ItemGroup>
    <Foo>
      <Data />
    </Foo>
  </ItemGroup>
</Project>
```
