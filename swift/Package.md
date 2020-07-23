# C, C++, ObjC Target

- Header files goes under `target/include/` folder
  - `include/` can be a symlink
  - `target/include/target.modulemap` can be used to indicate what headers to
    expose

## Module Map

```
module Target {
  umbrella "<path to header>"
  export <files, patterns>
}
```
