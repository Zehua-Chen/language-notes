# Tiered Compilation

Tiered compilation is enabled by default from .Net Core 3

When TC is enabled,

1. If AOT compiled code or ReadyToRun is available, these are used
2. Otherwise, JIT the method
   - Typically applies to generic methods for value types
   - Use Quick JIT, enabled by default for methods that don't contain loops
   - Use fully optimizing JIT for methods where Quick JIT is not used

Eventually, the fully optimizing JIT would create code in the background that
replace the code generated before

## Disabling TC

Code created using Quick JIT has worse performance, if this is an issue, disable
Quick JIT or disable TC completely

```xml
<PropertyGroup>
  <TieredCompilationQuickJit>false</TieredCompilationQuickJit>
</PropertyGroup>
```

```xml
<PropertyGroup>
  <TieredCompilation>false</TieredCompilation>
</PropertyGroup>
```

When Quick JIT or TC is disabled, all methods would be compiled by fully
optimizing JIT

Might need to perform a clean first for this to take effect.
