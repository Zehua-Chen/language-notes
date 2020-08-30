# `$this`

`$this` refers to `this` instance

# Accessing Properties and Methods

- Properties and methods are referenced without `$`
- Properties are declared with `$`
- Methods are declared as functions
- Properties and methods both require access modifiers

```php
<?php
class Person
{
  public $name = "peter";

  public function log()
  {
    printf("name = %s\n", $this->name);
  }
}

$person = new Person();
$person->log();
?>
```
