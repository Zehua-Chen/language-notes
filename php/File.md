# File

Php files' content are enclosed in `<?php ?>`

```php
<?php
// content goes here
?>
```

## Reference

Once a file is referenced, the current file would be able to reference its
content

- `include(path)`: if an error occurs, a warning would be emitted
- `require(path)`: if an error occurs, the program would crash
- `require_once(path)`: same as require, but make sure a file is refereced only
  once
- `include_once(path)`: same a include, but make sure a file is refereced only
  once
