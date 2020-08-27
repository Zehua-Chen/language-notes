# Builtin Tasks

## `<ZipDirectory />`

```xml
<Target Name="Zip" AfterTargets="Build">
  <ZipDirectory
    SourceDirectory="$(OutputPath)"
    DestinationFile="$(MSBuildProjectDirectory)\mm26-test-server.zip" />
</Target>
```

Zip a directory
