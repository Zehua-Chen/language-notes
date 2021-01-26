# Array Literals

```dart
List<Object> objects = [
  "",
  17,
  Person()
];

List<Person> people = <Person>[
  Person(),
  Person()
];
```

- List literals are of type `List<T>`
- To improve type inference, place `<Person>` before `[]`
  ```dart
  var people = <Person>[
    Person(),
    Person()
  ];
  ```
