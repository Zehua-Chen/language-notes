# Trimming

.Net Core 3 SDK can trim published apps for unused **assemblies** ( this feature
mostly target self-contained applications)

To enable trimming, add the following to the project file

```xml
<PropertyGroup>
  <PublishTrimmed>true</PublishTrimmed>
</PropertyGroup>
```

Then build using

```
dotnet publish -r <rid> -c Release
```
